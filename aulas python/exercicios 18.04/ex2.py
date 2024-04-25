# 2. Classe Figura Geométrica e Círculo:
# Crie uma classe abstrata FiguraGeometrica com os 
# métodos calcular_area() e descrever().
# Crie uma classe Circulo que herde de FiguraGeometrica.
# Implemente o método calcular_area() na classe Circulo para calcular a 
# área do círculo.
# Crie um objeto circulo1 e chame os 
# métodos calcular_area() e descrever().

class FiguraGeometrica:  #classe abstrata
    def calcular_area(self):
        raise NotImplementedError
    
    def descrever(self):
        raise NotImplementedError
        
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.1415 * self.raio * self.raio
    
    def descrever(self):
        print(f"area do circula é:{self.calcular_area()}")    
        
circulo1 = Circulo(3.1413)   
circulo1.descrever()
            
    

    
             