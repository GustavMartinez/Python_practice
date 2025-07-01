class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def new_name(self):
        self.name = input("ingresa el nuevo nombre: ")
        print(f"El nuevo nombre es {self.name}")


class Owner:
    def __init__(self, name, phone):
        self.owner_name = name
        self.owner_phone = phone


# Crear objeto Owner
dueno = Owner("gustavo", "33225544")

# Crear objeto Dog
doggy = Dog("bruny", dueno)


# Accesar propiedades del objeto Dog
print(doggy.name)
print(doggy.owner.owner_name)


#Ejecutar metodo del objeto Dog
doggy.new_name()
