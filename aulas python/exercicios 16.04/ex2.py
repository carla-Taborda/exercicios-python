# 2. Produto
# Crie uma classe Produto com os atributos:
# nome: nome do produto
# preco: preço do produto
# Implemente os métodos getters e setters para:
# nome
# preco
# Crie um objeto da classe Produto e realize as seguintes operações:
# Acesse e imprima o nome do produto.
# Altere o nome do produto.
# Acesse e imprima o preço do produto.
# Aplique um desconto no preço do produto.
# Acesse e imprima o novo preço do produto.

class Produto:
    def __init__(self, vestido, valor): #atributos
        self.vestido = vestido
        self.valor = valor
    
    def escrever(self):
        print(f" O produto é {self.vestido}") #método
    
    def descrever(self):    
        print(f" O valor é {self. valor}")   #método
    
    def get_vestido(self):
        return self.vestido
        
    def get_valor(self):
        return self.valor    
    
    def set_vestido(self, novo_vestido):
        self.vestido = novo_vestido
        
    def set_valor(self, novo_valor):
        self.valor = novo_valor
        print(f"o valor atual é {self.valor}")
    
    
produto1 = Produto ("vestido", 100)

print(f"o Valor é:{produto1.get_valor()}") 

produto1.set_vestido("vestido 2")
produto1.set_valor(12000)
print(f"{produto1.get_vestido()} o valor atual é: {produto1.get_valor()}")  # saldo após alteração
        
        