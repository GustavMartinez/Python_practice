# Format a value based on what flags are inserted
# structure: {value:flags}

# EXAMPLE 1
value_1 = 3000.14159
value_2 = -9850.98765
value_3 = 12.35

print(f"Value 1 is {value_1:.2f}") # Flag indicando 2 decimales
print(f"Value 2 is {value_2:.3f}") # flag indicando 3 decimales
print(f"Value 3 is {value_3:.4f}") # Flag indicando 4 decimales

# EXAMPLE 2

print(f"Value 1 is {value_1:10}") # Flag indicando 10 espacios para mostrar el output
print(f"Value 2 is {value_2:10}") # flag indicando 10 espacios para mostrar el output
print(f"Value 3 is {value_3:10}") # Flag indicando 10 espacios para mostrar el output

# EXAMPLE 3

print(f"Value 1 is {value_1:010}") # Flag indicando 10 espacios para el output y completa con 0 el output
print(f"Value 2 is {value_2:010}") # flag indicando 10 espacios para el output y completa con 0 el output
print(f"Value 3 is {value_3:010}") # Flag indicando 10 espacios para el output y completa con 0 el output

# EXAMPLE 4

print(f"Value 1 is {value_1:<10}") # Flag indicando 10 espacios para el output y alineado a la izquierda
print(f"Value 2 is {value_2:<10}") # flag indicando 10 espacios para el output y alineado a la izquierda
print(f"Value 3 is {value_3:<10}") # Flag indicando 10 espacios para el output y alineado a la izquierda

# EXAMPLE 5

print(f"Value 1 is {value_1:>10}") # Flag indicando 10 espacios para el output y alineado a la derecha
print(f"Value 2 is {value_2:>10}") # flag indicando 10 espacios para el output y alineado a la derecha
print(f"Value 3 is {value_3:>10}") # Flag indicando 10 espacios para el output y alineado a la derecha

# EXAMPLE 6

print(f"Value 1 is {value_1:^20}") # Flag indicando 20 espacios para el output y alineado al centro
print(f"Value 2 is {value_2:^20}") # flag indicando 20 espacios para el output y alineado al centro
print(f"Value 3 is {value_3:^20}") # Flag indicando 20 espacios para el output y alineado al centro

# EXAMPLE 7

print(f"Value 1 is {value_1:,}") # Flag indicando separador de miles
print(f"Value 2 is {value_2:,}") # flag indicando separador de miles
print(f"Value 3 is {value_3:,}") # Flag indicando separador de miles

# EXAMPLE 8 - MIXING

print(f"Value 1 is {value_1:>20,.2f}") # Flag indicando separador de miles
print(f"Value 2 is {value_2:>20,.2f}") # flag indicando separador de miles
print(f"Value 3 is {value_3:>20,.2f}") # Flag indicando separador de miles