def search_keyword(filename, keyword):
    total_count = 0

    with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                # Search without worrying about uppercase or lowercase
                count = line.lower().count(keyword.lower())

                if count > 0:
                    print("Line", line_number, ":", line.strip())
                    total_count = total_count + count

    if total_count == 0:
            print("The keyword was not found.")

    print("Total times found:", total_count)



def display_document(filename):
        with open(filename, "r") as file:
            content = file.read()

        print("\nDocument contents:")
        print(content)

while True:
    print("\n===== KEYWORD SEARCH UTILITY =====")
    print("1. Search Keyword")
    print("2. View File Document")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        keyword = input("Enter the keyword to search for: ")

        if keyword == "":
            print("Please enter a keyword.")
        else:
            search_keyword("report.txt", keyword)

    elif choice == "2":
        display_document("report.txt")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")