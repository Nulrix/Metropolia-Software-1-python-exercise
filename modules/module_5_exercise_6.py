# Module 5 - Exercise 6: Pi Approximation Calculator
# Uses Monte Carlo method to calculate approximate value of pi
# Generates random points in a square and checks if they fall inside the unit circle

import random

num_points = int(input("How many random points to generate? "))

points_inside_circle = 0

for i in range(num_points):
    # Generate random point in square (-1,-1) to (1,1)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Check if point is inside unit circle (x^2 + y^2 < 1)
    if x**2 + y**2 < 1:
        points_inside_circle += 1

# Calculate pi approximation: π ≈ 4n/N
pi_approximation = 4 * points_inside_circle / num_points

print(f"\nNumber of points generated: {num_points}")
print(f"Points inside circle: {points_inside_circle}")
print(f"Approximation of pi: {pi_approximation}")
