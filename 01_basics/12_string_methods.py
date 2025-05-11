name = input("Enter your full name: ")


# Function to count the number of characters, including spaces
len_name = len(name) # Len with spaces
print(len_name)

# Look for the first apparence of a character:
character = name.find("t") # Esto busca por la letra o en el nombre, y devuelve el index.
print(character)


# Look for the last apparence of a character:
character = name.rfind("t") # Esto busca por la última posición de la letra t y devuelve el index
print(character)

# If there is no character in the string, the result is -1

# Capitalize the first letter of the string
capital = name.capitalize()
print(capital)


# Make all uppercase
all_upper = name.upper()
print(all_upper)


#Make all lowercase
all_lower = name.lower()
print(all_lower)

# Replace method:
replace_name = name.replace("m", 'n')
print(replace_name)

