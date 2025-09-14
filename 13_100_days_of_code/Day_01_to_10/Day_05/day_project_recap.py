import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
numbers = ["0","1","2","3","4","5","6","7","8","9"]


print("Welcome to the PyPassword Generator!")

# User input
letter = int(input("How many letters do you want?\n"))
symbol = int(input("How many symbols do you want?\n"))
number = int(input("How many numbers do you want\n"))


let = []

# Select the letters, symbols and numbers randomlly
for i in range(letter):
    let.append(rd.choice(letters))

for i in range(symbol):
    let.append(rd.choice(symbols))

for i in range(number):
    let.append(rd.choice(numbers))
    

# Make the list in different order
rd.shuffle(let)

# convert the list to string
password = "".join(let)


# Final password
print(f"the final password is: {password}")
