# Module 5 - Exercise 2: Inches to Centimeters Converter
# Converts inches to centimeters until user enters negative value

while True:
    inches = float(input("Enter inches (negative value to quit): "))
    
    if inches < 0:
        print("Program ended.")
        break
    
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} centimeters\n")
