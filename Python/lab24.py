import csv


def display_all_students():
        with open("student_data.csv", "r") as file:
            reader = csv.DictReader(file)

            print("\nAll student records:")
            print("Roll No | Name | Subject | Marks")

            found_record = False

            for student in reader:
                found_record = True
                print(student["Roll_No"], "|", student["Name"], "|", student["Subject"], "|", student["Marks"])

            if found_record == False:
                print("There are no student records.")


def show_high_performers():
        with open("student_data.csv", "r") as file:
            reader = csv.DictReader(file)

            print("\nStudents who scored above 80:")
            print("Roll No | Name | Subject | Marks")

            found_student = False

            for student in reader:
                marks = int(student["Marks"])

                if marks > 80:
                    found_student = True
                    print(
                        student["Roll_No"], "|",
                        student["Name"], "|",
                        student["Subject"], "|",
                        marks)

            if found_student == False:
                print("No students scored above 80.")
                
while True:
    print("\n===== STUDENT RESULT ANALYSIS SYSTEM =====")
    print("1. Display All Students")
    print("2. Show Students with Marks Above 80")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        display_all_students()

    elif choice == "2":
        show_high_performers()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")