print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? \n$"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? \n"))
num_people = int(input("How many people to split the bill? \n"))

bill_each_person = (total_bill + (total_bill*(tip/100)))/num_people

print(f"Each person should pay: ${round(bill_each_person, 2)}")
