#* delante del argumento en una función le estamos indicando al programa que va a recibir un número indeterminado de elementos y ademas que los argumentos los recibira en forma de tupla
def devuelve_ciudades(*ciudades): 
    for elemento in ciudades:
        #for subelemento in elemento:
            #yield subelemento:
            yield from elemento #no utilizamos bucle anidado

ciudades_devueltas=devuelve_ciudades("Córdoba","Mendoza","Malargue","San Rafael")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))