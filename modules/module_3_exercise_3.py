# Module 3 - Exercise 3: Rectangle Calculator
# Program that asks for length and width and calculates perimeter and area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print(f"Perimeter: {perimeter:.2f}")
print(f"Area: {area:.2f}")
