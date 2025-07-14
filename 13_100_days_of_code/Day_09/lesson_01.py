# Dictionaries

my_dictionary = {
    "element_1":"Value x",
    "element_2":"value y",
    "element_3":"value z",
    "element_5":"value c"
}

for i in my_dictionary.values():
    print(i)

for j in my_dictionary.keys():
    print(j)

for k, v in my_dictionary.items():
    print(k, v)

print(my_dictionary["element_1"])


# Add new entry:

my_dictionary["element_4"] = "value_a"


for k, v in my_dictionary.items():
    print(k,v)


# Creating and empty dictionary:

my = {}


# Edit an item in a dictionary:

my_dictionary["element_1"] = "value b"


print(my_dictionary["element_1"])