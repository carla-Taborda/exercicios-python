# 2: Figuras Geométricas
# Crie as classes:
# Forma (classe base com método calcular_area() abstrato).
# Quadrado (herda de Forma, implementa calcular_area()).
# Retângulo (herda de Forma, implementa calcular_area()).
# Círculo (herda de Forma, implementa calcular_area()).
# Crie uma lista de formas:
# Inclua objetos de Quadrado, Retângulo e Círculo.
# Calcule e mostre:
# A área de cada forma.

from abc import ABC, abstractmethod

class forma(ABC):
    def calcular_area(self):
        pass

        
    def abstrato(self):
        pass

class quadrado(forma):
    def calcular_area(self):
        return super().calcular_area()

class retangulo(forma):
    def calcular_area(self):
        return super().calcular_area()

class circulo(forma):
    def calcular_area(self):
        return super().calcular_area()

formas_geometricas = [quadrado(), retangulo(), circulo()]

for forma in formas_geometricas:
    print()




