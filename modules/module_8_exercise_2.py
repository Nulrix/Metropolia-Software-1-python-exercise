# Module 8 - Exercise 2: New Or Existing Name
# Program that collects names into a set until an empty string is entered

names = set()

while True:
    name = input("Please enter a name: ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("The names you entered were:")
for name in names:
    print(name)
