#Logical operators

# and 
# or
# not

print("the Love Calculator is calculating your score...")
name1 = input("what is your name? ")
name2 = input("what is their name? ")

T = name1.count("t")
R = name1.count("r")
U = name1.count("u")
E = name1.count("e")

L = name1.count("l")
O = name1.count("o")
V = name1.count("v")
E2 = name1.count("e")

T += name2.count("t")
R += name2.count("r")
U += name2.count("u")
E += name2.count("e")

total_true = T + R + U + E

L += name2.count("l")
O += name2.count("o")
V += name2.count("v")
E2 += name2.count("e")

total_love = L + O + V + E2


score = int(str(total_true)+str(total_love))

if score < 10 or score > 90:
    print(f"Your score is: {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is: {score}, you are alright together")
else:
    print(f"Your score is {score}")