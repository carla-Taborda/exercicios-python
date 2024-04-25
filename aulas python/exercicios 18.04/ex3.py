# 3. Classe Conta Bancária e Conta Poupança:
# Crie uma classe ContaBancaria com os 
# atributos titular, saldo e taxa_juros.
# Crie uma classe ContaPoupanca que herde de ContaBancaria.
# Adicione à classe ContaPoupanca o atributo rendimento_mensal.
# Implemente 
# métodos depositar(), sacar(), calcular_rendimento() e apresentar_saldo()
# nas classes ContaBancaria e ContaPoupanca.
# Crie objetos conta1 e conta_poupanca1 e chame os métodos 
# adequados.

class ContaBancaria:
    def __init__(self, titular, saldo = 0, taxa_juros = 1):
        titular = titular
        saldo = saldo
        taxa_juros = taxa_juros
        
    def depositar(self,valor):
        self.saldo +=valor

    def sacar(self,valor):
        self.saldo >=valor
        self.saldo <=valor
    def calcular_rendimento(sef, taxa):     
        calcular_rendimento = self.saldo * (taxa / 100)
        self.saldo += calcular_rendimento
        
    def apresentar_saldo(self):   
        return self.saldo    


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_juros, rendimento_mensal):
        super().__init__(titular, saldo, taxa_juros)
        self.rendimento_mensal = rendimento_mensal
        
    def depositar(self,valor):
        self.saldo +=valor

    def sacar(self,valor):
        self.saldo >=valor
        self.saldo <=valor
        
    def calcular_rendimento(sef, taxa):     
        calcular_rendimento = self.saldo * (taxa / 100)
        self.saldo += calcular_rendimento
        
    def apresentar_saldo(self):   
        return self.saldo    


conta1 = ContaBancaria ("carla", 150000, 0,15, 10)
conta_poupanca1  = ContaPoupanca ("carla", 250000, 0,25, 20)
conta_poupanca1.depositar(2000)
conta_poupanca1.sacar(5000)
conta_poupanca1.apresentar_saldo()
conta_poupanca1.calcular_rendimento()

