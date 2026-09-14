# Module 8 - Exercise 3: Airport Data
# Program that stores airports in a dictionary as ICAO code and name

airports = {}

while True:
    print()
    print("(1) Enter a new airport")
    print("(2) Fetch airport information")
    print("(3) Quit")
    choice = input("Please select: ")

    if choice == "1":
        icao = input("Please enter the ICAO code: ").upper()
        name = input("Please enter the name of the airport: ")
        airports[icao] = name
        print(f"{name} was saved with the code {icao}.")

    elif choice == "2":
        icao = input("Please enter the ICAO code: ").upper()
        if icao in airports:
            print(f"The name of the airport is {airports[icao]}.")
        else:
            print(f"No airport was found with the code {icao}.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Unknown selection, please try again.")
