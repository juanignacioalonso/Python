"""
Estructuras que extraen valores de una función y almacenan los objetos iterables (pueden recorrer)
Estos valore se almacenean de uno en uno
Cada ves que un generador almacena su valor, este permanece en un estado pausado hasta que se solicite el siguiente. Esta caracteristica 
es conocida como "Suspencion de estado"
¿Que utilidad tienen?
Son más eficientes que las funciones tradicionales
Muy útiles con listas de valores infinitos
Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno

"""

""" 
# Con una funcion
def generaPares(limite):
    num = 1
    miLista=[]
    while num < limite:
        miLista.append(num*2)
        num=num+1

    return miLista

print(generaPares(20))

"""
"""
# Con un Generador
def generaPares(limite):
    num = 1
    
    while num < limite:
        yield num*2
        num=num+1

devuelvePares=generaPares(10)
#devuelvePares lo convertimos en un objeto iterable

for i in devuelvePares:
    print(i)

"""
#Imprimir los tres primeros elementos
def generaPares(limite):
    num = 1
    
    while num < limite:
        yield num*2
        num=num+1

devuelvePares=generaPares(10)

print(next(devuelvePares))
print("Mas lineas de codigo")
print(next(devuelvePares))
print("Mas lineas de codigo")
print(next(devuelvePares))


