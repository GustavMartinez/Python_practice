# list comprehension

numbers = [1,2,3,4,5]

# list comprehension: list = [new_item for item in list]
new_numbers = ['a'*n for n in numbers]

print(new_numbers)


name = "Gustavo"
[print(letter) for letter in name] # funciona perfecto

dubble = [n*2 for n in range(1,5)]
print(dubble)


# list comprehension with condition:
# new_list = [new_item for item in list if condition]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)