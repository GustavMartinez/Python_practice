# Exercise

# To do: work out how much they need to pay based on their size choice

# to do: work out how much to add to their bill based on their pepperoni choice

# to do: work out their final amount based on whether if they want extra cheese.


print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza de you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

final_bill = 0

if size == "s" or size == "S":
    final_bill = 15
    if pepperoni == "y" or pepperoni =="Y":
        final_bill += 2
    if extra_cheese == "y" or extra_cheese == "Y":
        final_bill += 1

elif size == "m" or size == "M":
    final_bill = 20
    if pepperoni == "y" or pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "y" or extra_cheese == "Y":
        final_bill += 1

elif size == "l" or size == "L":
    final_bill = 25
    if pepperoni == "y" or pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "y" or extra_cheese == "Y":
        final_bill += 1

else:
    print("Not a valid choice.")


print(f"Your final bill is: ${final_bill}")