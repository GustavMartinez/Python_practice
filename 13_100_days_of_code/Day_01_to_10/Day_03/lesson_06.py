# Exercise

# To do: work out how much they need to pay based on their size choice

# to do: work out how much to add to their bill based on their pepperoni choice

# to do: work out their final amount based on whether if they want extra cheese.


print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza de you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

final_bill = 0

if size == "S":
    final_bill = 15
    if pepperoni =="Y":
        final_bill += 2
    if extra_cheese == "Y":
        final_bill += 1

elif size == "M":
    final_bill = 20
    if pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1

elif size == "L":
    final_bill = 25
    if pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1

else:
    print("Not a valid choice.")


print(f"Your final bill is: ${final_bill}")
