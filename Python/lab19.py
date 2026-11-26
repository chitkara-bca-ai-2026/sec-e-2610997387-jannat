def write_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")


def read_notes():
    with open("notes.txt", "r") as file:
            notes = file.read()

    if notes == "":
         print("There are no saved notes yet.")
    else:
        print("\nSaved notes:")
        print(notes)


while True:
    print("\n===== STUDENT NOTES MANAGEMENT SYSTEM =====")
    print("1. Write / Save Note")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        note = input("Enter your note: ")
        write_note(note)

    elif choice == "2":
        read_notes()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")