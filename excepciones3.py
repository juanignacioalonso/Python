#Raise nos permite personalizar nuestras excepciones, esta excepcion no se captura en un bloque de try catch por lo que el programa no va a segir
# a no se que  usemos que capturemos la excepción como en el ejemplo siguiente
"""
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("La edad no puede ser menor que cero")
    if edad<20:
        return "Eres muy joven"
    elif edad< 40:
        return "Eres joven"
    elif edad <65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuídate..." 

print(evaluaEdad(85))

"""
import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError ("El número no puede ser negativo ")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un número ")))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
print("Programa tereminado")
