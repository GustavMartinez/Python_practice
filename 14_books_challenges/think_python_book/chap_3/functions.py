def phone():
    telefone = input("Ingresa tu numero de telefono: ")
    return telefone


def contact():
    name = input('Your name is: ')
    print(f"Welcome, {name}")
    telefono = phone()
    print(f"Tu telefono es {telefono}")



def first_line():
    print("+","-","-","-","-","+","-","-","-","-","+")


def second_line():
    print("|"," "," "," "," ","|"," "," "," "," ","|")


def pattern():
    first_line()
    second_line()
    second_line()
    second_line()
    second_line()

pattern()
pattern()
pattern()
first_line()