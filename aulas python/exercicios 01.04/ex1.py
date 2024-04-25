# 1. Verificação de Elemento:
# Crie um conjunto com os nomes de seus amigos.
# Peça ao usuário para digitar um nome.
# Verifique se o nome está no conjunto e informe o usuário se ele é seu amigo ou não.

meus_amigos = {' Andreza', 'Camily','Luana', 'Audrey', 'Bruna'} 
nome = input("Digite um nome para verificar se é meu amigo:") #inserção da verificação.
if nome in meus_amigos: #se, uma condição:"tal nome estiver no conjunto"
    print(nome,"é meu amigo!") 
else:    # se a condição determinada não é executada.
    print(nome,"não é meu amigo")
    
