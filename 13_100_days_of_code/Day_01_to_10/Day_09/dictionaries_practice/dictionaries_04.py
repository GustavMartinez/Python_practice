
"""

Tareas:

Agrega una nueva venta al mes de enero (puedes inventar un valor).

Crea un nuevo mes "abril" con una lista de al menos 2 ventas.

Calcula el total de ventas de febrero y muéstralo.

Calcula el total anual (suma de todos los valores de todas las listas).

Encuentra el mes con mayor total de ventas.

Muestra el diccionario final de ventas.

"""

ventas = {
    "enero" : [1200, 2300, 4100],
    "febrero" : [1500, 2100],
    "marzo" : [5000, 1000, 700],
}

# tarea 1
ventas["enero"].append(3000)

# tarea 2
ventas["abril"] = [6000, 1200]

# tarea 3
total_febrero = sum(ventas["febrero"])
print(f"El total de ventas de febrero fue: {total_febrero}")

# tarea 4

total = 0

for values in ventas.values():
    total += sum(values)

print(f"El total anual es: {total}")

# tarea 5

mayor_venta_mes = 0
nombre_mes = ""

for k, v in ventas.items():
    mes = sum(v)
    if mes > mayor_venta_mes:
        mayor_venta_mes = mes
        nombre_mes = k

print(f"El mes con mayor total de ventas es: {nombre_mes}")

# tarea 6:
print(ventas)