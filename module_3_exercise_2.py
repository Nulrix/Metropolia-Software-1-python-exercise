# Module 3 - Exercise 2: Circle Area Calculator
# Program that asks for radius and calculates the area of a circle

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2

print(f"The area of the circle is: {area:.2f}")
