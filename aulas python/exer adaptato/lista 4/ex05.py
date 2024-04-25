# Classe JogoEletronico
class JogoEletronico:
    def __init__(self, nome, genero, plataforma, classificacao_indicativa, preco):
        self.__nome = nome
        self.__genero = genero
        self.__plataforma = plataforma
        self.__classificacao_indicativa = classificacao_indicativa
        self.__preco = preco
        self.__desconto_aplicado = False

    def aplicar_desconto(self, percentual):
        if not self.__desconto_aplicado:
            self.__preco *= (1 - percentual / 100)
            self.__desconto_aplicado = True

    def calcular_valor_total(self):
        if self.__desconto_aplicado:
            return self.__preco
        else:
            return "Desconto não aplicado."

    def mostrar_informacoes(self):
        print("Informações do Jogo:")
        print("Nome:", self.__nome)
        print("Gênero:", self.__genero)
        print("Plataforma:", self.__plataforma)
        print("Classificação Indicativa:", self.__classificacao_indicativa)
        print("Preço:", self.__preco)
        print("Desconto Aplicado:", "Sim" if self.__desconto_aplicado else "Não")

jogo1 = JogoEletronico("The Witcher 3", "RPG", "PlayStation 4", "18+", 150)
jogo1.mostrar_informacoes()
jogo1.aplicar_desconto(20)
print("Valor Total:", jogo1.calcular_valor_total())