class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca,"\nModelo: ", self.modelo,"\nEnmarcha: ",self.enmarcha,"\nAcelera: ",self.acelera,"\nFrena: ",self.frena)

#Herencia
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hwilly=""
    def willy(self):
        self.hwilly="Voy haciendo un willy"
    

    def estado(self):
        print("Marca: ", self.marca,"\nModelo: ", self.modelo,"\nEnmarcha: ",self.enmarcha,"\nAcelera: ",self.acelera,"\nFrena: ",self.frena,"\n", self.hwilly)

class VElectricos(Vehiculos):
    
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True



