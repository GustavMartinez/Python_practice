# Importar la biblioteca
import random

# Lista de las cartas en el set de cartas
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print()
#initialize = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \t")

# Creacion de la lista de las cartas del computador y el usuario. listas vacias
player_hand = []
computer_hand = []


# seleccion aleatoria de las cartas iniciales del pc y del jugador
for i in range(2):
    player_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))


# condicion para que el computador elija una carta mas, si las actuales cartas suman menos que 17
while sum(computer_hand) < 17:
    computer_hand.append(random.choice(cards))

# Mostrar las cartas del pc y la sumatoria de las mismas
print(f"{computer_hand}, computer score: {sum(computer_hand)}")



more_cards = True

# Condicion para que el usuario elija o no más cartas e indique si se paso de 21
while more_cards:

    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"computer's firts card: {computer_hand[0]}") # mostrar la primera carta del pc
    
    add = input("Try 'y' to get another card, type 'n' to pass: \t")


    if add == 'y':
        player_hand.append(random.choice(cards))


    elif add == 'n':
        more_cards = False
        print(f"Your final hand: {player_hand}, final score is {sum(player_hand)}")


    if sum(player_hand) > 21:
       more_cards = False
       print(f"Your cards: {player_hand}, You lose. Your final score is {sum(player_hand)}")


# problema: convertir el 11 en 1