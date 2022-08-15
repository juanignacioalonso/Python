#Bucle indeterminado se ejecutara mientras la condicion sea verdadera
# While significa mientras, por lo tanto mientras se cumpla la condicion  se ejecutara el cuerpo del bucle
"""i=1
while i <=10:
    print("Ejecución"+str(i)) 
    i=i+1 #asi hacemo que temine el bucle, con el contador, que es un incremento de i, cuando supere 10 el programa sale del bucle
print("Termino la ejecución")"""


#Naturaleza indeterminada del bucle While
"""edad=int(input("Introduce la edad: "))

while edad<0 or edad>100:
    print("Edad incorrecta")
    edad=int(input("Introduce la edad: "))

print("Edad aceptada")
print("Edad "+str(edad))"""

#Hacer que un bucle no sea nunca infinito
import math


print("Calculo de Raíz cuadrada")

numero=float(input("Introduce un número "))

intentos=0
while numero<0:
    print("no se puede obtener la raíz de un numero negativo")
    if intentos==2:
        print("Has relizado varios intentos")
        break;# esta instrucción te saca del bucle por mas de que la condicion del bucle se cumpla
    numero=int(input("Introduce un número "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raíz cuadrada de "+str(numero)+" es "+str(solucion)) 


