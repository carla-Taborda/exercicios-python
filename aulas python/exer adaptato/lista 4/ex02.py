# Classe ProdutoEletronico
class ProdutoEletronico:
    def __init__(self, codigo, nome, marca, modelo, preco, tipo):
        self.__codigo = codigo
        self.__nome = nome
        self.__marca = marca
        self.__modelo = modelo
        self.__preco = preco
        self.__tipo = tipo
        self.__garantia_estendida = False

    def aplicar_garantia_estendida(self):
        if not self.__garantia_estendida:
            self.__preco *= 1.1  # Aumenta o preço em 10% para garantia estendida
            self.__garantia_estendida = True

    def calcular_valor_total(self):
        if self.__garantia_estendida:
            return self.__preco
        else:
            return "Garantia estendida não aplicada."

    def mostrar_informacoes(self):
        print("Informações do Produto:")
        print("Código:", self.__codigo)
        print("Nome:", self.__nome)
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo)
        print("Preço:", self.__preco)
        print("Tipo:", self.__tipo)
        print("Garantia Estendida:", "Sim" if self.__garantia_estendida else "Não")

# Produto Eletrônico
produto1 = ProdutoEletronico("001", "Smartphone", "Samsung", "Galaxy S21", 3000, "Celular")
produto1.mostrar_informacoes()
produto1.aplicar_garantia_estendida()
print("Valor Total:", produto1.calcular_valor_total())