#Captura de varias excepciones

def divide():
    try:
        op1=(float(input("Introduce el primer numero ")))
        op2=(float(input("Introduce el segundo numero ")))

        print("La división es: "+ str(op1/op2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        print("Calculo finalizado")

#Lo que este dentro del finally se ejecuta si o si, con error o sin error
"""
def divide():
    try:
        op1=(float(input("Introduce el primer numero ")))
        op2=(float(input("Introduce el segundo numero ")))

        print("La división es: "+ str(op1/op2))
    except:
        print("Ha ocurrido un error")
    print("Calculo finalizado")
"""
divide()