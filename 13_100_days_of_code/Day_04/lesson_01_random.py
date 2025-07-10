# random module

import random

# random integer between 0 and 5
random_integer = random.randint(0,5)

print(random_integer)


# Importar mi propio módulo
import lesson_02_my_module

print(lesson_02_my_module.my_favorite_number)
print(lesson_02_my_module.my_favorite_planet)


# random float point number

random_number_0_to_1 = random.random()
print(random_number_0_to_1)


random_number_0_to_1_times_10 = random.random() * 10
print(random_number_0_to_1_times_10)


random_float = random.uniform(1, 10)
print(random_float)