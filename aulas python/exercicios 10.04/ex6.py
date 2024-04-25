def fatorial(numero):
 
                    print(f"Calculando fatorial({numero})...")
                    if numero == 0:
                        print(f"Fatorial({numero}) = 1")
                        return 1
                    else:
                        resultado = numero * fatorial(numero - 1)
                        print(f"Fatorial({numero}) = {numero} * fatorial({numero - 1})")
                        print(f"Fatorial({numero - 1}) = {resultado}")
                        return resultado

numero_fatorial = 6

resultado_fatorial = fatorial(numero_fatorial)
print(f"Fatorial de {numero_fatorial}:{resultado_fatorial}")