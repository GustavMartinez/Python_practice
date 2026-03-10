import random

def sorteo():
    numero_de_juegos = int(input("Cuantos juegos quieres?"))
    juegos(numero_de_juegos)


def juegos(x):
    for i in range(x):
        num = 6
        lista = []

        for i in range(1, 61):
            lista.append(i)

        juego = []

        while num > 0:
            random_number = random.choice(lista)
            if random_number not in juego:
                juego.append(random_number)
                num -= 1

        juego.sort()

        print(juego)


sorteo()