print("Programa de valoracion de notas")
notaAlumno=float(input())

def evaluacion(nota):
    valoracion="Aprobado"
    if nota < 5:
        valoracion="Desaprobado"
    return valoracion

print (evaluacion(notaAlumno))
































