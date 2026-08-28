"""
MODULE 4: Conditional Structures (if/elif/else)
All 4 exercises in one file
"""


def exercise_1_zander_fish():
    """Exercise 1: Zander fish size checker"""
    print("\n=== EXERCISE 1: Zander Fish Size Checker ===")
    
    MIN_SIZE = 42
    
    fish_length = float(input("Enter the length of the zander (in centimeters): "))
    
    if fish_length < MIN_SIZE:
        difference = MIN_SIZE - fish_length
        print(f"Release the fish back into the lake.")
        print(f"The fish is {difference:.1f} centimeters below the size limit.")
    else:
        print("The fish meets the size requirement!")


def exercise_2_cabin_class():
    """Exercise 2: Cruise ship cabin class classifier"""
    print("\n=== EXERCISE 2: Cruise Ship Cabin Classifier ===")
    
    cabin_class = input("Enter the cabin class (LUX, A, B, or C): ").upper()
    
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")


def exercise_3_hemoglobin_level():
    """Exercise 3: Hemoglobin level analyzer"""
    print("\n=== EXERCISE 3: Hemoglobin Level Analyzer ===")
    
    gender = input("Enter your biological gender (Female/Male): ").lower()
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
    
    if gender == "female":
        if hemoglobin < 117:
            print("Your hemoglobin level is low.")
        elif 117 <= hemoglobin <= 155:
            print("Your hemoglobin level is normal.")
        else:
            print("Your hemoglobin level is high.")
            
    elif gender == "male":
        if hemoglobin < 134:
            print("Your hemoglobin level is low.")
        elif 134 <= hemoglobin <= 167:
            print("Your hemoglobin level is normal.")
        else:
            print("Your hemoglobin level is high.")
    else:
        print("Invalid gender input. Please enter 'Female' or 'Male'.")


def exercise_4_leap_year():
    """Exercise 4: Leap year detector"""
    print("\n=== EXERCISE 4: Leap Year Detector ===")
    
    year = int(input("Enter a year: "))
    
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


def main():
    """Main menu to select exercises"""
    while True:
        print("\n" + "="*50)
        print("MODULE 4: CONDITIONAL STRUCTURES (if/elif/else)")
        print("="*50)
        print("\nSelect an exercise to run:")
        print("1. Exercise 1 - Zander Fish Size Checker")
        print("2. Exercise 2 - Cruise Ship Cabin Classifier")
        print("3. Exercise 3 - Hemoglobin Level Analyzer")
        print("4. Exercise 4 - Leap Year Detector")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-4): ").strip()
        
        if choice == "1":
            exercise_1_zander_fish()
        elif choice == "2":
            exercise_2_cabin_class()
        elif choice == "3":
            exercise_3_hemoglobin_level()
        elif choice == "4":
            exercise_4_leap_year()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
