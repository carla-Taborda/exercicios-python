#1. Verificação de elemento em conjunto:
#Escreva um programa que verifique se um determinado elemento está presente em um conjunto. 
#Utilize if e else para exibir mensagens informativas.

conjunto = {'Bibiana', 30} #Criei uma variavel chamada conjunto
item = input("Digite um item do conjunto") #Input para o usuario digitar um item do conjunto


if item in conjunto: # Se a condição (elemento) está no conjunto
    print(f"A {item} está presente no conjunto") # verdadeiro 
else: # ou  condição (elemento) não esta.
    print("Não está no conjunto")