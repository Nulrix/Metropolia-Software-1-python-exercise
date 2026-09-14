# Module 7 - Exercise 3: Gallons To Litres
# Program that converts gallons to litres until a negative value is entered


def gallons_to_litres(gallons):
    return gallons * 3.785411784


while True:
    gallons = float(input("Please enter volume in gallons: "))
    if gallons < 0:
        print("Bye!")
        break

    litres = gallons_to_litres(gallons)
    print(f"{gallons} gallons is {litres:.2f} litres.")
