"""
A one-line shortcut for the if-else statement (ternary operator)
Print or assing one of two values based on a condition

Form:

x if condition else y
"""

# EXAMPLE 1
num = 4

print("Positive" if num > 0 else "Negative")


# EXAMPLE 2
# Adding the result to a variable:
result = "Even" if num%2==0 else "Odd"
print(result)


# EXAMPLE 3
a = 6
b = 7

max_num = a if a > b else b # Esto puede leerse: return variable a if a > b, otherwise return b
print(max_num)


# EXAMPLE 4
age = 25

status = "Adult" if age >= 18 else "Child"
print(status)


#EXAMPLE 5
temperature = 30

weather = "Hot" if temperature > 20 else "Cold"
print(weather)


# EXAMPLE 6
user_role = "guest"

access_level = "Full Access" if user_role == 'admin' else "Limited Access"
print(access_level)