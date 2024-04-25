# 3. Adicionando e Removendo Elementos:
# • Crie um dicionário vazio e adicione as chaves "nome" e "idade" com seus 
# respectivos valores.
# • Crie um dicionário com as informações de um produto e remova a chave 
# "cor".
# • Crie um dicionário com as informações de um livro e adicione a chave 
# "tradução" com o valor "Sim".
# • Crie um dicionário com as informações de um filme e remova a chave "ano 
# de lançamento".

meu_dicionario_vazio = {}
meu_dicionario1 = {'nome': 'Camila', 'idade':45}
print(meu_dicionario1)


meu_dicionario_produto = {'produto': 'vestido', 'preco': 100, 'cor': 'azul', 'tamanho': 'G'}
if 'cor' in meu_dicionario_produto: meu_dicionario_produto.pop ('cor') # remover um elemento = pop
print(meu_dicionario_produto) 

meu_dicionario2 = {'livro': 'Amar','autor': 'Caroline Machado', 'ano publicao': 2020, 'genero': 'romance'}
meu_dicionario2.update({'tradução': 'sim'})  #adição = comando update
print(meu_dicionario2)


meu_dicionario3 = {'filme': 'Evita', 'diretor': 'Alan Paker', 'ano de lancamento':'1997', 'genero': 'drama'}
if 'ano de lancamento' in meu_dicionario3: meu_dicionario3.pop ('ano de lancamento') # remover um elemento = pop
print(meu_dicionario3)