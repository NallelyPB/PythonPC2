''' Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
 pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
 materias.'''


lista_alumnos=[]
N=int(input('¿Cuanto alumnos desea ingresar?: '))
for _ in range(N):
    alum = input('Ingrese el nombre del alumno: ')
    notas=[]
    for i in range(1,4):
        nota = float(input(f'Ingrese la {i} nota del estudiante: '))
        notas.append(nota)
    alumno={
        'Alumno': alum,
        'Nota': notas
    }
    lista_alumnos.append(alumno)

for alumno in lista_alumnos:
      print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Nota']}")