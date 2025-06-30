class Car:
    def __init__(self, nombre, marca, ano):
        self.nombre_de_carro = nombre
        self.marca_de_carro = marca
        self.ano_fabricacion = ano


mi_carro = Car("roadster", "bmw", "2009")


print(mi_carro.ano_fabricacion)