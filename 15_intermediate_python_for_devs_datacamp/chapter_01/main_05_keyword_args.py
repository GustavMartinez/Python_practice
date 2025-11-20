# Create a custom function

def average(values, rounded=False):

    # Round average to two decimal places if rounded is True:
    if rounded == True:
        average_value = sum(values) / len(values)
        rounded_average = round(average_value, 2)
        return rounded_average
    
    # Otherwise, dont round
    else:
        average_value = sum(values) / len(values)
        return average_value
    

preparation_times = [19,15,48.5,23,12.8965,64,45]

print(average(preparation_times))
print(average(preparation_times, rounded=True))