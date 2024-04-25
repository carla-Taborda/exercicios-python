# 4. Par ou ímpar:
# Crie uma função que recebe um número como parâmetro e retorna True se o 
# número for par e False se for ímpar.

#numero = int(input("Digite o um número: "))

def par_ou_impar(numero):
    if numero %2  :
         print("o número é impar", False)
    else: 
        print("o número é par", True)
       
numero = int(input("Digite o um número: "))
resultado = par_ou_impar (numero)

# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         return f"{numero} é um número par."
#     else:
#         return f"{numero} é um número ímpar."