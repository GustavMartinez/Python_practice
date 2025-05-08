'''
Un string es una secuencia de caracteres. Los caracteres pueden ser accesados uno por uno, con el "bracket operator" = []
'''
fruta = "Mango"
letra = fruta[0]
print(letra)
letra = fruta[1]
print(letra)
letra = fruta[2]
print(letra)
letra = fruta[3]
print(letra)
letra = fruta[4]
print(letra)

#Para retornar la longitud o número de caracteres dentro de un string
longitud = len(fruta)
print(longitud)

#Para retornar el último valor del string:
print(fruta[longitud - 1])

#Traversal through a string with a loop
#Esto envuelve el procesar un string un caracter al tiempo. A menudo inicia al principio, selecciona cada caracter y hace algo con el, y continua hasta el final
#Por ejemplo:

for letra in fruta:
    print(letra)


#String slices
#Un segmento de un string se llama "slice". seleccionar un slice es similar a seleccionar un caracter
    
segmento_uno = fruta[0:3]
segmento_dos = fruta[3:]
print(segmento_uno)
print(segmento_dos)

#Looping and counting
#Este es un ejemplo de un programa que cuenta el numero de veces que una letra aparece en un string:

def contador_de_letras (palabra, letra):
    word = palabra
    conteo = 0
    for i in word:
        if i == letra:
            conteo += 1
    print(f"El numero de veces que la letra {letra} está dentro de la palabra {palabra} es: {conteo}")

#palabra_input = input("Ingresa una palabra: \n")
#letra_input = input("Ingresa la letra que quieres contar: \n")

#contador_de_letras(palabra=palabra_input, letra=letra_input)


#para remover espacios en blanco al inicio y fin de un string se usa el metodo "strip"

line = " here we go "
new_line = line.strip()
print(new_line)