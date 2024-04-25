# 3. Aluno
# Crie uma classe Aluno com os atributos:
# matricula: número da matrícula
# nome: nome do aluno
# curso: nome do curso
# Implemente os métodos getters e setters para:
# matricula
# nome
# curso
# Crie um objeto da classe Aluno e realize as seguintes operações:
# Acesse e imprima o número da matrícula do aluno.
# Altere o número da matrícula do aluno.
# Acesse e imprima o nome do aluno.
# Altere o nome do aluno.
# Acesse e imprima o nome do curso do aluno.
# Altere o nome do curso do aluno.

class Aluno:
    def __init__(self, numeroMatricula, nomeAluno, curso): #atributos
        self.numeroMatricula = numeroMatricula
        self.nomeAluno = nomeAluno
        self.curso = curso 
        
    def get_numero_matricula(self):
        return self.numeroMatricula
                
    def get_nomeAluno(self):
        return self.nomeAluno

    def get_curso(self):
        return self.curso
        

    def set_numero_matricula(self, novo_numeroMatricula):
        self.numeroMatricula = novo_numeroMatricula
            
    def set_nomeAluno(self, novo_nomeAluno):
        self.nomeAluno = novo_nomeAluno

    def set_curso(self, novo_curso):
        self.curso = novo_curso
     
       
aluno1 = Aluno(numeroMatricula = 456789, nomeAluno= "Clara", curso = "Programação" )
print("numeroMatrícula:", aluno1.get_numero_matricula())

aluno1.set_numero_matricula(456789)
print("numeroMatricula:", aluno1.get_numero_matricula())

aluno1.set_nomeAluno("Clara")
print("curso", aluno1.get_curso())

aluno1.set_curso("Desenvolvimento de software")
print("Novo Curso:", aluno1.get_curso())


       
       
# aluno1 = Aluno(numeroMatricula = 456789, nomeAluno= "Clara", curso = "Programação" )
# print("numeroMatrícula:", aluno1.get_numero_matricula())

# aluno1.set_numero_matricula(456789)
# print("numeroMatricula:", aluno1.get_numero_matricula())

# aluno1.set_nomeAluno("Clara")
# print("curso", aluno1.get_curso())

# aluno1.set_curso("Desenvolvimento")
# print("Novo Curso:", aluno1.get_curso())