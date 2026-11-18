username = input("Enter your username: ")
password = input("Enter your password: ")

long_enough = len(password) >= 8
has_digit = False
has_uppercase = False

for character in password:
    if character >= "0" and character <= "9":
        has_digit = True

    if character >= "A" and character <= "Z":
        has_uppercase = True

print("\n--- PASSWORD VALIDATION REPORT ---")
print("Username:", username)
print("Password:", "*" * len(password))

if long_enough:
    print("[PASS] At least 8 characters")
else:
    print("[FAIL] At least 8 characters")

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if has_uppercase:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

if long_enough and has_digit and has_uppercase:
    print("\nPassword is VALID!")
    print("Account created successfully for", username)
else:
    print("\nPassword is INVALID.")


