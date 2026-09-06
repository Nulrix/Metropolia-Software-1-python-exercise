# Module 6 - Exercise 4: City List
# Asks user to enter 5 city names and prints them in the same order

cities = []

# Use for loop to read city names
for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

# Use for/in loop to iterate and print
print("\nCities in the order entered:")
for city in cities:
    print(city)
