print("Programa de valoracion de notas")
notaAlumno=(input("Introduce la nota del alumno "))

def evaluacion(nota):
    valoracion="Aprobado"
    if nota < 5:
        valoracion="Desaprobado"
    return valoracion

print (evaluacion(float(notaAlumno)))
































