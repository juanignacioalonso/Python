"""for i in range(5,10):
    print(f'Valor de la variable {i}')

for i in range(5,50,3): # dene empezar en el 5 debe ir hasta el 50 y debe ir de 3 en tres
    print(f'Valor de la variable {i}')"""

#Len nos pasa la longitud de un string

valido=False
email=input("Coloque su email ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True 

if valido:
    print("El mail es verdadero")
else:
    print("El email es incorrecto")
