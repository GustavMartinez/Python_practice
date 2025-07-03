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


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print( f'Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')


#roberto = Empleado("Roberto", 43, "argentino")
#pablo = Persona("Pablo", 52, "chileno")
#ricardo = Empleado("ricardo", 43, "espanol", 'programador', 15000)

#print(ricardo.edad)
#print(ricardo.nacionalidad)
#ricardo.hablar()


# con las nuevas clases:

roberto = EmpleadoArtista("Roberto", 43, "argentino", "cantar", "Google", 15000)

roberto.presentarse()