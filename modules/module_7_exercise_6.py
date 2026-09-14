# Module 7 - Exercise 6: Pizza Unit Price
# Program that tells which of two pizzas is the better deal

import math


def unit_price(diameter, price):
    radius = diameter / 200  # centimetres to metres, diameter to radius
    area = math.pi * radius ** 2
    return price / area


diameter1 = float(input("Please enter the diameter of the first pizza: "))
price1 = float(input("Please enter the price of the first pizza: "))
diameter2 = float(input("Please enter the diameter of the second pizza: "))
price2 = float(input("Please enter the price of the second pizza: "))

unit_price1 = unit_price(diameter1, price1)
unit_price2 = unit_price(diameter2, price2)

print(f"Unit price of the first pizza: {unit_price1:.2f} euros / square metre")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros / square metre")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("The pizzas provide equal value for money.")
