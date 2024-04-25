
listaNumerica = set()
while True:
 tamanho_conjunto = input("Pressione um número para definir o tamanho do seu conjunto: ")
 if tamanho_conjunto.isdigit():
       tamanho_conjunto = int(tamanho_conjunto)
       break
 else:
   print("Digite número, não uma tecla.")
print("O tamanho do seu conjunto é:", tamanho_conjunto)
tentativas = tamanho_conjunto
for i in range(tamanho_conjunto):
  numeros = input("Digite um número: ")
  numeros = int(numeros)
  listaNumerica.add(numeros)
for i in range(tamanho_conjunto):
  print(f"Você tem: {tentativas} tentativas")
  numeroRepetido = int(input("Digite um número que deseja ver se ele está no conjunto: "))
  if numeroRepetido in listaNumerica:
    print(f"O número {numeroRepetido} se encontra no conjunto.")
    break
  else:
    print(f"O número {numeroRepetido} não se encontra no conjunto.")
    tentativas -= 1
    if tentativas==0:
      print('Você não encontrou')
    

