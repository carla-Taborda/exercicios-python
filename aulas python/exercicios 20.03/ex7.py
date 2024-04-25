#7. Verificar se um Valor Está Presente em uma Lista: 
# lista = [10, 20, 30]
# valor_presente = int(input("qual valor presente na lista: ")) #converter uma string em inteiro
# #valor_int = int(valor_presente) #converter uma string em inteiro
# valor = lista.count(valor_presente)
# if  valor == 0:
#     print("o valor não está presente")
# else:
#     print("o valor esta na lista")


    
lista = []    
while True:
    tecla_parada = input("pressione qualquer tecla para parar de agregar números à lista: ") # comando que para de colocar valor a lista.
    if not tecla_parada.isdigit(): 
        break
    else:
        print("Digite uma tecla, não um numero: ")  
        
while True:   
    numero = input("digite um numero: ")   # numero é digitado pelo usuário
    if numero == tecla_parada: #se for igual a tecla parada, o loop para.
        break
    valor = int(numero)
    lista.append(numero)
    
valor_presente = int(input("qual valor presente na lista: "))    
        
    
    
    
    
    
    