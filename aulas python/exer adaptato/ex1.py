from datetime import datetime

class Voo:
    def __init__(self, codigo, companhia, origem, destino, horario_saida, horario_chegada, preco_passagem):
        self._codigo = codigo
        self._companhia = companhia
        self._origem = origem
        self._destino = destino
        self._horario_saida = horario_saida
        self._horario_chegada = horario_chegada
        self._preco_passagem = preco_passagem

    def calcular_duracao_voo(self):
        hora_saida = datetime.strptime(self._horario_saida, "%H:%M")
        hora_chegada = datetime.strptime(self._horario_chegada, "%H:%M")
        duracao = hora_chegada - hora_saida
        duracao_horas = duracao.total_seconds() / 3600
        return duracao_horas

    def aplicar_desconto(self, percentual_desconto):
        self._preco_passagem *= (1 - percentual_desconto / 100)

    def mostrar_informacoes(self):
        print("Informações do voo:")
        print(f"Código: {self._codigo}")
        print(f"Companhia: {self._companhia}")
        print(f"Origem: {self._origem}")
        print(f"Destino: {self._destino}")
        print(f"Horário de saída: {self._horario_saida}")
        print(f"Horário de chegada: {self._horario_chegada}")
        print(f"Preço da passagem com desconto é: R${self._preco_passagem:.2f}")
        print(f"A duração do voo é: {self.calcular_duracao_voo()} horas ")

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_companhia(self):
        return self._companhia

    def set_companhia(self, companhia):
        self._companhia = companhia

    def get_origem(self):
        return self._origem

    def set_origem(self, origem):
        self._origem = origem

    def get_destino(self):
        return self._destino

    def set_destino(self, destino):
        self._destino = destino

    def get_horario_saida(self):
        return self._horario_saida

    def set_horario_saida(self, horario_saida):
        self._horario_saida = horario_saida

    def get_horario_chegada(self):
        return self._horario_chegada

    def set_horario_chegada(self, horario_chegada):
        self._horario_chegada = horario_chegada

    def get_preco_passagem(self):
        return self._preco_passagem

    def set_preco_passagem(self, preco_passagem):
        self._preco_passagem = preco_passagem

voo = Voo("V123", "AirlineX", "São Paulo", "Nova York", "10:00", "15:00", 1000.00)
voo.aplicar_desconto(10)
voo.mostrar_informacoes()

