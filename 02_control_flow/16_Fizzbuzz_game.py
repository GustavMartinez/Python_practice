#You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules:

# 1. Your program should print each number from 1 to 100 in turn and include number 100.
# 2. when the number is divisible by 3 then instead of printing the number it should print "Fizz"
# 3. when the number is divisible by 5 then instead of printing the number it should print "Buzz"
# 4. If the number is divisible by both 3 and 5, then instead of the number it should print "FizzBuzz"


total_list = list(range(0, 100 + 1))


for i in total_list:
        if i % 3 == 0 and i % 5 == 0:
                total_list[i] = "FizzBuzz"
        elif i % 3 == 0:
                total_list[i] = "Fizz"
        elif i % 5 == 0:
                total_list[i] = "Buzz"

total_list.pop(0)

for i in total_list:
       print(i)