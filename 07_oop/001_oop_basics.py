# Clase perrito
class Dog:
    def __init__(self, name, breed, age, owner):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_age = age
        self.dog_owner = owner

# Clase dueno
class Owner:
    def __init__(self, name, address, phone):
        self.owner_name = name
        self.owner_address = address
        self.owner_phone = phone
        


# objetos dueno

un_dueno = Owner("gustavo", "candono nonuno", "3535-2121")
otro_dueno = Owner("martinez", "candono siqura", "3535-2121")

# objetos perritos
un_perrito = Dog("bruno", "pincher", 2, un_dueno)
otro_perrito = Dog("teo", "canino", 5, otro_dueno)



# Accesarndo los atributos:

print(un_perrito.dog_name)
print(otro_perrito.dog_age)
print(un_dueno.owner_name)
print(un_perrito.dog_owner.owner_name)