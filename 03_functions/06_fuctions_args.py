def list_of_numbers(*numbers):
    """
    Esta funcion puede recibir cualquier cantidad de numeros
    """
    for number in numbers:
        print(number)

def multiply(*numbers):
    """
    Esta funcion multiplica todos los números que se le pasen
    """
    total = 1
    for number in numbers:
        total*= number
    return total


def number_args(*number):
    print(number[0]*number[1])



# Primera funcion

list_of_numbers(2,5,3,6,8)


print()
# Segunda funcion:

print(multiply(5,8,4,2))


print()
# Tercera funcion:
number_args(5,6,4,7,2)


# OTRA FUNCION:

args_tuple = (2,5,9,84,4)

def number_args_2(*numbers):
    print(numbers[0] * numbers[1])

number_args_2(*args_tuple) # TENER EN CUENTA EL ASTERISCO QUE SE LE PASA A LA FUNCION