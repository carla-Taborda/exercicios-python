#6. Ordenação de elementos em um conjunto: 
#Escreva um programa que ordene os elementos de um conjunto em ordem crescente ou 
#decrescente. Utilize for para iterar pelos elementos e if para comparar e trocar posições.

numeros = {1,2,3,8,5,6,9,7,10,4}
lista_crescente = list((numeros))

 
 
# Converte o conjunto em uma lista
lista_crescente = list(numeros)

# Loop para iterar pelos elementos da lista
for i in range(len(lista_crescente) - 1):
  # Loop para comparar com os elementos posteriores
  for j in range(i + 1, len(lista_crescente)):
    # Comparação dos elementos
    if lista_crescente[j] < lista_crescente[i]:
      # Troca dos elementos
      temp = lista_crescente[i]
      lista_crescente[i] = lista_crescente[j]
      lista_crescente[j] = temp

# Impressão da lista ordenada
print(set(lista_crescente))
    



# for fruta in conjunto:
#               print("if fruta == fruta_procurada:")
#               if fruta == fruta_procurada:
#                 print(f"Encontramos a fruta {fruta_procurada}!")