
"""

Tareas:

Imprime la nota de "programacion".

Agrega una nueva materia con su nota dentro de "cursos".

Cambia la nota de "historia".

Calcula y muestra el promedio de notas del estudiante.

Agrega una nueva clave al diccionario principal llamada "promedio" con el valor calculado.

Imprime el diccionario final.

"""


estudiantes = {
    "nombre" : "Ana",
    "cursos" : {
        "matematicas" : 8.5,
        "historia" : 7.2,
        "programacion" : 9.1
    },
}

# tarea 1
print(estudiantes["cursos"]["programacion"])

# tarea 2
estudiantes["cursos"]["fisica"] = 2.0

# tarea 3
estudiantes["cursos"]["historia"] = 10.0

# tarea 4

sumatoria = 0
materias = 0

for nota in estudiantes["cursos"].values():
    sumatoria += nota
    materias += 1

promedio = sumatoria/materias
print(f"El promedio de las notes es: {promedio}")

# tarea 5
estudiantes["promedio"] = promedio

# tarea 6
print(estudiantes)
