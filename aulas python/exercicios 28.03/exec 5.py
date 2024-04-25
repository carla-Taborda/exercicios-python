#5. Subconjuntos: 
#Escreva um programa que determine se um conjunto é subconjunto de outro. Utilize for para iterar 
#pelos elementos do primeiro conjunto e if para verificar a presença no segundo. 

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

subconjunto = conjunto1.issubset(conjunto2)
print(subconjunto)