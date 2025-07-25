# Basic dictionary:
# Keys are unique

person = {
    "name" : "Alice",
    "age" : 30,
}

# Call the value (Alice) by the key (name)
print(f"La edad es: {person['age']}")
print(f"El nombre es: {person['name']}")


# Exercise:
# Create a dictionary called book with the following key-value pairs:
# "title": "Python Basics"
# "author": "John Doe"
# "year": 2023
# Then, print the value of "author".

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "year": 2023
}

print(f"El autor del libro {book['title']}, publicado en el año {book['year']}, es: {book['author']}")

################################################################

# Adding, updating, and deleting items:

# Add a new key-value pair:
book["pages"] = 250

#Update a value
book['year'] = 2024

#Delete a key:
del book["pages"]

# Adding:
book["publisher"] = "TechPress"

# Update
book["year"] = 2025

# delete
del book["title"]

#################################################################

# Looping through a dictionary

# Looping through keys:

for key in book:
    print(key)

# Loopong through values:

for value in book.values():
    print(value)

print()
# Looping through a key-value pair:
for key, value in book.items():
    print(key, "=>", value)