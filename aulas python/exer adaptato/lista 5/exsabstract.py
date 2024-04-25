from abc import ABC, abstractmethod

# Classe abstrata FiguraGeometrica
class FiguraGeometrica(ABC):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @abstractmethod
    def calcular_area(self):
        pass

# Subclasses de FiguraGeometrica
class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)  # A altura é igual à base para um quadrado

    def calcular_area(self):
        return self.base * self.base

class Retangulo(FiguraGeometrica):
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Classe abstrata ContaBancaria
class ContaBancaria(ABC):
    def __init__(self, titular, saldo, taxa_juros):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def calcular_juros(self):
        pass

# Subclasses de ContaBancaria
class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def calcular_juros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)

class ContaPoupanca(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def calcular_juros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)

class ContaInvestimento(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def calcular_juros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)

# Classe abstrata Veiculo
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

# Subclasses de Veiculo
class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado")

    def desligar(self):
        print("Carro desligado")

    def acelerar(self):
        print("Carro acelerando")

    def frear(self):
        print("Carro freando")

class Moto(Veiculo):
    def ligar(self):
        print("Moto ligada")

    def desligar(self):
        print("Moto desligada")

    def acelerar(self):
        print("Moto acelerando")

    def frear(self):
        print("Moto freando")

class Caminhao(Veiculo):
    def ligar(self):
        print("Caminhão ligado")

    def desligar(self):
        print("Caminhão desligado")

    def acelerar(self):
        print("Caminhão acelerando")

    def frear(self):
        print("Caminhão freando")

# Classe abstrata Funcionario
class Funcionario(ABC):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    @abstractmethod
    def calcular_pagamento(self):
        pass

    @abstractmethod
    def tirar_ferias(self):
        pass

# Subclasses de Funcionario
class CLT(Funcionario):
    def calcular_pagamento(self):
        return self.salario

    def tirar_ferias(self):
        print("Funcionário CLT tirando férias")

class PJ(Funcionario):
    def calcular_pagamento(self):
        return self.salario

    def tirar_ferias(self):
        print("Funcionário PJ não tem férias")

class Freelancer(Funcionario):
    def calcular_pagamento(self):
        return self.salario

    def tirar_ferias(self):
        print("Freelancer não tem férias")

# Classe abstrata Jogo
class Jogo(ABC):
    def __init__(self, nome, genero, plataforma, classificacao_indicativa):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.classificacao_indicativa = classificacao_indicativa

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def pausar(self):
        pass

    @abstractmethod
    def salvar_jogo(self):
        pass

    @abstractmethod
    def carregar_jogo(self):
        pass

# Subclasses de Jogo
class RPG(Jogo):
    def iniciar(self):
        print("Iniciando jogo de RPG")

    def pausar(self):
        print("Jogo de RPG pausado")

    def salvar_jogo(self):
        print("Jogo de RPG salvo")

    def carregar_jogo(self):
        print("Jogo de RPG carregado")

class Aventura(Jogo):
    def iniciar(self):
        print("Iniciando jogo de aventura")

    def pausar(self):
        print("Jogo de aventura pausado")

    def salvar_jogo(self):
        print("Jogo de aventura salvo")

    def carregar_jogo(self):
        print("Jogo de aventura carregado")

class Estrategia(Jogo):
    def iniciar(self):
        print("Iniciando jogo de estratégia")

    def pausar(self):
        print("Jogo de estratégia pausado")

    def salvar_jogo(self):
        print("Jogo de estratégia salvo")

    def carregar_jogo(self):
        print("Jogo de estratégia carregado")





# Figuras Geométricas
quadrado = Quadrado(5)
print("Área do quadrado:", quadrado.calcular_area())

retangulo = Retangulo(4, 6)
print("Área do retângulo:", retangulo.calcular_area())

triangulo = Triangulo(3, 4)
print("Área do triângulo:", triangulo.calcular_area())

# Contas Bancárias
conta_corrente = ContaCorrente("João", 1000, 1)
conta_corrente.depositar(500)
print("Saldo da conta corrente:", conta_corrente.saldo)
conta_corrente.calcular_juros()
print("Saldo com juros da conta corrente:", conta_corrente.saldo)

conta_poupanca = ContaPoupanca("Maria", 2000, 2)
conta_poupanca.sacar(300)
print("Saldo da conta poupança:", conta_poupanca.saldo)
conta_poupanca.calcular_juros()
print("Saldo com juros da conta poupança:", conta_poupanca.saldo)

# Veículos
carro = Carro("Toyota", "Corolla", 2022, "Prata")
carro.ligar()
carro.acelerar()
carro.frear()
carro.desligar()

moto = Moto("Honda", "CB 500", 2021, "Preto")
moto.ligar()
moto.acelerar()
moto.frear()
moto.desligar()

# Funcionários
funcionario_clt = CLT("Ana", "Desenvolvedor", 5000)
print("Salário do funcionário CLT:", funcionario_clt.calcular_pagamento())
funcionario_clt.tirar_ferias()

funcionario_pj = PJ("Pedro", "Consultor", 7000)
print("Salário do funcionário PJ:", funcionario_pj.calcular_pagamento())
funcionario_pj.tirar_ferias()

freelancer = Freelancer("Lucas", "Designer", 50)
print("Pagamento do freelancer:", freelancer.calcular_pagamento())
freelancer.tirar_ferias()

# Jogos
rpg = RPG("The Elder Scrolls V: Skyrim", "RPG de ação", "PC", "18+")
rpg.iniciar()
rpg.salvar_jogo()
rpg.pausar()
rpg.carregar_jogo()

aventura = Aventura("The Legend of Zelda: Breath of the Wild", "Aventura", "Nintendo Switch", "10+")
aventura.iniciar()
aventura.salvar_jogo()
aventura.pausar()
aventura.carregar_jogo()