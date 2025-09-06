my_dict = {
    "nombre": ["Gustavo", "Gabriel"],
    "Edad": [34, 50],
    "Pais": ["Colombia", "Peru"]
}


for country in my_dict["Pais"]:
    print(country)

print(my_dict["nombre"][0])

if 'Colombia' in my_dict["Pais"]:
    print('si si')