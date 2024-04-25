# 3. Média de três números:
# Crie uma função que recebe três números como parâmetros e retorna a média 
# aritmética dos três.

numero_1 = 5
numero_2 = 10
numero_3 = 25

def calculo_media(numero_1, numero_2, numero_3):
   media = numero_1 + numero_2 + numero_3/3
   return media

resultado = calculo_media(numero_1, numero_2,numero_3)
print('A média é: ', resultado)

#######

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o segundo número: "))


def calculo_media(numero_1, numero_2, numero_3):
    media = numero_1 + numero_2 + numero_3/3
    return media

resultado = calculo_media(numero_1, numero_2,numero_3)
print('A média é: ', resultado)