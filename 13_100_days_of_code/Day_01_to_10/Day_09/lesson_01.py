# Dictionaries

my_dictionary = {
    "element_1":"Value x",
    "element_2":"value y",
    "element_3":"value z",
    "element_5":"value c",
}

# Loop through the values
for i in my_dictionary.values():
    i = i + "-abc"
    print(i)

# Loop through the keys
for j in my_dictionary.keys():
    print(j)

# Loop through the items
for k, v in my_dictionary.items():
    v = v + '-def'
    print(k, v)

print()
# Printing the value for the specified key
print(my_dictionary["element_1"])


# Add new entry:

my_dictionary["element_4"] = "value_a"


for k, v in my_dictionary.items():
    print(k,v)


# Creating and empty dictionary:
my = {}
print(my)


print()
# Edit an item in a dictionary:

my_dictionary["element_1"] = "value b"


print(my_dictionary["element_1"])