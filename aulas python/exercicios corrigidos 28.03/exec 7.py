#7. Remoção de elementos duplicados:
#Escreva um programa que remova elementos duplicados de um conjunto. Utilize while para iterar 
#pelo conjunto e if para verificar a presença de elementos duplicados.


lista = [1,2,3,8,5,6,9,7,10,4,3,10]
conjunto = set(lista) # transformando lista em conjunto.

conjunto_sem_duplicados = set(lista)  # Conjunto para armazenar elementos únicos.
while conjunto:
    elemento = conjunto.pop()
    if elemento not in conjunto_sem_duplicados:
        conjunto_sem_duplicados.add(elemento)

print(f"Conjunto original:{lista}")
print(f"Conjunto sem duplicados: {conjunto_sem_duplicados}")