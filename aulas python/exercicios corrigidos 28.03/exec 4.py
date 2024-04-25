#4. União de conjuntos: 
#Escreva um programa que encontre a união de dois conjuntos. Utilize for para iterar pelos 
#elementos de ambos os conjuntos e adicionar à lista final. 

automovel = {'Renault'}
oleo = {'Elf'}
print (automovel.union(oleo))


automovel = {'Renault'}
oleo = {'Elf'}

# Cria uma lista vazia para armazenar a união
uniao = set()

# Itera pelos elementos do conjunto `automovel`
for elemento in automovel:
  # Adiciona o elemento à lista `uniao`
  uniao.add(elemento)

# Itera pelos elementos do conjunto `oleo`
for elemento in oleo:
  # Se o elemento não está na lista `uniao`, adiciona-o
  if elemento not in uniao:
    uniao.add(elemento)

# Imprime a lista `uniao`
print(uniao)