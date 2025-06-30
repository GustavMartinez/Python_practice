class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def greet(self):
        print(f"Hello!, my name is {self.name}, and I am {self.age} years old")


primera_persona = Person("gustavo", 25)
primera_persona.greet()

segunda_persona = Person("Maria", 50)
segunda_persona.greet()
