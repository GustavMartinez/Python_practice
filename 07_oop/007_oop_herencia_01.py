class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def hablar(self):
        print("Hola, estoy hablando mucho")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


#roberto = Empleado("Roberto", 43, "argentino")
pablo = Persona("Pablo", 52, "chileno")
ricardo = Empleado("ricardo", 43, "espanol", 'programador', 15000)

print(ricardo.edad)
print(ricardo.nacionalidad)
ricardo.hablar()