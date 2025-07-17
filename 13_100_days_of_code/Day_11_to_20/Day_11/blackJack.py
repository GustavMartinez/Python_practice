import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print()
#initialize = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \t")


player_hand = []
computer_hand = [5,11,7]

for i in range(2):
    player_hand.append(random.choice(cards))
    # computer_hand.append(random.choice(cards))



while sum(computer_hand) < 17:
    if 11 in computer_hand and sum(computer_hand) > 21:
        computer_hand.remove(11)
        computer_hand.append(1)
    computer_hand.append(random.choice(cards))


print(f"{computer_hand}, computer score: {sum(computer_hand)}")



more_cards = True

while more_cards:

    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"computer's firts card: {computer_hand[0]}")
    
    add = input("Try 'y' to get another card, type 'n' to pass: \t")


    if add == 'y':
        player_hand.append(random.choice(cards))


    elif add == 'n':
        more_cards = False
        print(f"Your final hand: {player_hand}, final score is {sum(player_hand)}")


    if sum(player_hand) > 21:
       more_cards = False
       print(f"Your cards: {player_hand}, You lose. Your final score is {sum(player_hand)}")
    
    
    

    
