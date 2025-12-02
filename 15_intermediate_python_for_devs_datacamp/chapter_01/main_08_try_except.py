def average(values):
    try:
        # code that might cause an error
        average_value = sum(values) / len(values)
        return average_value
    
    except:
        # code to run if an error occurs:
        print("average() accepts a list or set. Please provide a correct data type")



## raise TypeError:

def average_2(values):
    # Check data type
    if type(values) in (list, set):
        # Run if appropriate data type was used
        average_value = sum(values) / len(values)
        return average_value
    else:
        # run if an exception occurs
        raise TypeError("average() accepts a list or set. Please provide a correct data type")