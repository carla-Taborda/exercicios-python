# 5. Tabuada:
# Crie uma função que recebe um número como parâmetro e imprime a tabuada 
# de 1 a 10 desse número.

def tabuada(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero*i}')

numero = int(input("Digite o um número: "))
tabuada(numero)
 






# def multiplica(x):
# global numero_global
# numero_global *= x
# return numero_global
# resultado_multiplicacao = multiplica(5)
# print(f"Resultado multiplicação: {resultado_multiplicacao}")  
# print(f"Número global: {numero_global}") 
