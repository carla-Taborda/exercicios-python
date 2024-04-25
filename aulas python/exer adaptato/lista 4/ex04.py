# Classe AgendaTelefonica
class AgendaTelefonica:
    def __init__(self):
        self.__contatos = []

    def adicionar_contato(self, nome, telefone, email):
        self.__contatos.append({"nome": nome, "telefone": telefone, "email": email})

    def buscar_contato(self, chave):
        for contato in self.__contatos:
            if chave in contato.values():
                return contato
        return None

    def remover_contato(self, chave):
        contato = self.buscar_contato(chave)
        if contato:
            self.__contatos.remove(contato)
        else:
            print("Contato não encontrado.")

    def mostrar_contatos(self):
        print("Contatos:")
        for contato in self.__contatos:
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            print("Email:", contato["email"])
            print("--------------------")
agenda = AgendaTelefonica()
agenda.adicionar_contato("João", "123456789", "joao@email.com")
agenda.adicionar_contato("Maria", "987654321", "maria@email.com")
agenda.mostrar_contatos()