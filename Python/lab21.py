def get_document_statistics():
        with open("document.txt", "r") as file:
            content = file.read()

        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        return len(lines), len(words), characters


def display_document_content():
        with open("document.txt", "r") as file:
            content = file.read()

        print("\nDocument contents:")
        print(content)

while True:
    print("\n===== DOCUMENT STATISTICS TOOL =====")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        result = get_document_statistics()

        if result is None:
            print("document.txt was not found. Create it first.")
        else:
            lines, words, characters = result
            print("\nDocument Statistics:")
            print("Total lines:", lines)
            print("Total words:", words)
            print("Total characters:", characters)

    elif choice == "2":
        display_document_content()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")