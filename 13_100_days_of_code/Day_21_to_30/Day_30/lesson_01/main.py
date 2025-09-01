# with open("a file") as file:
#     file.read()

"""
Errors:

FileNotFound
KeyError
IndexError
TypeError


"""

try:
    file = open("/13_100_days_of_code/a_file.txt")

except:
    file = open("./13_100_days_of_code/Day_21_to_30/Day_30/a_file.txt", 'w')
    file.write("Something")

finally:
    file.close()