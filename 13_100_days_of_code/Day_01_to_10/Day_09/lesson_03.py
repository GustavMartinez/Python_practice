capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid"
}


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
    "Spain": ["Madrid", "Barcelona", "Valencia"],
    "Italy": ["Florenca", "Roma", {'Veneza': ['Martelago', 'Maerne']}]
}

# How to print "Lille":

print(travel_log["France"][1]) # Resuelto!

# How to print "Valencia":

print(travel_log["Spain"][2]) # Resuelto!


# How to print Maerne
# dictionary >> italy key >> thrid element >> veneza key >> second element
print(travel_log["Italy"][2]['Veneza'][1]) 


# Nesting lists
nested_list = ["A", "B",["C", "D", "E"], "F"]

print(nested_list[2][0]) # print "C"
print(nested_list[2][2]) # print "E"


travel_log_v2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    },
    "Spain":{
        "num_times_visited":3,
        "cities_visited": ["Madrid", "Barcelona", "Valencia"]
    }
}

# How to print "stuttgart"

print(travel_log_v2["Germany"]["cities_visited"][0]) # Resuelto! 

# How to print "Barcelona"

print(travel_log_v2["Spain"]["cities_visited"][1]) # Resuelto!