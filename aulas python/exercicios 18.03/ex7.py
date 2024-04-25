#7. Verificar se um valor está presente em uma tupla:
#Modifique o código para verificar se um determinado valor está presente na tupla.

tupla = (5, 6, 7, 8, 9)
indice_lucas =  tupla.index(8)
if 8 in tupla:
    print(f"o valor esta presente na tupla em qual posição:{indice_lucas}")
else:
    print(f"o valor não esta presente")