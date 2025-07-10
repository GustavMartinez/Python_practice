import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
numbers = [0,1,2,3,4,5,6,7,8,9]


print("Welcome to the PyPassword Generator!")


num_letters = int(input("How many letters would you like in your password?"))
num_symbols = int(input("How many symbols would you like?"))
num_numbers = int(input("How many numbers would you like?"))


# Easy password

easy_password = []

for i in range(0, num_letters):
    easy_password.append(random.choice(letters))

for j in range(0, num_symbols):
    easy_password.append(random.choice(symbols))

for k in range(0, num_numbers):
    easy_password.append(random.choice(numbers))

print(easy_password)


# Hard password

hard_password = easy_password.copy()

random.shuffle(hard_password)


print(hard_password)