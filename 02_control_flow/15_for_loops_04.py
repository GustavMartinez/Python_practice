#You are going to write a program that calculates the sum of all the even numbers from 1 to x. If x is 100 then the first even number would be 2 an the last one is 100.

target = int(input("Enter a number between 0 and 1000 \n"))
sumatoria = 0
total_pares = 0

if target > 1000:
    print("Valor fuera de rango")

else:
    list_of_numbers = list(range(1,target+1))
    for i in list_of_numbers:
        if i % 2 == 0:
            sumatoria += i
            total_pares += 1
    print(f"Numero ingresado: {target}")
    print(f"numeros pares dentro y hasta {target}: {total_pares}")
    print(f"El resultado de la suma de los numeros pares dentro del rango es: {sumatoria}")