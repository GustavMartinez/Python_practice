print("Welcome to the secret auction program.")

bids = {}

more_bidders = True

while more_bidders == True:

    name = input("What is your name?:\n")
    bid = int(input("What's your bid?:\n$"))

    bids[name] = bid

    
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if other_bidders == "no":
        more_bidders = False
    elif other_bidders == "yes":
        print("\n"*100)

highest = 0
winner = ''

for k,v in bids.items():
    if v > highest:
        highest = v
        winner = k

print(bids)
print(f"The winner is: {winner}, the bid was: {highest}")