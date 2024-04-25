# 4. Subconjuntos:
# Crie um conjunto com os países da América do Sul e outro com os países que você já visitou.
# Verifique se o conjunto dos países que você já visitou é um subconjunto do conjunto dos países 
# da América do Sul.
america_do_sul = {'Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Chile', 'Bolivia', 'Colômbia', 'Equador', 'Guiana'}
america_do_sul_visitado = {'Brasil', 'Argentina', 'Uruguai', 'Paraguai'}
validacao_sub_americadosulvisitado = america_do_sul_visitado.issubset(america_do_sul) #todos os paises visitados são um subconjunto da america do sul.
print(validacao_sub_americadosulvisitado)