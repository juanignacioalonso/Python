"""
Las excepciones son errores que ocurren durante la ejecución del programa. La sintaxis del código es correcta pero durante la 
ejecución ha ocurrido "algo inesperado" 

Este tipo  de errores de ejecución se pueden controlar para que la ejecución del programa continúe. Es lo que se conoce como manejo
o control de excepciones

"""

from pickle import TRUE


def suma(num1, num2):
    	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operación erronea" 	

while True:
	try:
		op1=(int(input("Introduce el primer numero: ")))

		op2=(int(input("Introduce el segundo numero: ")))

		break
	
	except ValueError:
		print("Los Valores introducidos no son correctos, intentalo de nuevo")
	

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")