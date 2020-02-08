# -*- coding: utf-8 -*-
def sequencia_teorica(which=0):
	
	teorica = {"GlmS":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
	simples = {"GlmS": "abcdefghi"}

	file = "/home/wildrimak/projects/Aperfeiçoar-e-colocar-no-github/EncontreMelhoresMoldesParaModelagemPorHomologia/sequencias/glms"
	arquivo = open(file, 'r')
	conteudo = arquivo.readlines()
	arquivo.close()

	one_row = ""

	for line in conteudo:
		one_row+=line[:-1]

	one_row = one_row[:-1]
	
	real = {"GlmS": one_row}

	lista = [real, teorica, simples]

	return lista[which]

def sequencias_analisadas(which=0):

	simula_sequencias = [
		{"SRE01":"ABDCEREFGGHIJJKKLMXQRZSTMUVWXYZ\n"},
		{"SRE10":"MCGIVGYVGRRPAYVVVMDALRRMEYRGYDSSGIALVDGGTLTVRRRAGRLANLEEAVAEMPSTALSGTTGLGHTRWA\n"},
		{"SRE11":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"}
	] 

	nova_sequencia = [
		{"S1":"ABCDeFGHIJKLMNoP"},
		{"S2":"ABcDeFGhIjKLMNOPqRStUVWXuZfsdfdvxvxcvsdfvdzczczc"}
	]

	simples = [
		{"8OOQ_A":"ssssssshs"},
		{"9PVX_A":"sssssfghi"}
	]

	obtidas = obter_proteinas_homologas_from_file()

	lista = [obtidas, simula_sequencias, nova_sequencia, simples]

	return lista[0]

def abrir_proteina(dict_molde):
	
	chave = dict_molde.keys()[0]
	sequencia = dict_molde[chave]

	aminoacidos = list()
	ordem = 0

	for sigla in sequencia:
		ordem+=1
		aminoacidos.append(Aminoacido(ordem, sigla))

	return aminoacidos

def abrir_proteinas_homologas(sequencias):

	proteinas = list()

	for sequencia in sequencias:
		aminoacidos = abrir_proteina(sequencia)
		sigla = sequencia.keys()[0]
		proteinas.append(Proteina(sigla, aminoacidos))

	return proteinas

def obter_proteinas_homologas_from_file():
	file = "/home/wildrimak/projects/Aperfeiçoar-e-colocar-no-github/EncontreMelhoresMoldesParaModelagemPorHomologia/sequencias/blast-glms"
	arquivo = open(file, 'r')
	conteudo = arquivo.readlines()
	arquivo.close()

	proteina = dict()

	for line in conteudo:
		if line.startswith(">"):
			chave = str(line[1:7])
		else:
			if line.endswith("\n"):
				line = line[:-1]
			try:
				proteina[chave]
			except KeyError as e:
				proteina[chave] = line
			else:
				proteina[chave]+= line

	lista_de_dict_proteinas = list()

	for par in zip(proteina.keys(), proteina.values()):
		chave, valor = par[0], par[1]
		dic = {chave:valor}
		lista_de_dict_proteinas.append(dic)

	return lista_de_dict_proteinas
	
class Aminoacido:

	def __init__(self, ordem, sigla):
		self.ordem = ordem
		self.sigla = sigla

	def __str__(self):
		return str(self.ordem) + "" + self.sigla

class Proteina:
	def __init__(self, sigla, aminoacidos):
		self.sigla = sigla
		self.aminoacidos = aminoacidos	

	def __str__(self):

		retorno = ""	
		retorno += "<<\n\tProteina: " + str(self.sigla) + ",\n\tAminoacidos: [" 

		for aminoacido in self.aminoacidos:
			retorno += "<" + str(aminoacido) + ">-"

		retorno = retorno[:-1]
		retorno += "]\n>>"
		return retorno

class AnalisadorProteinas:

	def __init__(self, proteina_molde, proteinas_homologas):
		
		self.proteina_resultante = self.uniao_de_aminoacidos_resultantes(proteina_molde, proteinas_homologas)
		self.is_equals = self.is_equals_molde(proteina_molde, self.proteina_resultante)
		self.PROTEINA_MOLDE = proteina_molde if self.is_equals else self.proteina_resultante
		self.proteinas_homologas = proteinas_homologas
		self.copia_proteinas_homologas = tuple(proteinas_homologas)


	def is_equals_molde(self, molde, resultante):

		if len(molde.aminoacidos) != len(resultante.aminoacidos):
			return False

		for par in zip(molde.aminoacidos, resultante.aminoacidos):
			aminoacido_molde  = par[0]
			aminoacido_resultante = par[1]

			if aminoacido_molde.ordem != aminoacido_resultante.ordem: 
				return False
			if aminoacido_molde.sigla != aminoacido_resultante.sigla:
				return False

		return True	


	def deixar_somente_proteinas_necessarias(self):

		proteina_corrente = None
		quantidade_de_analises = len(self.copia_proteinas_homologas)
		dicionario_atualizado = self.dicionarizar_lista_de_proteinas(self.copia_proteinas_homologas)

		for enesima in xrange(quantidade_de_analises):
			proteina_corrente = dicionario_atualizado[enesima]
			dicionario_atualizado[enesima] = None
			nova_lista_de_proteinas_homologas = self.transformar_em_lista_dicionario_de_proteinas(dicionario_atualizado)
			proteina_resultante = self.uniao_de_aminoacidos_resultantes(self.PROTEINA_MOLDE, nova_lista_de_proteinas_homologas)
			
			if not self.is_equals_molde(self.PROTEINA_MOLDE, proteina_resultante):
				dicionario_atualizado[enesima] = proteina_corrente

		proteinas_retornadas = self.transformar_em_lista_dicionario_de_proteinas(dicionario_atualizado)

		return proteinas_retornadas
			
	def dicionarizar_lista_de_proteinas(self, proteinas):
		
		dicionario = dict()
		for i in xrange(len(proteinas)):
			dicionario[i] = proteinas[i]

		return dicionario

	def transformar_em_lista_dicionario_de_proteinas(self, dicionario_de_proteinas):

		lista = list()
		chaves = dicionario_de_proteinas.keys()
		chaves = chaves.sort()

		for key in dicionario_de_proteinas:
			value = dicionario_de_proteinas[key]

			if (value != None):
				lista.insert(key-1, value)

		return lista

	def uniao_de_aminoacidos_resultantes(self, proteina_molde, lista_de_proteinas_homologas):
		lista_aminoacidos_resultantes = []

		for proteina_homologa in lista_de_proteinas_homologas:
			for par in zip(proteina_homologa.aminoacidos, proteina_molde.aminoacidos):
				
				aminoacido_homologo = par[0]
				aminoacido_molde = par[1]

				position = aminoacido_molde.ordem - 1

				try:
					tem_alguem_aqui = lista_aminoacidos_resultantes[position]
				except IndexError as nao_tem_ninguem_ainda:
					
					if aminoacido_homologo.sigla == aminoacido_molde.sigla:
						lista_aminoacidos_resultantes.append(aminoacido_homologo)
					else:
						lista_aminoacidos_resultantes.append(Aminoacido(aminoacido_homologo.ordem, "!"))
				else:
					if aminoacido_homologo.sigla == aminoacido_molde.sigla:
						lista_aminoacidos_resultantes.pop(position)
						lista_aminoacidos_resultantes.insert(position, aminoacido_homologo)

		
		return Proteina("Resultante", lista_aminoacidos_resultantes)

def main():

	aminoacidos_molde = abrir_proteina(sequencia_teorica())
	proteina_molde = Proteina("Original", aminoacidos_molde)
	
	#proteinas_homologas = abrir_proteinas_homologas(sequencias_analisadas())
	proteinas_homologas = abrir_proteinas_homologas(obter_proteinas_homologas_from_file())

	analisador = AnalisadorProteinas(proteina_molde, proteinas_homologas)
	retorno = analisador.deixar_somente_proteinas_necessarias()

	for protein in  retorno:
		print(protein)

	print(len(retorno))

if __name__ == '__main__':
	main()

