# 1: Animais no Zoológico
# Crie as classes:
# Animal (classe base com métodos comer() e dormir()).
# Cachorro (herda de Animal, com método latir()).
# Gato (herda de Animal, com método miar()).
# Papagaio (herda de Animal, com método falar()).
# Crie uma lista de animais:
# Inclua objetos de Cachorro, Gato e Papagaio.
# Faça os animais:
# Comerem.
# Dormirem.
# Realizarem ações específicas (latir, miar, falar) de acordo com seu tipo.


class Animal:    
    def fazer_barulho(self):
        raise NotImplementedError
    
    def comer(self):
        raise NotImplementedError
    
    def dormir(self):
        raise NotImplementedError

    
class Cachorro(Animal):        
    def fazer_barulho(self):
        print("au au!")
    
    def comer(self):
        print(" O cachoro esta comendo!")
        
    def dormindo(self):
        print(" O cachorro dorme!")
        
class Gato(Animal):
    def fazer_barulho(self):
        print(" miau!")
    
    def comer(self):
        print(" O gato esta comendo!")
        
    def dormindo(self):
        print(" O gato dorme!")
        
class Papagaio(Animal):
    def fazer_barulho(self):
        print(" Inter!")
    
    def comer(self):
        print(" O papagaio esta comendo!")
        
    def dormindo(self):
        print(" O papagaio dorme!")
              
cachorro1 = Cachorro ( "ração castrados", "dormir na rua", "au au")
cachorro1.fazer_barulho()
gato1 = Gato ("whiscas", "dormir no sofa", "miau")
gato1.fazer_barulho()
papagaio1 = Papagaio ("ração", "dormir na gaiola", "inter") 
papagaio1.fazer_barulho()


