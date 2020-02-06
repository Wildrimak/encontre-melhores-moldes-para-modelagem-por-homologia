def antiga():

	original_dict = sequencia_teorica()
	analisada_list = sequencias_analisadas()
	resposta = converte_sequencia_original_sequencia_de_dicionarios(analisada_list, original_dict)
	ordem = 0
	for elemento in zip(resposta["GlmS"].keys(), resposta["GlmS"].values()):
		ordem+=1
		print(ordem, elemento)

def converte_sequencia_original_sequencia_de_dicionarios(sequencias_analisadas_list, original_dict):
	
	""" Exemplo retornado = {"GlmS": {
		(1, "A") : [4AMV, 1MOQ_A, 1MOS_A, ...], 
		(2, "B") : False, 
		(3, "C") : [4AMV, 1MOS_A, ...], 
		...}} """
	sequencia_de_dicionarios = {}
	
	""" Faz algo como {"GlmS" : {}} """
	nome_dicionario_str = original_dict.keys()[0]
	sequencia_de_dicionarios[nome_dicionario_str] = {}

	""" Algo como "ABCDE..." """
	sequencia_original_str = original_dict[original_dict.keys()[0]] 


	for sequence_analisada_dict in sequencias_analisadas_list:
		
		sequence_analisada_key = sequence_analisada_dict.keys()[0]
		sequence_analisada_str = sequence_analisada_dict[sequence_analisada_key]
		ordem = 0

		for par in zip(sequencia_original_str, sequence_analisada_str):

			ordem+=1

			if par[0] == par[1]:
				"""
				Pode existir ou pode nao existir uma lista no dicionario em questao
				Se nao existir deve se seta a lista com a chave em questao
				Se existir deve se incrementar a lista com a chave em questao para nao perder chaves anteriores
				"""
				if(not sequencia_de_dicionarios[nome_dicionario_str].has_key((ordem, par[0]))):
					sequencia_de_dicionarios[nome_dicionario_str][(ordem, par[0])] = [sequence_analisada_key]

				else:
					sequencia_de_dicionarios[nome_dicionario_str][(ordem, par[0])] += [sequence_analisada_key]

			else:
				"""
				Antes de setar como False perguntar pra sequencia_de_dicionarios se existe alguem com mesma chave como True
				Se nao existir eh que coloca essa chave como False
				Se eu for verdadeiro devo continuar verdadeiro, se nao que viro falso 
				"""
				if(not sequencia_de_dicionarios[nome_dicionario_str].has_key((ordem, par[0]))):
					sequencia_de_dicionarios[nome_dicionario_str][(ordem, par[0])] = []


	return sequencia_de_dicionarios

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

def sequencia_teorica():
	
	teorica = {"GlmS":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
	simples = {"GlmS": "abcdefghi"}
	return simples

def abrir_proteina(dict_molde):
	
	chave = dict_molde.keys()[0]
	sequencia = dict_molde[chave]

	aminoacidos = list()
	ordem = 0

	for sigla in sequencia:
		ordem+=1
		aminoacidos.append(Aminoacido(ordem, sigla))

	return aminoacidos

def abrir_proteinas_homologas():

	proteinas = list()

	for sequencia in sequencias_analisadas():
		aminoacidos = abrir_proteina(sequencia)
		sigla = sequencia.keys()[0]
		proteinas.append(Proteina(sigla, aminoacidos))

	return proteinas

def sequencias_analisadas():

	simula_sequencias = [
		{"SRE01":"ABDCEREFGGHIJJKKLMXQRZSTMUVWXYZ"},
		{"SRE02":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE03":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE04":"ABDCEREFGGHIJJKKLMXQRZSTMUVWXYZ"},
		{"SRE05":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE03":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE07":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE08":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE09":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE10":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE11":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE12":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE13":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE14":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE15":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE16":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE17":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE18":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE19":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE20":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE21":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE22":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
		{"SRE23":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE24":"ABBCDEAKFGHIOPQRLSSUVZFXYZSY"},
		{"SRE25":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ"},
		{"SRE26":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"}
	] 

	nova_sequencia = [
		{"S1":"ABCDeFGHIJKLMNoP"},
		{"S2":"ABcDeFGhIjKLMNOPqRStUVWXuZfsdfdvxvxcvsdfvdzczczc"},
		{"S3":"ABCDEFGHIJKLMNoPqrstuvwxyzfsdsfsdfsdfsdfsd"},
		{"S4":"abcdefghijklmNoPqRStuVWXYZ"},
		{"S5":"trsgacbdvxcvsgfPQbsfzxvXYZ"}
	]

	simples = [
		{"4AMV_A":"abcsss"},
		{"1MOQ_A":"sssdsf"},
		{"2JVX_A":"ssssssghi"}
	]

	return simples

def main():

	aminoacidos_molde = abrir_proteina(sequencia_teorica())

	proteina_molde = Proteina("Original", aminoacidos_molde)
	proteinas_homologas = abrir_proteinas_homologas()

	#print(proteina_molde)
	#for proteina_hmg in proteinas_homologas:
		#print(proteina_hmg)

	analisador = AnalisadorProteinas(proteina_molde, proteinas_homologas)
	retorno = analisador.deixar_somente_proteinas_necessarias()
	#print(analisador.proteina_resultante)
	#print("Somos iguais: " + str(analisador.is_equals))
	#print(analisador.PROTEINA_MOLDE)
	#print(str(analisador.proteinas_homologas))
	#print(str(analisador.copia_proteinas_homologas))

class AnalisadorProteinas:

	def __init__(self, proteina_molde, proteinas_homologas):
		
		self.proteina_resultante = self.uniao_de_aminoacidos_resultantes(proteina_molde, proteinas_homologas)
		self.is_equals = self.is_equals_molde(proteina_molde, self.proteina_resultante)
		self.PROTEINA_MOLDE = proteina_molde if self.is_equals else self.proteina_resultante
		self.proteinas_homologas = proteinas_homologas
		self.copia_proteinas_homologas = tuple(proteinas_homologas)


	def is_equals_molde(self, molde, resultante):

		if len(molde.aminoacidos) != resultante.aminoacidos:
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

			if self.PROTEINA_MOLDE != proteina_resultante:
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
		is_igual_original = True

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
						is_igual_original = True
					else:
						is_igual_original = False

		
		return Proteina("Resultante", lista_aminoacidos_resultantes)


if __name__ == '__main__':
	main()

