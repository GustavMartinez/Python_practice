capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# How to print "Lille":

print(travel_log["France"][1]) # Resuelto!


nested_list = ["A", "B",["C", "D"]]

print(nested_list[2][0])


travel_log_v2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}

# How to print "stuttgart"

print(travel_log_v2["Germany"]["cities_visited"][0]) # Resuelto! 