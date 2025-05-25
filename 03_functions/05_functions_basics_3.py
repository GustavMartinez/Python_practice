def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("gustavo", "martinez")
sponge = create_name(first="spongebob", last="squarepants")
print(full_name)
print(sponge)  