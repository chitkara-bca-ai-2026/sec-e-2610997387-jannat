def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = fibonacci(n - 1)
    next_number = sequence[-1] + sequence[-2]
    sequence.append(next_number)

    return sequence

while True:
    print("\n===== MATHEMATICS LEARNING TOOL =====")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        try:
            number = int(input("Enter a non-negative integer: "))

            if number < 0:
                print("Please enter a number that is 0 or greater.")
            else:
                answer = factorial(number)
                print("The factorial of", number, "is", answer)

        except ValueError:
            print("Please enter a whole number.")

    elif choice == "2":
        try:
            terms = int(input("How many terms do you want? "))

            if terms < 0:
                print("Please enter a number that is 0 or greater.")
            else:
                answer = fibonacci(terms)
                print("Fibonacci series:", answer)

        except ValueError:
            print("Please enter a whole number.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")