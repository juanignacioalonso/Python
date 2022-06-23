#Conjunto de líneas de código agrupadas(bloque de código) que funcionan como una unidad realizando una tarea específica.
#Las funciones pueden devolver valores.
#Pueden tener parametros o argumentos.
#Tambien se denominan "métodos" cuando se encuentran definidas dentro de una clase.

#Utilidad
#Reutilizar codigo.

#Sintaxis
#def nombre_funcion():
    #instrucciones de la funcion
    #return # esto es opcional

#def nombre_funcion_parametros(parametros):
    #instrucciones de la funcion
    #return #esto es opcional

#Ejecución
#nombre_funcion()
#nombre_funcion_parametros("parametro")

#Tenemos funciones predefinidas, que son las de python y propias que son las que creamos
#print("Estamos aprendiendo python")

#def imprime():
    #print("Estamos aprendiendo python")
    
#La función no hace nada si no la llamamos
#imprime()

"""def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()"""
#FUNCIÓN CON PARAMETROS
"""def suma(num1,num2):
    print(num1+num2)

suma(2,2)

suma(4,5)"""

#Funcion utilizando return
def suma(num1,num2):
    resultado=num1+num2
    return resultado

print(suma(56,69)) 

