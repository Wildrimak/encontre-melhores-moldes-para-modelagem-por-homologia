# -*- coding: utf-8 -*-
import os

def directory_protein_target():

	current_directory = os.getcwd()
	files = os.listdir(current_directory)
	files.sort()
	protein_directory = files[2]
		
	target_directory = os.path.join(current_directory, protein_directory)
	protein_file = os.listdir(target_directory)[0]

	target = os.path.join(target_directory, protein_file)

	return target

def directory_protein_moldes():

	current_directory = os.getcwd()
	files = os.listdir(current_directory)
	files.sort()
	sequences_directory = files[3]
	
	moldes_directory = os.path.join(current_directory, sequences_directory)
	moldes_file = os.listdir(moldes_directory)[0]

	moldes = os.path.join(moldes_directory, moldes_file)

	return moldes

def sequencia_teorica(which=0):
	
	teorica = {"GlmS":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
	simples = {"GlmS": "abcdefghij"}

	file = directory_protein_target()
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
		{"SRE11":"ABCDEFFBJGHLIJWKLVMNOZPQTRSNTUVWXYZ\n"}
	] 

	simples = [
		{"7ABQ_A":"abzsssshsj"},
		{"8SOQ_A":"abcdefghsj"},
		{"9PVX_A":"sssssfghij"}
	]

	obtidas = obter_proteinas_homologas_from_file()

	lista = [obtidas, simula_sequencias, simples]

	return lista[which]

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
	file = directory_protein_moldes()
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

	def __eq__(self, obj):
		return isinstance(obj, Aminoacido) and obj.ordem == self.ordem and obj.sigla == self.sigla

class Proteina:
	def __init__(self, sigla, aminoacidos):
		self.sigla = sigla
		self.aminoacidos = aminoacidos
		self.tamanho = len(aminoacidos)
		self.score = self.calcula_score()	
		self.percentual = self.calcula_percentual()

	def calcula_score(self):
		
		score = 0
		
		for aminoacido in self.aminoacidos:
			if aminoacido.sigla != "!":
				score+=1

		return score

	def compare(self, proteina):


		meus_aminoacidos = list(self.aminoacidos)
		aminoacidos_da_outra = list(proteina.aminoacidos)
		minha_qtd_aminoacidos = len(meus_aminoacidos)
		qtd_aminoacidos_outra = len(aminoacidos_da_outra)

		if minha_qtd_aminoacidos != qtd_aminoacidos_outra:
			
			if (minha_qtd_aminoacidos < qtd_aminoacidos_outra):
				
				preenche_com = qtd_aminoacidos_outra - minha_qtd_aminoacidos
				for i in xrange(preenche_com):
					meus_aminoacidos.append(None)

			else:

				preenche_com = minha_qtd_aminoacidos - qtd_aminoacidos_outra
				for i in xrange(preenche_com):
					aminoacidos_da_outra.append(None)


		qtd_aminoacidos_iguais = 0


		monta_string = {
				"cima" : {self.sigla : []}, 
				"baixo" : {proteina.sigla : []}
			}

		for par in zip(meus_aminoacidos, aminoacidos_da_outra):
			
			my_amino, other_amino = par[0], par[1]


			if my_amino != None and other_amino != None:

				monta_string["cima"][self.sigla].append(my_amino)
				monta_string["baixo"][proteina.sigla].append(other_amino)

				if my_amino.sigla == other_amino.sigla:
		
					qtd_aminoacidos_iguais += 1
		
			else:
				monta_string["cima"][self.sigla].append("!")
				monta_string["baixo"][proteina.sigla].append("!")
				
		
		representation = self.__monta_string(monta_string, proteina)
		
		percentual_de_similaridade = 0

		if proteina.tamanho != 0: 
			percentual_de_similaridade = (qtd_aminoacidos_iguais * 100.0)/proteina.tamanho

		return {
				"representation" : representation, 
				"qtd_aminoacidos_iguais" : qtd_aminoacidos_iguais, 
				"percentual_de_similaridade" : percentual_de_similaridade
			}

	def __monta_string(self, dicionario, proteina):
		
		string = ""

		lista_de_cima = dicionario["cima"][self.sigla]
		lista_de_baixo = dicionario["baixo"][proteina.sigla]
		lista_de_centro = list()

		count = 0
		for par in zip(lista_de_cima, lista_de_baixo):
			count+=1

			my_amino, other_amino = par[0], par[1]


			print(my_amino)
			print(other_amino)

			if my_amino == other_amino:
				print("Entramos")
				lista_de_centro.append(str(count) + "=")
			else:
				lista_de_centro.append(str(count) + "!")

		multiplo = len(lista_de_cima)

		__tamanho_sigla = len([i for i in self.sigla]) 
		__tamanho_outra_sigla = len([i for i in proteina.sigla])

		espacador = __tamanho_sigla if __tamanho_sigla > __tamanho_outra_sigla else __tamanho_outra_sigla


		string += self.sigla.ljust(espacador)+ " "

		for i in xrange(multiplo):
			string += str(lista_de_cima[i])

		string+="\n" + ">"*espacador + " "

		for i in xrange(multiplo):
			string+=lista_de_centro[i]

		string+="\n" + proteina.sigla.ljust(espacador) + " "

		for i in xrange(multiplo):
			string += str(lista_de_baixo[i])

		return string



	def calcula_percentual(self):
		#TENTAR ENTENDER QUANDO EU TO CRIANDO UMA PROTEINA DE TAMANHO 0
		percentual = 0 if self.tamanho == 0 else (self.score * 100.0)/self.tamanho
		return percentual

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

		self.proteina_de_entrada = proteina_molde
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

	def write(self):

		current_directory = os.getcwd()
		files = os.listdir(current_directory)
		files.sort()
		results_directory = files[4]
		target_directory = os.path.join(current_directory, results_directory)
		

		final_file = os.path.join(target_directory, "log-resultados")


		arquivo_resultado = open(final_file, 'w')

		proteinas = self.deixar_somente_proteinas_necessarias()
		arquivo_resultado.write("Qtd de proteinas que entraram: " + str(len(self.copia_proteinas_homologas)) + "\n")
		arquivo_resultado.write("Qtd de proteinas necessarias: " + str(len(proteinas)) + "\n")
		arquivo_resultado.write("As sequencias ficam igual a original? " + str(self.is_equals) + "\n")
		arquivo_resultado.write("Qtd de aminoacidos da proteina de entrada: " + str(self.proteina_de_entrada.tamanho) + "\n")
		arquivo_resultado.write("Score obtido: " + str(self.PROTEINA_MOLDE.score) + "\n")
		arquivo_resultado.write("Percentual em relação ao melhor que se pode obter: " + str(self.PROTEINA_MOLDE.percentual) + "\n")


		nomes = list()
		for proteina in proteinas:
			nomes.append(proteina.sigla)

		nomes.sort()
		arquivo_resultado.write("Uteis: " + str(nomes) + "\n\n")

		for proteina in proteinas:
			result = proteina.compare(self.PROTEINA_MOLDE)

			arquivo_resultado.write(str(result["representation"]) + "\n\n")
			arquivo_resultado.write("Percentual de similaridade: " + str(result["percentual_de_similaridade"]) + "\n")
			arquivo_resultado.write("Qtd de aminoacidos iguais: " + str(result["qtd_aminoacidos_iguais"]) + "\n\n")


		arquivo_resultado.close()

def main():

	which = int(input("0 - Real, 1 - Complex, 2 - Sample: "))

	aminoacidos_molde = abrir_proteina(sequencia_teorica(which))
	proteinas_homologas = abrir_proteinas_homologas(sequencias_analisadas(which))
	
	proteina_molde = Proteina("Original", aminoacidos_molde)
	analisador = AnalisadorProteinas(proteina_molde, proteinas_homologas)
	
	analisador.write()



if __name__ == '__main__':
	main()

