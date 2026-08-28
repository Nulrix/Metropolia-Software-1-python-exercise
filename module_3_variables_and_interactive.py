"""
MODULE 3
"""

import math
import random


def exercise_1_greeting():
    """Exercise 1: Name greeting program"""
    print("\n=== EXERCISE 1: Name Greeting ===")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


def exercise_2_circle_area():
    """Exercise 2: Circle area calculator"""
    print("\n=== EXERCISE 2: Circle Area Calculator ===")
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f}")


def exercise_3_rectangle():
    """Exercise 3: Rectangle perimeter and area calculator"""
    print("\n=== EXERCISE 3: Rectangle Calculator ===")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    perimeter = 2 * (length + width)
    area = length * width
    
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")


def exercise_4_number_stats():
    """Exercise 4: Sum, product, and average of three numbers"""
    print("\n=== EXERCISE 4: Number Statistics ===")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    total_sum = num1 + num2 + num3
    product = num1 * num2 * num3
    average = total_sum / 3
    
    print(f"Sum: {total_sum}")
    print(f"Product: {product}")
    print(f"Average: {average:.2f}")


def exercise_5_weight_converter():
    """Exercise 5: Medieval weight converter"""
    print("\n=== EXERCISE 5: Medieval Weight Converter ===")
    
    LOTS_PER_GRAM = 13.3
    LOTS_PER_POUND = 32
    POUNDS_PER_TALENT = 20
    
    talents = float(input("Enter talents: "))
    pounds = float(input("Enter pounds: "))
    lots = float(input("Enter lots: "))
    
    total_lots = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND) + (pounds * LOTS_PER_POUND) + lots
    
    total_grams = total_lots * LOTS_PER_GRAM
    
    kilograms = int(total_grams // 1000)
    remaining_grams = total_grams % 1000
    
    print(f"\nThe weight in modern units:")
    print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")


def exercise_6_combination_lock():
    """Exercise 6: Random combination lock code generator"""
    print("\n=== EXERCISE 6: Random Combination Lock Generator ===")
    
    code_3digit = ""
    for i in range(3):
        code_3digit += str(random.randint(0, 9))

    code_4digit = ""
    for i in range(4):
        code_4digit += str(random.randint(1, 6))
    
    print("Combination lock codes:")
    print(f"3-digit code (0-9): {code_3digit}")
    print(f"4-digit code (1-6): {code_4digit}")


def project_1_game_starter():
    """Project 1: Game starter - asks for player name and age"""
    print("\n=== PROJECT 1: Game Starter ===")
    print("\n--- Text-Based Adventure Game ---")
    
    player_name = input("Enter your name: ")
    player_age = int(input("Enter your age: "))
    
    print(f"\nWelcome, {player_name}!")
    print(f"You are {player_age} years old.")
    print("Your adventure begins now...")


def main():
    """Main menu to select exercises"""
    while True:
        print("\n" + "="*50)
        print("MODULE 3: VARIABLES AND INTERACTIVE PROGRAMS")
        print("="*50)
        print("\nSelect an exercise to run:")
        print("1. Exercise 1 - Name Greeting")
        print("2. Exercise 2 - Circle Area Calculator")
        print("3. Exercise 3 - Rectangle Calculator")
        print("4. Exercise 4 - Number Statistics")
        print("5. Exercise 5 - Medieval Weight Converter")
        print("6. Exercise 6 - Combination Lock Generator")
        print("7. Project 1 - Game Starter")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-7): ").strip()
        
        if choice == "1":
            exercise_1_greeting()
        elif choice == "2":
            exercise_2_circle_area()
        elif choice == "3":
            exercise_3_rectangle()
        elif choice == "4":
            exercise_4_number_stats()
        elif choice == "5":
            exercise_5_weight_converter()
        elif choice == "6":
            exercise_6_combination_lock()
        elif choice == "7":
            project_1_game_starter()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
