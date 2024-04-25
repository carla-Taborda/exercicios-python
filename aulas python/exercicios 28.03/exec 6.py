#6. Ordenação de elementos em um conjunto: 
#Escreva um programa que ordene os elementos de um conjunto em ordem crescente ou 
#decrescente. Utilize for para iterar pelos elementos e if para comparar e trocar posições.

numeros = {1,2,3,8,5,6,9,7,10,4}
lista_crescente = list(sorted(numeros))
print(f"Lista Crescente{lista_crescente}")
lista_decrescente = list(sorted(numeros,reverse=True))
print(f"Lista Decrescente{lista_decrescente}")
 
 
for i in lista_crescente:
    print(f"{lista_crescente}")
    if lista_crescente == lista_decrescente:
        print(f"{lista_crescente}")




# for fruta in conjunto:
#               print("if fruta == fruta_procurada:")
#               if fruta == fruta_procurada:
#                 print(f"Encontramos a fruta {fruta_procurada}!")