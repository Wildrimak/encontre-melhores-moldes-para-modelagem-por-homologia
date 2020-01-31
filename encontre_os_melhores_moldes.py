def main():

	original_dict = sequencia_teorica()


	analisada_list = sequencias_analisadas()
	analisada_primeira_dict = analisada_list[0]
	
	resposta = converte_sequencia_original_sequencia_de_dicionarios(analisada_list, original_dict)
	print(resposta)
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

def _calcula_score(sequencia_teorica, sequence_analisada):
	
	score_int = 0

	for par in zip(sequencia_teorica, sequence_analisada):
		if par[0] == par[1]:
			score_int+=1

	return score_int

def _count(sequence):
	return len([c for c in sequence])

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
		{"SRE24":"ABBCDEAKFGHIOPQRLSTUVZFXYZSY"},
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

	return nova_sequencia


def sequencia_teorica():
	
	teorica = {"GlmS":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

	return teorica


if __name__ == '__main__':
	main()