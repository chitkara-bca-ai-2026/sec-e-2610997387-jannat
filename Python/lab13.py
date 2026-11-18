inventory = ["Laptop", "Mouse", "Keyboard"]

while True:
    print("\n--- INVENTORY MENU ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nInventory:")
        for item in inventory:
            print("-", item)

    elif choice == "2":
        item = input("Enter item to add: ")
        inventory.append(item)
        print(item, "added to inventory.")

    elif choice == "3":
        item = input("Enter item to remove: ")

        if item in inventory:
            inventory.remove(item)
            print(item, "removed from inventory.")
        else:
            print("Item not found.")

    elif choice == "4":
        inventory.sort()
        print("Inventory sorted.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")