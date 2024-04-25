# 1. Classe Voo: 
# Crie uma classe Voo que represente um voo com as seguintes características: 
# Atributos 
# privados: codigo, companhia, origem, destino, horario_saida, horario_chega
# da, preco_passagem. 
# Métodos: 
# __init__: Inicializa o voo com os atributos necessários. 
# calcular_duracao_voo: Calcula a duração do voo (diferença entre 
# horários de saída e chegada). 
# aplicar_desconto: Aplica um desconto percentual no preço da 
# passagem. 
# mostrar_informacoes: Imprime as informações do voo (código, 
# companhia, origem, destino, horários, preço com desconto). 
 

class Voo:
    
    def __init__(self, codigo, companhia, origem, destino, horario_saida, horario_chegada, preco_passagem):
         self.codigo = codigo
         self.companhia = companhia
         self.origem = origem
         self.destino = destino
         self.horario_saida = horario_saida
         self.horario_chegada = horario_chegada
         self.preco_passagem = preco_passagem
         
         
    def calcular_duracao(self):
        duracao =  self.horario_chegada - self.horario_saida
        print(f"A viagem leva {duracao} horas")
        
    def aplicar_preco_com_desconto(self):
        desconto = self.preco_passagem * 0.5
        preco_com_desconto = self.preco_passagem - desconto
        print(f"O preço da passagem com desconto é: R${preco_com_desconto:.2f}")
        
    def apresentar_dados(self):
        print(f"Codigo: {self.codigo}, Companhia: {self.companhia}, Origem:{self.origem}, Destino:{self.destino}, Preço com desconto R${self.preco_passagem}")
        
voo1 = Voo(123456, "Inca", "Porto Alegre", "Florianópolis", 8, 10, 150)
voo1.apresentar_dados()
voo1.calcular_duracao()
voo1.aplicar_preco_com_desconto()