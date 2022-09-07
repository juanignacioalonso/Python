"""
Clase: Modelo donde se redactan las características comunes de un grupo de objetos
Instancia de clase o objeto de clase: ejemplar perteneciente a una clase
Modularización: cuando un programa se forma por varias clases, cada clase funciona de forma independiente y permite ser reutilizadas
es mas facil encontrar los errores, el programa sigue funcionando si una clase tiene errores
Encapsulación: el funcionamiento interno de una clase no tiene relacion con el funcionamiento interno de otra clase  
Metodos: comportamiento de la clase, no son los atributos. Es una función especial que pertenece a la clace donde se esta armando
Constructor: es un metodo especial que le da estado inicial a los objetos que pertenezcan a una clase
Encapsulación: proteger una propiedad o metodo para que no se pueda modificar desde fuera de la clase
Herencia sirve para la reutilización de codigo
"""
# Esta clase tiene dos Comportamientos y 4 propiedades  
class Coche():
    #Constructor
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4#Encapsulamos el atributo para no poder ser usada sesde fuera de la clase
        self.__enmarcha=False
    #Self hace referencia al propio objeto pertneciente a la clase o instancia en otras clases es el this, en python si o si hay q ponel self
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.__chequeoInterno()
        if(self.__enmarcha and chequeo):  
            return "El auto esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo no podemos arrancar"
        else:
            return "El auto esta parado"
        
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis,"cm  y un largo de" , self.__largoChasis, "cm")

    def __chequeoInterno(self):#Encapsulamiento del metodo
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puerta="cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puerta=="cerradas"):
            return True
        else:
            return False


#Primera instancia de clase (Objeto)
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("Creamos el segundo objeto")
#Segunda instancia de clase (Objeto)
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche.estado()

