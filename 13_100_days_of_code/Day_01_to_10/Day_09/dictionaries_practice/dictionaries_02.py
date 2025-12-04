"""

Imprime el precio de la banana.

Agrega un nuevo producto con su precio.

Actualiza el precio de la naranja.

Elimina la clave "manzana" del diccionario.

Imprime todas las claves del diccionario.

Imprime todos los valores del diccionario.

Imprime el diccionario final.

"""



precios = {
    "manzana" : 3.5,
    "banana" : 2.0,
    "naranja" : 4.2,
}

# tarea 1:
print(precios["banana"])

# tarea 2:
precios["mango"] = 3.1

# tarea 3:
precios["naranja"] = 1.5

# tarea 4:
del precios["manzana"]

# tarea 5:
for k in precios.keys():
    print(k)

# tarea 6:
for v in precios.values():
    print(v)

# tarea 7:
print(precios)
