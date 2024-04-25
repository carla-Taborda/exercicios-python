#3. Diferença de conjuntos: 
#Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
#elementos e if para verificar a presença no primeiro conjunto e não no segundo.

conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {4, 5, 6, 7, 8, 9}

diferenca = set()

for i in conjunto1:
    if i not in conjunto2:
        diferenca.add(i)
    elif i not in conjunto1:
        diferenca.add(i)  

print(f"A diferença entre os conjuntos é:{conjunto1.symmetric_difference(conjunto2)}")
