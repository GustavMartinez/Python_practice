# Dictionaries

my_dictionary = {
    "element_1":"Value x",
    "element_2":"value y",
    "element_3":"value z",
    "element_5":"value c",
}

# Loop through the values
for each_value in my_dictionary.values():
    each_value = each_value + "-abc"
    print(each_value)

# Loop through the keys
for each_key in my_dictionary.keys():
    print(each_key)

# Loop through the items
for each_key, each_value in my_dictionary.items():
    each_value = each_value + '-def'
    print(each_key, each_value)

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



dictionary_of_cities = {
    "Minas Gerais" : "Belo Horizonte",
    "Rio de Janeiro" : "Rio de Janeiro",
    "Sao Paulo" : "Sao Paulo",
}

