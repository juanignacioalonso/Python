#Continue
"""for letra in "Python":
    if letra == "h":
        continue # Ignora la linea que imprime la h
    print("Viendo la letra: "+ letra)"""
#UN EJEMPLO DE USO ES CONTAR SOLO LETRAS Y NO ESPACIOS
"""nombre="Pildoras informatigas"
contador=0
for i in nombre:
    if i == " ":
        continue
    contador+=1
print(contador)"""
#Pass
"""class Miclase:
    pass #Para ejecutar mas tarde"""
#Else en bucle
email=input("INTRODUCE TU EMAIL")

for i in email:
    if i =="@":
        arroba=True
        break;

else:# se ejecuta cuando el bucle este vacio
    arroba=False
print(arroba)
