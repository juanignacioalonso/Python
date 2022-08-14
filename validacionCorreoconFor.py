"""email=False
miEmail=input("Ingrese su dirección de correo: ")

for i in miEmail:
    if(i=="@" ):
        email=True

if(email==True): #si ponemos email solo tambien lo toma como verdadero
    print("El email es correcto")
else:
    print("el email es incorrecto")"""


contador=0
miEmail=input("Ingrese su dirección de correo: ")

for i in miEmail:
    if(i=="@" or i=="." ):
        contador=contador+1

if(contador>=2): #si ponemos email solo tambien lo toma como verdadero
    print("El email es correcto")
else:
    print("el email es incorrecto")