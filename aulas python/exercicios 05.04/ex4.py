# 4. Percorrendo Dicionários:
# • Crie um dicionário com as informações de um amigo e imprima cada chave 
# e valor em linhas separadas.
# • Crie um dicionário com as informações de um produto e imprima todos os 
# valores em uma única linha.
# • Crie um dicionário com as informações de um livro e imprima as chaves 
# "título" e "autor" em uma única linha.
# • Crie um dicionário com as informações de um filme e imprima as chaves 
# "nome" e "diretor" em uma única linha

# meu_dicionario_amigo = {'nome': 'Camila', 'idade':45, "curso":'Analista de Sistemas', 'matricula':182300651}
# print(meu_dicionario_amigo.get('nome'))
# print(meu_dicionario_amigo.get('idade'))
# print(meu_dicionario_amigo.get('curso'))
# print(meu_dicionario_amigo.get('matricula'))  #comando get.() seleciona o item que será impresso.

meu_dicionario1 = {'produto': 'vestido', 'preco': 100, 'cor': 'azul', 'tamanho': 'G'}
print(meu_dicionario1.values())

meu_dicionario2 = {'livro': 'amar','autor': 'Caroline Machado', 'ano publicao': 2020, 'genero': 'romance'}
print(f"{meu_dicionario2['livro']}, {meu_dicionario2['autor']}")


meu_dicionario3 = {'filme': 'Evita', 'diretor': 'Alan Paker', 'ano de lancamento':'1997', 'genero': 'drama'}
print(f"{meu_dicionario3['filme']}, {meu_dicionario3['diretor']}")