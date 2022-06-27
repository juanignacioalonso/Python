""" Estructura de datos que nos permite anlmacenar valores de diferentes tipo (enteros,cadenas de texto,decimales)
e incluso listas y diccionarios.

La principal caraccteristica de los disccionarios es que los datos se almacenan asosciados a una clave de tal forma
que se crea una asociacion de tipo clave:valor para cada elemento almacenado

Los elementos almacenados no están ordenados. El orden es indíferente a la hora de almacenar la información en un diccio
nario  """

miDiccionario={"Argentina":"Buenos Aires","Alemania":"Berlin","Francia":"Paris","España":"Madrid"}
#Agregar valores
miDiccionario["Italia"]="Lisboa"
#Modificar valores
miDiccionario["Italia"]="Roma"
#Eliminar elementos
del miDiccionario["Francia"]
#Los diccionarios pueden ser mixtos
miDiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
#Con Tuplas
miTupla=["España","Francia","Reino Unido "]
miDiccionario3={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres"}
miDiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
#print(miDiccionario["Francia"])
print(miDiccionario)
print(miDiccionario2)
print(miDiccionario3)
print(miDiccionario4["anillos"]) 