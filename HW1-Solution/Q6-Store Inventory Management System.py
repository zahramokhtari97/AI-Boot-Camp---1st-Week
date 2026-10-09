
inventory = {}

def add_product():
    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity to add: "))
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    inventory[name] = inventory.get(name, 0) + quantity
    print(f"{name} added successfully. Current stock: {inventory[name]}")


def sell_product():
    name = input("Enter product name to sell: ").strip()

    if name not in inventory:
        print("Product not found in inventory.")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if quantity > inventory[name]:
        print("Insufficient stock. Sale cannot be completed.")
        return

    inventory[name] -= quantity

    if inventory[name] == 0:
        del inventory[name]
        print(f"{name} is out of stock and has been removed.")
    else:
        print(f"Sale completed. Remaining stock of {name}: {inventory[name]}")


def search_product():
    name = input("Enter product name to search for: ").strip()

    if name in inventory:
        print(f"{name}: {inventory[name]} units available.")
    else:
        print("Product not found in inventory.")


def show_inventory():
    if not inventory:
        print("The inventory is empty.")
        return

    print("\nCurrent Inventory:")

    for name, quantity in inventory.items():
        print(f"{name} - {quantity}")


def save_inventory():
    try:
        with open("inventory.txt", "w", encoding="utf-8") as file:
            for name, quantity in inventory.items():
                file.write(f"{name} - {quantity}\n")

        print("Inventory saved successfully to inventory.txt.")

    except OSError as error:
        print(f"Could not save inventory: {error}")


def inventory_report():
    if not inventory:
        print("The inventory is empty. No report can be generated.")
        return

    product_count = len(inventory)
    total_stock = sum(inventory.values())

    highest_quantity = max(inventory.values())
    lowest_quantity = min(inventory.values())

    highest_products = [
        name for name, quantity in inventory.items()
        if quantity == highest_quantity
    ]

    lowest_products = [
        name for name, quantity in inventory.items()
        if quantity == lowest_quantity
    ]

    print("\nInventory Report")
    print("------------------------------")
    print(f"Number of products: {product_count}")
    print(f"Total stock: {total_stock}")
    print(f"Highest stock: {', '.join(highest_products)} ({highest_quantity})")
    print(f"Lowest stock: {', '.join(lowest_products)} ({lowest_quantity})")


print("Welcome to the Store Inventory Management System!")
print("Commands: add, sell, search, show, save, report, exit")

while True:
    command = input("\nEnter a command: ").strip().lower()

    if command == "add":
        add_product()

    elif command == "sell":
        sell_product()

    elif command == "search":
        search_product()

    elif command == "show":
        show_inventory()

    elif command == "save":
        save_inventory()

    elif command == "report":
        inventory_report()

    elif command == "exit":
        print("Exiting the inventory management system. Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")