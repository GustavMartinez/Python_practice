#Automatic pizza order program

#Based on a user's order, work out their final bill.

#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#add pepperoni for small pizza (Y or N): +$2
#add pepperoni for medium or large pizza (Y or N): +$3
#add extra cheese for any size pizza (Y or N): +$1

print("Thank you for choosing python pizza deliveries!")

size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

Bill = 0

if size == 'S':
    Bill = 15
    if add_pepperoni == 'Y':
        Bill +=2
    print("You order a Small pizza")
elif size == 'M':
    Bill = 20
    if add_pepperoni == 'Y':
        Bill +=3
    print("You order a Medium pizza")
elif size == 'L':
    Bill = 25
    if add_pepperoni == 'Y':
        Bill += 3
    print("You order a Large pizza")
else:
    print("I didnt understood, try again!")

if extra_cheese == 'Y':
    Bill += 1



print(f"Thank you for choosing python pizza deliveries! \n Your final bill is: $ {Bill}")