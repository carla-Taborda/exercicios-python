#1. Soma de dois números:
#Escrever um programa que soma dois números digitados pelo usuário e imprime o 
#resultado

#numero = int(input("Digite um número: "))
#numero1 = int(input("digite outro número: "))
#soma = numero + numero1
#print (soma)

#2. Comparação de duas strings:
#Escrever um programa que compara duas strings digitadas pelo usuário e informa 
#se elas são iguais ou diferentes.

#palavra = input("Digite uma palavra: ")
#palavra2 = input("Digite uma segunda palavra: ")
#if  palavra == palavra2:
#    print(" As palavras são iguais") 
#else: 
#    print(" As palavras são diferentes")


#3. Verificação se um número é par ou ímpar:
#Escrever um programa que verifica se um número digitado pelo usuário é par ou 
#ímpar e informa o resultado.

#numero = int(input("Digite um número: "))
#if numero % 2 == 0:
 #   print("par") 
#else:
 #   print("impar")
#4. Cálculo da média de três notas:
#Escrever um programa que calcula a média de três notas digitadas pelo usuário e 
#imprime o resultado.

#nota = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#nota3 = float(input("digite a terceira nota: "))
#soma = (nota + nota2 + nota3) / 3 
#print(soma)

# 5. Concatenar duas strings e verificar o tamanho da string resultante:
#Escrever um programa que concatena duas strings digitadas pelo usuário e 
#informa o tamanho da string resultante.
#palavra = input("Digite uma palavra: ")
#palavra1 = input("digite outra palavra: ")
#tamanhoPalavra = len(f"{palavra}{palavra1}")
#print(tamanhoPalavra)

#6. Simular um jogo de adivinhação:
#Escrever um programa que simula um jogo de adivinhação, onde o usuário deve 
#adivinhar um número secreto

#numero = int(input(" Digite o número que estou pensando: "))
#while(numero != 5):
#    print("Voce errou")
#    numero = int(input(" Digite o número que estou pensando: "))   
#print("acertou!")


#7. Calcular a área de um triângulo:
#Escrever um programa que calcula a área de um triângulo, a partir da base e da 
#altura digitadas pelo usuário.
#A fórmula para obter a área do triangulo é A = b*al/2

#base = int(input("Digite o valor da base: "))
#altura = int(input("Digite o valor da altura: "))
#formula = base*altura /2
#print (formula)

#8. Converter temperatura de Celsius para Fahrenheit:
#Escrever um programa que converte uma temperatura de Celsius para Fahrenheit, 
#a partir da temperatura em Celsius digitada pelo usuário.
#A fórmula para conversão de Celsius para Fahrenheit é: F = (C * 9/5) + 32

#temperaturaCelsius = float(input("Digite a temperatura em Celsius: "))
#formula = (temperaturaCelsius * 9 / 5) + 32
#print (formula)

#9. Verificar se um caractere está presente em uma string:
#Escrever um programa que verifica se um caractere digitado pelo usuário está
#presente em uma string e informa o resultado.

#caracter = input("Digite um caracter: ")
#string = "Exemplo de string"

#if caracter in string:
  #print(f"O caractere '{caracter}' está presente na string.")
#else:
  #print(f"O caractere '{caracter}' não está presente na string.")


#10. Calcular o fatorial de um número:
#Escrever um programa que calcula o fatorial de um número digitado pelo usuário.
#Lembrando: O código calcula o fatorial de um número usando um loop for. O 
#fatorial de um número é o produto de todos os números inteiros positivos menores 
#ou iguais a ele. Por exemplo, o fatorial de 5 é 120, pois 120 = 1 * 2 * 3 * 4 * 5

numero = int(input("Digite um número: "))

fatorial = 1

for i in range(1, numero + 1):
  fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")
