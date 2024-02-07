#Write a program that adds the digits in a 2 digit number. Eg. if the imput was 35, then the output should be 3 + 5 = 8


numero = input("Escribe un numero de dos digitos: ")

numero_uno = numero[0]
numero_dos = numero[1]

resultado = int(numero_uno) + int(numero_dos)

print(resultado)