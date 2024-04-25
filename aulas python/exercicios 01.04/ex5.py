# 5. Ordenação de Elementos:
# Crie um conjunto com números de 1 a 10.
# Ordene os elementos do conjunto em ordem crescente e decrescente e imprima as listas 
# ordenadas
numeros = {1,2,3,8,5,6,7,4,9,10}
lista_ordenada = list(sorted(numeros))#conjunto se transforma em lista
print(lista_ordenada)
lista_decrecente =list(sorted(numeros, reverse=True))
#conjunto_decrescente = sorted(numeros) 
print(lista_decrecente)
