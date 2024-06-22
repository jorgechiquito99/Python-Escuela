print("programa de evaluacion de notas")

nota_alumno=input("introduce la nota del alumno:  ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspendido"
    return  valoracion
print(evaluacion(int(nota_alumno)))