print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:        # 45 <= age <= 55 
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo take? Type y for Yes and n for No: ")    
    if wants_photo == "y":
        bill += 3
    
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")