# while loop executes some code WHILE some condition remains true

nombre = input("Escribe tu nombre: ")

while nombre == "":
    print("No escribiste tu nombre, hazlo de nuevo")
    nombre = input("Escribe tu nombre: ")

print(f"Hola, {nombre}")