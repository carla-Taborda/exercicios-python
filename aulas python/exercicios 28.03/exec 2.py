#2. Interseção de conjuntos: 
#Escreva um programa que encontre a interseção de dois conjuntos. Utilize for para iterar pelos 
#elementos e if para verificar a presença em ambos os conjuntos. 
meu_conjunto = {'Honda', 'Renault'}
outro_conjunto = {'Mclaren', 'Williams'}

meu_conjunto_intersecao = set()

for elemento in meu_conjunto:
    if elemento in outro_conjunto:
        meu_conjunto_intersecao.add(elemento)

print("A interseção dos conjuntos é:", meu_conjunto_intersecao)
