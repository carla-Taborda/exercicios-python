# Classe Restaurante
class Restaurante:
    def __init__(self, nome, especialidade, endereco, horario_funcionamento):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__endereco = endereco
        self.__horario_funcionamento = horario_funcionamento
        self.__cardapio = {}

    def adicionar_prato(self, nome_prato, descricao, preco):
        self.__cardapio[nome_prato] = {"descrição": descricao, "preço": preco}

    def remover_prato(self, nome_prato):
        if nome_prato in self.__cardapio:
            del self.__cardapio[nome_prato]
        else:
            print("Prato não encontrado no cardápio.")

    def mostrar_cardapio(self):
        print("Cardápio:")
        for prato, info in self.__cardapio.items():
            print("Nome:", prato)
            print("Descrição:", info["descrição"])
            print("Preço:", info["preço"])
            print("--------------------")

restaurante1 = Restaurante("Restaurante Italiano", "Comida Italiana", "Rua das Pizzas, 123", "Das 11h às 22h")
restaurante1.adicionar_prato("Pizza Margherita", "Molho de tomate, muçarela e manjericão", 40)
restaurante1.adicionar_prato("Spaghetti Carbonara", "Massa italiana com molho carbonara", 35)
restaurante1.mostrar_cardapio()