def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(operations["*"](4,8))





def calculator():

    should_accumulate = True
    num_1 = float(input("What is the first number? "))


    while should_accumulate:

        for i in operations:
            print(i)

        operation = input("Pick an operation: ")

        num_2 = float(input("What is the second number? "))

        answer = operations[operation](num_1,num_2)

        print(f"{num_1} + {num_2} is: {answer}")


        choise = input(f"Type 'y' to continue calculating with {answer} or type 'no' to start a new calculation:")


        if choise == "y":
            num_1 = answer
        elif choise == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()



calculator()