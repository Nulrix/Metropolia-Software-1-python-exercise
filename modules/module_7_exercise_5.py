# Module 7 - Exercise 5: Remove Uneven Numbers
# Program that returns a new list containing only the even numbers


def remove_uneven(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shortened = remove_uneven(original)

print(f"Original list: {original}")
print(f"Only even numbers: {shortened}")
