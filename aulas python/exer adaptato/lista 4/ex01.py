class Voo:
    def __init__(self, codigo, companhia, origem, destino, horario_saida, horario_chegada, preco_passagem):
        self.__codigo = codigo
        self.__companhia = companhia
        self.__origem = origem
        self.__destino = destino
        self.__horario_saida = horario_saida
        self.__horario_chegada = horario_chegada
        self.__preco_passagem = preco_passagem

    def calcular_duracao_voo(self):
        
        horaSaida, minutoSaida = divmod(self.__horario_saida * 100, 100)
        horaChegada, minutoChegada = divmod(self.__horario_chegada * 100, 100)
        
     
        minutoSaidatotal = horaSaida * 60 + minutoSaida
        minutosChegadatotal = horaChegada * 60 + minutoChegada
        
       
        duracaoEmMinutos = minutosChegadatotal - minutoSaidatotal
        
        
        horaDuracao = duracaoEmMinutos // 60
        minutoDuracao = duracaoEmMinutos % 60
        return f"{horaDuracao}h {minutoDuracao}min"

    def aplicarDesconto(self, percentual):
       
        self.__preco_passagem -= self.__preco_passagem * (percentual / 100)

    def mostrar_informacoes(self):
        
        print(f"Código do voo: {self.__codigo} # Companhia: {self.__companhia}")
        print(f"Origem: {self.__origem} # Destino: {self.__destino}")
        print(f"Horário de Saída: {self.__horario_saida}h # Horário de Chegada: {self.__horario_chegada}h")
        print(f"Preço da Passagem já com desconto: R${self.__preco_passagem:.2f}")

voo1 = Voo(89,"Latam", "Brasil", "Europa", 15.20, 07.30, 5000)

print(f"Duração do voo é: {voo1.calcular_duracao_voo()}")
print("######################################################")
voo1.aplicarDesconto(30)
voo1.mostrar_informacoes()