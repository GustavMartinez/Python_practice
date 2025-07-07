# Hacer loop en dos listas al mismo tiempo

animales = ["gato", "perro", "loro"]
numeros = ["12", "15", "18"]


for animal, numero in zip(animales, numeros):
    print(f"Recorriendo la lista animales: {animal}")
    print(f"Recorriendo la lista numeros: {numero}")