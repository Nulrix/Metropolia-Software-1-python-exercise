# Module 5 - Exercise 1: Numbers Divisible by Three
# Uses a while loop to print all numbers divisible by 3 in range 1-1000

number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
