#Data types

#Strings == Texto
print("Esto es un string")
print("El texto es de tipo 'string'")

#integers == Numero enteros
print("Esto es un int: ", 3)
print("Los números enteros de de tipo 'int'")

#float == Numeros decimales
print("Esto es un float: ", 4.56)

#Boolean == logical. True or False
print("Esto es un bool: ", True)


#Accesar un texto a partir de su indice
print('hola'[3])  

#Type checking:
print(type('Holaaaa'))


#Conversion de texto para int y verificacion:
texto = '12345'  #variable con datos en string
numero = int(texto)  #Uso de la funcion int() para transformar string en int

print(type(numero))  #Type checking