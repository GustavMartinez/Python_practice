print("Welcome to the auction program")

bidders = {}
bidding = True

while bidding:

    bidder_name = input("What is your name?:\t")
    bid = float(input("What is your bid?:\t$"))
    bidders[bidder_name] = bid
    more_bidders = input("There are other bidders? y or n:\t").lower()

    if more_bidders == 'n':
        bidding = False
    else:
        print("\n" * 15)

count = 0
higher_bidder = ""

for k,v in bidders.items():
    if v > count:
        count = v
        higher_bidder = k

print(f"The highest bidder was: {higher_bidder}")
