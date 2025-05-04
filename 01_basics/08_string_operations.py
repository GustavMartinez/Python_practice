# Como el tipo de dato string es un texto, generalmente no se pueden hacer operaciones con ellos.
# Por ejemplo:

"""

comida = "chinesse" - "food" # Esto genera un TypeError, pues no se puede hacer esa operación
comida = "chinesse" / "food" # Esto también genera un TypeError
comida = "chinesse" * "food" # Esto también genera un TypeError


"""



# Sin embargo, hay dos exepciones: '+' y '*'

# El operador '+' realiza la operación de concatenación, es decir, une dos strings:

mensaje = "Hola" + "mundo" # Esto genera como resultado "Holamundo"
print(mensaje)

# Como el mensaje aparece todo unido, puede adicionarse un espacio para seperar los strings

nuevo_mensaje = "Hola" + " " + "mundo"
print(nuevo_mensaje)


# El operador '*' realiza la operación de repetición, cuando se multiplica un string por un entero

otro_mensaje =  3 * "Hello "
print(otro_mensaje)
