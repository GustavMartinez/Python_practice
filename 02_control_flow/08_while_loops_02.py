# while loop executes some code WHILE some condition remains true

edad = int(input("Esbribe tu edad: "))

while edad < 0:
    print("Tu edad no puede ser negativa")
    edad = int(input("Esbribe tu edad: "))


print(f"Tu tienes {edad} años!")