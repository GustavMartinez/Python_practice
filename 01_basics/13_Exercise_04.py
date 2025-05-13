"""
EXERCISE:

validate user input exercise

1. username is no more than 15 characters
2. username must not contain spaces
3. username must not contain digits



"""

username = input("Ingresa tu username, menos de 15 caracteres, sin espacios y sin números: ")

spaces = username.find(" ")
has_number = username.isnumeric()
has_letter = username.isalpha()

if len(username) >= 15:
    
    print("Nombre de usuario mayor a 15 caracteres. Error!")
else:
    if spaces != -1:
        print("Nombre de usuario con espacios. Error!")
    
    else:
        if has_number or not has_letter:
            print("Nombre de usuario con número. Error!")
        else:
            print("Usuario correcto!")