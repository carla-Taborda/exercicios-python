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
        
    def comer(self):
        print(f"O {self.__class__.__name__} está comendo.")
    
    def dormir(self):
        print(f"O {self.__class__.__name__}  está dormindo.")

class Cachorro(Animal):

    def latir(self):
        print(f"{self.__class__.__name__} Au au!")
        
class Gato(Animal):

    def miar(self):
        print(f"{self.__class__.__name__} Miau!")
class Papagaio(Animal):

    def falar(self):
        print(f"{self.__class__.__name__} Ohh, quero bis, kkkkkkk")
        
animais_do_zoo = [Cachorro(), Gato(), Papagaio()]

# Fazendo os animais comerem, dormirem e realizarem ações específicas
for i in animais_do_zoo:
  i.comer()
  i.dormir()

  if isinstance(i, Cachorro):
    i.latir()
  elif isinstance(i, Gato):
    i.miar()
  elif isinstance(i, Papagaio):
    i.falar()