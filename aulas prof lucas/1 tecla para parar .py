# Cria um conjunto vazio para armazenar os números
listaNumerica = set()

# Loop infinito para permitir a entrada de números
while True:
  # Solicita ao usuário que pressione uma tecla para parar de adicionar números
  tecla_parada = input("Pressione uma tecla para parar de agregar números ao conjunto: ")

  # Verifica se a tecla pressionada é um dígito
  if not tecla_parada.isdigit():
    # Se não for um dígito, sai do loop infinito
    break
  else:
    # Se for um dígito, informa que o usuário deve digitar uma tecla e não um número
    print("Digite uma tecla, não um número.")

# Imprime a tecla que o usuário digitou para parar
print("Sua tecla para parar é:", tecla_parada)

# Loop infinito para permitir a entrada de números
while True:
  # Solicita ao usuário que digite um número
  numeros = input("Digite um número: ")

  # Verifica se o número digitado é a tecla para parar e se o conjunto não está vazio
  if numeros == tecla_parada and listaNumerica != []:
    # Se sim, informa que está fechando a lista e sai do loop infinito
    print(f"Fechando lista...")
    break
  elif not numeros.isdigit():
    # Se o número digitado não for um dígito, informa que não é possível adicionar letras ou espaços vazios ao conjunto e continua o loop
    print('Não pode adicionar letras ou espaços vazios ao conjunto')
    continue

  # Converte o número digitado para um inteiro
  numeros = int(numeros)

  # Adiciona o número ao conjunto
  listaNumerica.add(numeros)

# Loop infinito para permitir a busca de números no conjunto
while True:
  # Solicita ao usuário que digite um número para verificar se está no conjunto
  numeroRepetido = int(input("digite um número que deseja ver se ele está no conjunto: "))

  # Verifica se o número digitado está no conjunto
  if numeroRepetido in listaNumerica:
    # Se estiver, informa que o número está no conjunto e sai do loop infinito
    print(f"O número {numeroRepetido} se encontra no conjunto.")
    break
  else:
    # Se não estiver, informa que o número não está no conjunto
    print(f"O número {numeroRepetido} não se encontra no conjunto.")



#Exemplos de como determinar um tamanho de conjunto:
#tamanho_conjunto = int(input("Digite o tamanho do conjunto: "))

#conjuntoNumerico = set()

#for i in range(tamanho_conjunto):
#    numero = int(input("Digite um número: "))
#    conjuntoNumerico.add(numero)
        
#tamanho_conjunto = int(input("Digite o tamanho do conjunto: "))

#numeros = []

#while len(numeros) < tamanho_conjunto:
#    numero = int(input("Digite um número: "))
#    numeros.append(numero)