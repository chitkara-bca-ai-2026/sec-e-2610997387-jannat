def create_book_file():
    file = open("books.txt", "r")
    file.close()
        
file = open("books.txt", "w")
file.write("Python Basics,John Smith,Programming\n")
file.write("Artificial Intelligence,Jane Lee,AI\n") 
file.write("Learning Python,Sam Brown,Programming\n")
file.write("Machine Learning,Alex Green,AI\n")
file.write("Software Design,Chris White,Software Engineering\n")
file.close()


def read_books():
    books = []

    file = open("books.txt", "r")
    for line in file:
        parts = line.strip().split(",")

        if len(parts) == 3:
            book = {
                "title": parts[0],
                "author": parts[1],
                "category": parts[2]
            }
            books.append(book)

    file.close()
    return books


def view_books_by_category():
    books = read_books()

    if len(books) == 0:
        print("There are no books in the library.")
        return

    categories = []

    for book in books:
        if book["category"] not in categories:
            categories.append(book["category"])

    print("\nBooks by category:")

    for category in categories:
        print("\n" + category + ":")
        for book in books:
            if book["category"] == category:
                print("-", book["title"], "by", book["author"])


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    category = input("Enter book category: ")

    file = open("books.txt", "a")
    file.write(title + "," + author + "," + category + "\n")
    file.close()

    print("Book added successfully.")


def view_categories():
    books = read_books()
    categories = []

    for book in books:
        if book["category"] not in categories:
            categories.append(book["category"])

    if len(categories) == 0:
        print("There are no categories yet.")
    else:
        print("\nLibrary categories:")
        for category in categories:
            print("-", category)


def add_to_wishlist():
    category = input("Enter the category the student wants: ")

    file = open("wishlist.txt", "a")
    file.write(category + "\n")
    file.close()

    print("Category added to the wishlist.")


def analyze_categories():
    books = read_books()
    library_categories = []

    for book in books:
        if book["category"] not in library_categories:
            library_categories.append(book["category"])

    # Read wishlist categories, if the file exists
    wishlist_categories = []

    try:
        file = open("wishlist.txt", "r")
        for line in file:
            category = line.strip()
            if category != "" and category not in wishlist_categories:
                wishlist_categories.append(category)
        file.close()
    except FileNotFoundError:
        pass

    if len(wishlist_categories) == 0:
        print("The wishlist is empty.")
        return

    print("\nCategory gap analysis:")

    for category in wishlist_categories:
        if category in library_categories:
            print(category + " - Available in the library")
        else:
            print(category + " - Not available; consider adding books in this category")


# Start the program
create_book_file()

while True:
    print("\n===== LIBRARY BOOK COLLECTION =====")
    print("1. View books by category")
    print("2. Add a new book")
    print("3. View library categories")
    print("4. Add a category to the student wishlist")
    print("5. Run category gap analysis")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_books_by_category()
    elif choice == "2":
        add_book()
    elif choice == "3":
        view_categories()
    elif choice == "4":
        add_to_wishlist()
    elif choice == "5":
        analyze_categories()
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Please enter a number from 1 to 6.")