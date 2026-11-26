def append_entry(date, entry):
    with open("daily_log.txt", "a") as file:
        file.write(date + " - " + entry + "\n")

    print("Entry saved successfully.")

def display_log():
    try:
        with open("daily_log.txt", "r") as file:
            log_entries = file.read()

        if log_entries == "":
            print("The log book is empty.")
        else:
            print("\n===== DAILY LOG =====")
            print(log_entries)

    except FileNotFoundError:
        print("No log entries yet. Add an entry first.")


while True:
    print("\n===== DAILY LOG BOOK =====")
    print("1. Add Daily Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        date = input("Enter the date: ")
        entry = input("What did you do? ")
        append_entry(date, entry)

    elif choice == "2":
        display_log()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")