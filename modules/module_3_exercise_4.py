# Module 3 - Exercise 4: Number Statistics
# Program that asks for three integers and calculates sum, product, and average

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

total_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = total_sum / 3

print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
