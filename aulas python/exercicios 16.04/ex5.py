# 5. Ponto Geográfico
# Crie uma classe PontoGeografico com os atributos:
# latitude: latitude do ponto
# longitude: longitude do ponto
# Implemente os métodos getters e setters para:
# latitude
# longitude
# Crie um objeto da classe PontoGeografico e realize as seguintes operações:
# Acesse e imprima a latitude do ponto.
# Altere a latitude do ponto.
# Acesse e imprima a longitude do ponto.
# Altere a longitude do ponto.



class PontoGeografico:
    
    def __init__(self, latitude, longitude): #atributos
        self.latitude = latitude
        self.longitude = longitude
        
    def get_latitude(self):
        return self.latitude
        
    def get_longitude(self):
        return self.longitude
    
    def set_latitude(self, nova_latitude):
        self.latitude = nova_latitude
        
    def set_longitude(self, nova_longitude):
        self.longitude = nova_longitude
        
PontoGeografico1 = PontoGeografico( latitude =  "-30.03283000" ,  longitude =  "-51.23019000" )        
print(PontoGeografico1.get_latitude())

PontoGeografico1.set_latitude("-30.05678000")
print(PontoGeografico1.get_latitude())

PontoGeografico1.set_longitude("-51.012345000")
print(PontoGeografico1.get_longitude())




#print(Carro1.get_marca())  

#Carro1.set_marca("Dogde")
#print(Carro1.get_marca())

#Carro1.set_modelo("Dakota")
#print(Carro1.get_modelo())


        