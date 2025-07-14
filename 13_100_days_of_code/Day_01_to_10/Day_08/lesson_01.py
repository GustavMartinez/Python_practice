# greeting function
def greet(name):
    print(f"Helloooo {name}")
    print(f"How do you do {name}?")
    print(f"Is'n the weather nice {name} ?")


greet("Angela")
greet("Jack")


# Life in weeks
def life_in_weeks(age):
    x = 90 * 52 - (age * 52)
    print(f"You have {x} weeks left.")
    
    
life_in_weeks(20)
life_in_weeks(40)
life_in_weeks(70)