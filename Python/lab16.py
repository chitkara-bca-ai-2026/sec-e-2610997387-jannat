def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp

history = []

while True:
    print("\n===== UTILITY CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (remainder)")
    print("6. Power (default: square)")
    print("7. View calculation history")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "8":
        print("Calculator closed.")
        break

    elif choice == "7":
        if len(history) == 0:
            print("No calculations yet.")
        else:
            print("\nCalculation history:")
            for item in history:
                print(item)

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            a = float(input("Enter first number: "))
            b = None

            if choice == "6":
                exponent = input("Enter exponent, or press Enter to square: " )

                if exponent == "":
                    result = power(a)
                    calculation = str(a) + " squared = " + str(result)
                else:
                    b = float(exponent)
                    result = power(a, b)
                    calculation = str(a) + " to the power " + str(b) + " = " + str(result)

            else:
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = add(a, b)
                    calculation = str(a) + " + " + str(b) + " = " + str(result)

                elif choice == "2":
                    result = subtract(a, b)
                    calculation = str(a) + " - " + str(b) + " = " + str(result)

                elif choice == "3":
                    result = multiply(a, b)
                    calculation = str(a) + " * " + str(b) + " = " + str(result)

                elif choice == "4":
                    result = divide(a, b)
                    if result is None:
                        print("Cannot divide by zero.")
                        continue
                    calculation = str(a) + " / " + str(b) + " = " + str(result)

                elif choice == "5":
                    result = modulus(a, b)
                    if result is None:
                        print("Cannot find a remainder using zero.")
                        continue
                    calculation = str(a) + " % " + str(b) + " = " + str(result)

            print("Result:", result)
            history.append(calculation)

        except ValueError:
            print("Please enter numbers only.")

    else:
        print("Invalid choice. Enter a number from 1 to 8.")