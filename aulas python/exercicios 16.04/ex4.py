# 4. Carro
# Crie uma classe Carro com os atributos:
# marca: marca do carro
# modelo: modelo do carro
# ano: ano de fabricação do carro
# Implemente os métodos getters e setters para:
# marca
# modelo
# ano
# Crie um objeto da classe Carro e realize as seguintes operações:
# Acesse e imprima a marca do carro.
# Altere a marca do carro.
# Acesse e imprima o modelo do carro.
# Altere o modelo do carro.
# Acesse e imprima o ano de fabricação do carro.
# Altere o ano de fabricação do carro.


class Carro:
    def __init__(self, marca, modelo, ano): #atributos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_ano(self):
        return self.ano
        
    def set_marca(self, nova_marca):
        self.marca = nova_marca
    
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    
    def set_ano(self, novo_ano):
        self.ano = novo_ano   
       
Carro1 = Carro (marca = "Dogde", modelo = "Ram" , ano = "2019" )         
print(Carro1.get_marca())  

Carro1.set_marca("Dogde")
print(Carro1.get_marca())

Carro1.set_modelo("Dakota")
print(Carro1.get_modelo())

Carro1.set_ano("2004")
print(Carro1.get_ano())


      
        
    
        
        
        
#aluno1 = Aluno(numeroMatricula = 456789, nomeAluno= "Clara", curso = "Programação" )
#print("numeroMatrícula:", aluno1.get_numero_matricula())

#aluno1.set_numero_matricula(456789)
#print("numeroMatricula:", aluno1.get_numero_matricula())

#aluno1.set_nomeAluno("Clara")
#print("curso", aluno1.get_curso())

#aluno1.set_curso("Desenvolvimento de software")
#print("Novo Curso:", aluno1.get_curso())

        
