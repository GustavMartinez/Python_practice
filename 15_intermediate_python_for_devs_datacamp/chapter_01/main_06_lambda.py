# Lambda functions:

"""

lambda keyword:
- Represents an anonymous function

lambda arguments: expression
- Convention is to use x for a single argument
- The expression is the equivalent of the function body
- No return statement is required
- Can be stored as a variable

"""

# Lambda average function:

print(lambda x: sum(x) / len(x))


# get the average:

(lambda x: sum(x) / len(x)) ([3,6,9])
print((lambda x: sum(x) / len(x)) ([3,6,9]))


# Storing and calling a lambda function:

average = lambda x: sum(x) / len(x)

# call the average function:

print(average([5,10,15]))


## lambda functions - multiple parameters

# Two parameters:

power = lambda x, y: x**y
print(power(2,5))


## Lambda functions - Lambda functions with iterables

# map() applies a function to all elements in an iterable

names = ["john", "sally", "leah"]

# apply a lambda function inside map():

capitalize = map(lambda x: x.capitalize(), names)

# convert to a list:

capitalize_list = list(capitalize)

print(capitalize_list)
