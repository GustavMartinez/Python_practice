def add(*args):
    return sum(args)



print(add(5, 8, 10, 15, 50,60))


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)