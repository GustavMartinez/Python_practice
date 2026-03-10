PATH = "13_100_days_of_code/Day_21_to_30/Day_24/lesson_1/mi_archivo.txt"


## Sobreescribir

def escribir():
    with open(PATH, mode="w") as a:
        a.write("Otro texto") ## Cambiar el texto aqui


## Actualizar un archivo:

def actualizar():
    with open(PATH, mode='a') as file:
        file.write("\nOtra linea") ## Cambiar el texto aqui

#escribir()
actualizar()