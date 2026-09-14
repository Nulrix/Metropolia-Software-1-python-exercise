# Module 8 - Exercise 1: Month To Season
# Program that prints the season of a month, seasons stored in a tuple

seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Please enter the number of the month: "))

if month < 1 or month > 12:
    print("That is not a valid month.")
else:
    # 12, 1, 2 -> winter; 3, 4, 5 -> spring; 6, 7, 8 -> summer; 9, 10, 11 -> autumn
    season = seasons[(month % 12) // 3]
    print(f"The season of month {month} is {season}.")
