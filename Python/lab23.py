def add_student_record():
    name = input("Enter student name: ")

    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    with open("student_data.txt", "a") as file:
            file.write(name + "," + str(mark1) + "," + str(mark2) + "," + str(mark3) + "\n")

    print("Student record saved.")

def display_records():
    with open("student_data.txt", "r") as file:
            records = file.readlines()

    if len(records) == 0:
            print("There are no student records yet.")
            return

    print("\nSaved student records:")

    for record in records:
            details = record.strip().split(",")

            name = details[0]
            mark1 = float(details[1])
            mark2 = float(details[2])
            mark3 = float(details[3])

            average = (mark1 + mark2 + mark3) / 3

            print("Name:", name)
            print("Marks:", mark1, mark2, mark3)
            print("Average:", round(average, 2))
            print()


while True:
    print("\n===== STUDENT MARKS FILE HANDLING =====")
    print("1. Add and Store Student Marks")
    print("2. Display Records and Average")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_student_record()

    elif choice == "2":
        display_records()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")