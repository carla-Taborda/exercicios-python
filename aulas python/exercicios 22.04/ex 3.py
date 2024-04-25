# 3: Funcionários em uma Empresa
# Crie as classes:
# Funcionario (classe base com atributos nome e salario).
# Gerente (herda de Funcionario, com bônus e método adicionar_funcionario()).
# Vendedor (herda de Funcionario, com comissão e 
# método calcular_comissao()).
# Crie uma lista de funcionários:
# Inclua objetos de Gerente e Vendedor.
# Mostre:
# O nome e o salário de cada funcionário.
# O bônus do gerente (se houver).
# A comissão do vendedor (se houver).
# Adicione um funcionário:
# Utilize o método adicionar_funcionario() do gerente para incluir um novo 
# funcionário na lista.

class Funcionario:
  

  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def mostrar_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Salário: R$ {self.salario:.2f}")

class Gerente(Funcionario):
 

  def __init__(self, nome, salario, bonus):
    super().__init__(nome, salario)
    self.bonus = bonus
    self.funcionarios = []

  def adicionar_funcionario(self, funcionario):
    self.funcionarios.append(funcionario)

  def mostrar_dados(self):
    super().mostrar_dados()
    print(f"Bônus: R$ {self.bonus:.2f}")

class Vendedor(Funcionario):
  

  def __init__(self, nome, salario, comissao):
    super().__init__(nome, salario)
    self.comissao = comissao
    self.vendas = 0

  def calcular_comissao(self):
    return self.vendas * (self.comissao / 100)

  def mostrar_dados(self):
    super().mostrar_dados()
    print(f"Comissão: R$ {self.calcular_comissao():.2f}")

funcionarios = [] # Criação da lista de funcionários

gerente1 = Gerente("Camila Bueno", 5000.0, 500.0)# Criação de objetos de Gerente e Vendedor
vendedor1 = Vendedor("Joel Oliveira", 2500.0, 5.0)
vendedor2 = Vendedor("Catarina", 2000.0, 7.0)

funcionarios.append(vendedor1) # Adição de vendedores à lista de funcionários
funcionarios.append(vendedor2)

gerente1.adicionar_funcionario(vendedor1) # Adição de vendedores à lista de funcionários gerenciados pelo gerente
gerente1.adicionar_funcionario(vendedor2)

print("\nFuncionários:") # Apresentação dos dados dos funcionários
for funcionario in funcionarios:
  funcionario.mostrar_dados()

print("\nDados do Gerente:")
gerente1.mostrar_dados()

        

    
    
