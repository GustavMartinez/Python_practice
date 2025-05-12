"""
EXERCISE:

validate user input exercise

1. username is no more than 15 characters
2. username must not contain spaces
3. username must not contain digits



"""

username = input("Ingresa tu username, menos de 15 caracteres, sin espacios y sin números")

if len(username) >= 15:
    print("Nombre de usuario mayor a 15 caracteres")
else:
    print(f"Tu nombre de usuario es {username}")