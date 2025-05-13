# Formar a value based on what flags are inserted
# structure: {value:flags}

# EXAMPLE 1
value_1 = 3.14159
value_2 = -985.98765
value_3 = 12.35

print(f"Value 1 is {value_1:.2f}") # Flag indicando 2 decimales
print(f"Value 2 is {value_2:.3f}") # flag indicando 3 decimales
print(f"Value 3 is {value_3:.4f}") # Flag indicando 4 decimales

# EXAMPLE 2

print(f"Value 1 is {value_1:10}") # Flag indicando 10 espacios para mostrar el output
print(f"Value 2 is {value_2:10}") # flag indicando 10 espacios para mostrar el output
print(f"Value 3 is {value_3:10}") # Flag indicando 10 espacios para mostrar el output