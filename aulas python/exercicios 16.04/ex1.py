# 1. Conta Bancária
# Crie uma classe conta bancaria com os atributos:
# titular: nome do titular da conta
# saldo: saldo da conta
# Implemente os métodos getters e setters para:
# titular
# saldo
# Crie um objeto da classe ContaBancaria e realize as seguintes operações:
# Acesse e imprima o nome do titular da conta.
# Altere o nome do titular da conta.
# Acesse e imprima o saldo da conta.
# Deposite um valor na conta.
# Acesse e imprima o novo saldo da conta.


class ContaBancaria:
    def _init_(self, titularConta, saldoConta): #atributos
        self.titularConta = titularConta
        self.saldoConta = saldoConta
    
    def escrever(self):
        print(f"Nome do titular é {self.titularConta}") #método
    
    def descrever(self):    
        print(f"Seu saldo é {self.saldoConta}")   #método
        
    def get_titularConta(self):
        return self.titularConta
        
    def get_saldoConta(self):
        return self.saldoConta
    
    def set_titularConta(self, novo_titular):
        self.titularConta = novo_titular
        
    def set_saldoConta(self, novo_saldoConta):
        self.saldoConta = novo_saldoConta
        print(f"saldo atual é {self, novo_saldoConta}")

contaBancaria1 = ContaBancaria ("saldo")

print(f"Seu saldo é:{contaBancaria1.get_saldoConta()}") # saldo atual

contaBancaria1.set_titularConta("saldo")

print(f"Seu saldo atual é: {contaBancaria1.get_saldoConta()}")  # saldo após alteração
        
        

        
