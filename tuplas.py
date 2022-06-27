""" Las tuplas son listas inmutables, es  decir, no se pueden modificar después de su creación.
No permite añadir,eliminar,mover elementos etc
Permite estraer porciones, pero el resultado de la extracción es una tupla nueva.
No permiten busqueda (index)
Si permiten comprobar si un elemento se encuentra en la tupla
   La ventaja en cuanto a las Listas
Mas rapidas
Menos espacio
Formatean Srings
Pueden utilizarse como claves en un diccionario """

#Sintaxis: nombreTupla=(elem1,elem2,elem3...)
from typing import List


miTupla=("Juan",13,1,1995)
print(miTupla[2])
#Convertir una tupla en una lista
miLista= list(miTupla)
print(miLista[:])
#convertir una lista en tupla
miLista2=["Romina","Sergio","Pedro"]
miTupla2=tuple(miLista2)
print(miTupla2)
#Para saber si un elemento se encuentra dentro de la tupla
print("Juan" in miTupla)
#Cuantos veces se encuentra el elemento dentro de la tupla
print(miTupla.count(13))
#Saber la longitud de una tupla
print(len(miTupla))
#Tuplas unitarias
miTupla3=("Juan", )