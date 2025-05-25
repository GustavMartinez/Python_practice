# Functions:

def happy_birthday(name):
    print(f"Happy birthday {name}")


def happy_birthday_2(name, years):
    print(f"Happy Birthday {name}")
    print(f"You are {years} old!")


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")



happy_birthday("Joe")
print()
happy_birthday_2("Roger", 35)
happy_birthday_2("Novak", 32)
print()
display_invoice("Rafa", 42.10, "01/02")
display_invoice(username="Andy", amount=45, due_date="05/25")
