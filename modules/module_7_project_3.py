# Module 7 - Project 3: Main Menu Functions And Inventory
# Adventure game where each main menu selection is its own function

inventory = []
gold = 100


def print_menu():
    print()
    print("=== ADVENTURE GAME ===")
    print("(1) Pick up an item")
    print("(2) Show inventory")
    print("(3) Drop an item")
    print("(4) Visit the shop")
    print("(0) Quit")


def add_item():
    item = input("Which item do you pick up? ")
    if item == "":
        print("You pick up nothing.")
    else:
        inventory.append(item)
        print(f"{item} was added to your backpack.")


def show_inventory():
    if len(inventory) == 0:
        print("Your backpack is empty.")
    else:
        print("Your backpack contains:")
        number = 1
        for item in inventory:
            print(f"{number}. {item}")
            number += 1
        print(f"You have {len(inventory)} item(s) and {gold} gold.")


def drop_item():
    item = input("Which item do you drop? ")
    if item in inventory:
        inventory.remove(item)
        print(f"You dropped {item}.")
    else:
        print(f"You do not have {item}.")


def shop():
    global gold
    price = 30
    print(f"The merchant sells a torch for {price} gold. You have {gold} gold.")
    answer = input("Do you want to buy it (y/n)? ")

    if answer.lower() != "y":
        print("The merchant shrugs.")
    elif gold < price:
        print("You cannot afford that.")
    else:
        gold -= price
        inventory.append("torch")
        print(f"You bought a torch. You have {gold} gold left.")


while True:
    print_menu()
    choice = input("Please select: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        show_inventory()
    elif choice == "3":
        drop_item()
    elif choice == "4":
        shop()
    elif choice == "0":
        print("Thanks for playing!")
        break
    else:
        print("Unknown selection, please try again.")
