class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    
    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")


    def cortar(self):
        print(f"Cortaste la llamada desde tu {self.modelo}")


# instanciar la clase (crear un objeto)
celular_1 = Celular("Samsung", "S23", "48MP")


# Accesar propiedades y métodos
print(celular_1.marca)
celular_1.llamar()