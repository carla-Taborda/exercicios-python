# 1. Classe Pessoa e Aluno:
# Crie uma classe Pessoa com os atributos nome, idade e sexo.
# Crie uma classe Aluno que herde da classe Pessoa.
# Adicione à classe Aluno o atributo matricula.
# Implemente métodos get_matricula(), set_matricula(), apresentar() nas 
# classes Pessoa e Aluno.
# Crie objetos pessoa1 e aluno1 e chame os métodos adequados.

class Pessoa:

    def __init__(self, nome, idade, sexo): #atributos
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def apresentar(self):
        print(f"meu nome é: {self.nome}, tenho {self.idade} anos, sou {self.sexo}")
        
class Aluno(Pessoa):
    
    def __init__(self, nome, idade, sexo, matricula):
        super().__init__(nome, idade, sexo)
        self.matricula = matricula
        
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula
    
    def apresentar(self):
        super().apresentar()
        print(f"minha matricula é: {self.matricula}")
        
        
pessoa1 = Pessoa("carla", 40, "f")         
pessoa1.apresentar()  

    
aluno1 = Aluno("carla", 40, "f", 456789)
aluno1.apresentar()
print(aluno1.get_matricula())
aluno1.set_matricula(123456)
print(aluno1.get_matricula())
    
   