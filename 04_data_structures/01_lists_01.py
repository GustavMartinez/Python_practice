#crear una lista:
#nome da lista = [items separados por coma]

states_of_brasil = ['Minas Gerais', "Rio de Janeiro", "Matogrosso", "Rio grande do Sul", "Parana", "Amazonas", "Acre", "Roraima", "Rondonia", "Goiania"]

#Slicing lists by indexes
print(states_of_brasil[0:5:2])

#Change item in the list:

states_of_brasil[1] = "Rioooo"

print(states_of_brasil)



#Adicionar un elemento al final de la lista:

states_of_brasil.append("Alagoas")
print(states_of_brasil)



#Adicionar una lista al final de otra:

states_of_brasil.extend(["Pernambuco", "Piaui"])
print(states_of_brasil)