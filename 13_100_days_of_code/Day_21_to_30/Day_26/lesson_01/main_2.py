# Objetivo: Hacer que cada numero aumente en una unidad

numbers = [1,2,3,4,5,6,7,8,9]
new_numbers = []

for i in numbers:
    i += 1
    new_numbers.append(i)


print(f"Lista 1: {numbers}")
print(f"Lista 2, modificada {new_numbers}")


# Objetivo: Hacer que cada numero aumente 10 veces:

tercera_lista = []

for i in numbers:
    i *= 10
    tercera_lista.append(i)


print(f"Tercera lista {tercera_lista}")


tercera_lista_con_list_comprehension = [i*10 for i in numbers]
print(tercera_lista_con_list_comprehension)
