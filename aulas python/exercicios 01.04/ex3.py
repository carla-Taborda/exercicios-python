# 3. Diferença de Conjuntos:
# Crie um conjunto com os livros que você já leu e outro com os livros que você deseja ler.
# Encontre os livros que você ainda não leu e imprima a lista

livros_lidos = {'Orgulho e preconceito','Em chamas','A cidade do sol'}
livros_lerei = {'Jogos vorazes','A revolta', 'Assim acaba'}
livros_desejo_ler = livros_lerei - livros_lidos 
print("Livros que pretendo ler:")
for livro in livros_lerei:print(livro)