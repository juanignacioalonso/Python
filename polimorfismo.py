"""
Polimorfismo: en programacion es cuando un objeto puede cambiar de forma dependiendo del contexto en el que se utilice, por lo tanto tambien 
cambia de comportamiento es facil de utilizar ya que python es un lenguaje de programación de tipado dinamico es decir no necesitamos
especificar deque tipo es un objeto a ola hora de utilizarlo

"""


class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

"""
Sin polimorfismo

miVehiculo=Moto()
miVehiculo2=Coche()
miVehiculo3=Camion()

miVehiculo.desplazamiento()
miVehiculo2.desplazamiento()
miVehiculo3.desplazamiento()

"""
#Con polimorfismo
def desplazamientoVehiculo(vehiculo):#En esta parte se produce el polimorfismo, no especificamos de que tipo es el objeto
    vehiculo.desplazamiento()

miVehiculo=Moto()
desplazamientoVehiculo(miVehiculo)
