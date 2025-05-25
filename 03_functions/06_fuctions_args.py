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




# Primera funcion

list_of_numbers(2,5,3,6,8)

# Segunda funcion:
print()
print(multiply(5,8,4,2))