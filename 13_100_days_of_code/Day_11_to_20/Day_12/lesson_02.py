# Prime number checker

"""

You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

"""

def is_prime(user_number):
    if user_number % 2 == 0 and user_number != 2:
        return False
    elif user_number % 3 == 0 and user_number != 3:
        return False
    elif user_number % 5 == 0 and user_number != 5:
        return False
    else:
        return True

is_prime()