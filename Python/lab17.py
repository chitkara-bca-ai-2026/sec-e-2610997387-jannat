def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def display_student(roll, student):
    total, average = calculate_results(student["Marks"])

    print(
        "Roll No:", roll,
        "| Name:", student["Name"],
        "| Marks:", student["Marks"],
        "| Total:", total,
        "| Average:", round(average, 2))

def add_student(records, roll, name, marks):
    if roll in records:
        print("A student with that roll number already exists.")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks}
        print("Student added successfully.")

students = {
    "101": {"Name": "Rohan", "Marks": [85, 90, 78]},
    "102": {"Name": "Asha", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]} }


while True:
    print("\n===== STUDENT RECORDS MANAGEMENT SYSTEM =====")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(students) == 0:
            print("There are no student records.")
        else:
            print("\nStudent Records:")
            for roll in students:
                display_student(roll, students[roll])

    elif choice == "2":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")

        mark1 = int(input("Enter marks for subject 1: "))
        mark2 = int(input("Enter marks for subject 2: "))
        mark3 = int(input("Enter marks for subject 3: "))

        marks = [mark1, mark2, mark3]
        add_student(students, roll, name, marks)

        print("Please enter marks as whole numbers.")

    elif choice == "3":
        roll = input("Enter roll number to search: ")

        if roll in students:
            print("\nRecord found:")
            display_student(roll, students[roll])
        else:
            print("No student found with that roll number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")