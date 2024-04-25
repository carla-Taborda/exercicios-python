# 5. Classe Funcionario e Gerente:
# Crie uma classe Funcionario com os 
# atributos nome, cargo, salario e data_admissao.
# Crie uma classe Gerente que herde de Funcionario.
# Adicione à classe Gerente os atributos bonus e area_gerenciada.
# Implemente 
# métodos calcular_pagamento(), bonificar(), promover() e apresentar_dad
# os() nas classes Funcionario e Gerente.
# Crie objetos funcionario1 e gerente1 e chame os métodos adequados.

class Funcionario:
    def __init__(self, nome, cargo, salario, data_admissao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao

    def calcular_pagamento(self):
        return self.salario

    def bonificar(self, bonus):
        self.salario += bonus

    def promover(self, promocao):
        self.cargo = promocao

    def apresentar_dados(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario}, Admissão: {self.data_admissao}")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, data_admissao, bonus, area_gerenciada):
        super().__init__(nome, cargo, salario, data_admissao)
        self.bonus = bonus
        self.area_gerenciada = area_gerenciada

    def calcular_pagamento(self):
        return self.salario + self.bonus

funcionario1 = Funcionario("Clara", "Compras", 7000, "17/02/2011")
gerente1 = Gerente("Catarina", "Gerente", 15000, "01/03/2015", 3000, "Participação Lucros")

print("Funcionário:")
funcionario1.apresentar_dados()
print("\nGerente:")
gerente1.apresentar_dados()
print(f"\nSalário do Funcionário: {funcionario1.calcular_pagamento()}")
print(f"Salário do Gerente: {gerente1.calcular_pagamento()}")
