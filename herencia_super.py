#Principio de sustitución "es siempre un/a" UN EMPLEADO ES SIEMPRE UNA PERSONA al reves no se da UNA PERSONA NO SIEMPRE ES UN EMPLEADO 

class Persona():
    def __init__(self,nombre,edad,lugarRecidencia):
        self.nombre=nombre
        self.edad=edad
        self.lugarRecidencia=lugarRecidencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ",self.edad,"Lugar de Recidencia: ",self.lugarRecidencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,recidencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,recidencia_empleado)#Ejecuta el metodo init de la clase padre
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()#Ejecuta el metodo init de la clase padre
        print("Su salario es: ",self.salario," Su antiguedad es de: ",self.antiguedad, " años")
Sr=Empleado(1500,15,"Manuel",25,"Colombia")
Sr.descripcion()
#Función para saber si un objeto es instancia de una clase determinada 
#Leva dos argumentos primero el nombre de la instancia y luego la clase a la que queremos comprobar si pertenece
print(isinstance(Sr,Persona))