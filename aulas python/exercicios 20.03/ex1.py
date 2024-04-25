#1. Encontrar o Maior Valor em uma Lista:
# list_int = [10 , 20, 30]
# maior_valor = max(list_int)
# print("o maior valor é:", maior_valor)

lista = [] 
while True:
  tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
  if not tecla_parada.isdigit(): #A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
    break
  else:
    print("Digite uma tecla, não um número.")


while True:
    
    numero = input("digite um numero: ")
    if numero == tecla_parada:
        break
    valor = int(numero)
  
    lista.append(numero) #agregar um valor a lista
 
print(f"o maior valor é:{max(lista)}")



# while len(lista)<= 3:
#     numero = input("digite um numero: ")
#     valor = int(numero)
#     lista.append(numero)
# print(f"o maior valor é:{max(lista)}")