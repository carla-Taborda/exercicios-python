# 4. Classe Veículo e Carro:
# Crie uma classe abstrata Veiculo com os atributos marca, modelo e ano.
# Crie uma classe Carro que herde de Veiculo.
# Adicione à classe Carro os atributos cor, numero_portas e tipo_cambio.
# Implemente 
# métodos ligar(), desligar(), acelerar(), frear() e descrever() nas 
# classes Veiculo e Carro.
# Crie um objeto carro1 e chame os métodos adequados.

class Veiculo: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, cor, numero_portas, tipo_cambio):
        self.cor = cor
        self.numero_portas = numero_portas
        self.tipo_cambio = tipo_cambio

    def ligar(self):
        raise NotImplementedError
    
    def desligar(self):
        raise NotImplementedError
    
    def acelerar(self):
        raise NotImplementedError
    
    def frear(self):
        raise NotImplementedError
    
    def descrever(self):
        raise NotImplementedError

carro1 = Carro 
carro1.ligar
carro1.desligar
carro1.acelerar
carro1.frear
carro1.descrever





