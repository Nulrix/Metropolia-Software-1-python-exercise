# Module 7 - Exercise 4: Sum Of A List
# Program that calculates the sum of the numbers in a list with a function


def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


my_list = [1, 2, 3, 4, 5, 10, 20]

print(f"The list is: {my_list}")
print(f"The sum of the numbers is: {list_sum(my_list)}")
