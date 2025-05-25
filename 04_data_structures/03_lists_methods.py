# Lista:

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Pineapple",
    "Mango",
    "Strawberry",
    "Blueberry",
    "Watermelon",
    "Grapes",
    "Peach",
    "Pear",
    "Cherry",
    "Kiwi",
    "Lemon",
    "Papaya"
]


print(len(fruits))

print("apple" in fruits)
print("Apple" in fruits)

fruits[0] = "Pineapple" # Reasing a value to the index 0

fruits.append("Lulo") # Adicionar un elemento al final de la lista

for _ in fruits:
    print(_)

fruits.remove('Apple') # Removes the element if it exists, otherwise, gives -1

fruits.insert(0, 'Piñacolada') # Adiciona un elemento en la posición 0

fruits.sort() # Organiza alfabeticamente la lista

fruits.reverse() # Revers in the order they appare
