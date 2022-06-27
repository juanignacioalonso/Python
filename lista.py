"""Listas es muy parecido a los array, estructura de datos que mos permite almacenar varios valores, puede almacenar
 diferentes tipos de valores y se puede expandir dinámicamente los ultimos dos items no pasan en otros lenguajes"""

 #Sintaxis: nombreLista=[elem1,elem2,elem3...]
 #Indice: la posición del elemento en la lista, pero no es lo mismo que la posición por ejemplo el primer elemento es 0


milista2=["Sandra","Lautaro"]*3
milista=["Maria","Juan",5,"Romina"]
#milista.append("Sara")#Este metodo agrega el elemento al final de la lista
#milista.insert(2,"Pedro")#Para cuando no queremos agregar al final
#milista.extend(["Nicolas","Alicia","Clara"])#Para agregar más de un elemento
#milista.remove(5)#Para eliminar un elemento
#milista.pop()#Elimina el ultimo elemento de la lista
milista3=milista+milista2 # Unir dos listas
#Para mostrar todos loos elementos
print(milista[:])
#Para mostrar un elemento
print(milista[1])
#Si ponemos indices negativos python empieza a contar desde el final
print(milista[-2])
#Para mostrar una porcion de la lista
print(milista[0:3])
print(milista[:2])#de forma abreviada 
print(milista[2:0])#Accede desde el elemento que le indicamos hasta el final
print(milista.index("Juan"))#Para mostrar en que indice esta el elemento
print("Pepe" in milista)#Para saber si un elemento se encuentra en mi lista
print(milista3)
print(milista2)