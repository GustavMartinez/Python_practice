try:
    age = int(input("How old are you?: "))

except ValueError:
    print("You have typed an invalid number. Try again with a numerical response")
    age = int(input("How old are you?: "))


if age > 18:
    print(f"You can drive at age {age}")