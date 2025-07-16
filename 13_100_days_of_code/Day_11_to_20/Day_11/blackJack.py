import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print()
#initialize = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \t")


player_hand = []

for i in range(2):
    player_hand.append(random.choice(cards))

more_cards = True

while more_cards:
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    
    add = input("Try 'y' to get another card, type 'n' to pass: \t")

    if sum(player_hand) > 21:
        more_cards = False
        print(f"You lose. Your final score is {sum(player_hand)}")
    
    elif add == 'y':
        player_hand.append(random.choice(cards))
    
    elif add == 'n':
        more_cards = False
        print(f"Your final score is {sum(player_hand)}")
