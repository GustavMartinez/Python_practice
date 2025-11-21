# Create a custom function to calculate the average value:

def average(values):

    """
    
    Find the mean in a sequence of values and round to two decimal places.
    
    Args:
        values (list): A list of numeric values
    
    Returns:
        rounded_average (float): The mean of values, rounded to two decimal places.
    
    """


    # Calculate the average
    average_value = sum(values) / len(values)

    # Round the results
    rounded_average = round(average_value, 2)

    # Return rounded_average as an output
    return rounded_average


def generate_email(full_name):
    name_parts = full_name.split()
    email = name_parts[0].lower() + "." + name_parts[1].lower() + "@techcompany.com"

    return email


# Using the average function:

preparation_times = [19,15,48.5,23,12.8965,64,45]
average_value = average(preparation_times)
print(average_value)


# Using the generate_email function:

full_name = "Alan Turing"
print(generate_email(full_name))


# Accessing the docstring:
print(average.__doc__)