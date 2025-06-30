class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def greet(self):
        print(f"Hello!, my name is {self.name}, and I am {self.age} years old")


mi_persona = Person("gustavo", 25)


mi_persona.greet()