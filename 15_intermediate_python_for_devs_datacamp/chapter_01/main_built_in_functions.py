# Built-in functions, modules, and packages

preparation_times = [19,15,48.5,23,12.8965,64,45]

max_prep_time = max(preparation_times) # max value
min_prep_time = min(preparation_times) # min value
sum_prep_time = sum(preparation_times) # sum of elements
num_of_times_recorded = len(preparation_times) # number of elements
sorted_list = sorted(preparation_times) # Sorted list in ascending order


# Printing results:

print(f"Maximum preparation time: {max_prep_time} minutes")
print(f"Minimum preparation time: {min_prep_time} minutes")
print(f"Sum of all preparation times: {round(sum_prep_time, 2)}")
print(f"Number of times recorded: {num_of_times_recorded}")
print(f"list sorted in ascending order: {sorted_list}")
