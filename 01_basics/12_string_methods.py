name = input("Enter your full name: ")


# Function to count the number of characters, including spaces
len_name = len(name) # Len with spaces
print(f"El número de caracteres es: {len_name}")

# Look for the first apparence of a character:
character = name.find("t") # Esto busca por la letra o en el nombre, y devuelve el index.
print(f"La primera 't', aparece en el indice: {character}")


# Look for the last apparence of a character:
character = name.rfind("t") # Esto busca por la última posición de la letra t y devuelve el index
print(f"La última 't' que aparece en el texto esta en el indice: {character}")

# If there is no character in the string, the result is -1

# Capitalize the first letter of the string
capital = name.capitalize()
print(f"Primera letra capitalizada: {capital}")


# Make all uppercase
all_upper = name.upper()
print(f"Convertir todo el texto a mayuscula: {all_upper}")


#Make all lowercase
all_lower = name.lower()
print(f"Convertir todo el texto a minuscula: {all_lower}")

# Replace method:
replace_name = name.replace("m", 'n')
print(replace_name)

