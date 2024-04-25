# 2. Acessando Valores:
# • Crie um dicionário com as informações de um amigo e acesse o valor da 
# chave "nome".
# • Crie um dicionário com as informações de um produto e acesse o valor da 
# chave "preço".


meu_dicionario = {'nome': 'Camila', 'idade':45, 'curso:': 'Analista de Sistemas', 'matricula':182300651}
print(meu_dicionario.get('nome')) #comando .get() determina o elemento

meu_dicionario1 = {'produto': 'vestido', 'preco': 100, 'cor': 'azul', 'tamanho': 'G'}
print(meu_dicionario1.get('preco'))