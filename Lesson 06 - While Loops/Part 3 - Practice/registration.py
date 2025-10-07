# Username validation
while True:
    username = input("Enter a username: ")
    if len(username) < 3:
        print("Please enter at least 3 characters!")
        continue
    if len(username) > 15:
        print("Please enter less than 15!")
        continue
    has_space = False
    for char in username:
        if char == " ":
            has_space = True
            break
    if has_space:
        print("No spaces allowed!")
        continue
    print(f"Welcome, '{username}'")
    break

# Password Validation
while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Please enter at least 8 characters!")
        continue
    has_digit = False
    has_uppercase = False
    for char in password:
        if 'A' <= char <= 'Z':
            has_uppercase = True
            continue
        if '0' <= char <= '9':
            has_digit = True
            continue
    if not has_uppercase:
        print("Requires at least one uppercase letter!")
        continue
    if not has_digit:
        print("Requires at least one digit!")
        continue
    print(f"Password: '{password}'")
    break
    
# Age validation
while True:
    age = int(input("Enter your age: "))
    if age < 13:
        print("Sorry, you are too young! Age limit: 13+")
        continue
    if age > 120:
        print("Please enter a valid age!")
        continue
    print(f"Age: {age} years")
    break

# Confirmation of registration
while True:
    confirmation = input("Enter yes or no to confirm or cancel registration: ")
    lower_confirm = confirmation.lower()
    if lower_confirm == "yes" or lower_confirm == "y":
        print("Registration confirmed. Successful!")
        break
    elif lower_confirm == "no" or lower_confirm == "n":
        print("Registration cancelled.")
        break
    else:
        print("Please enter yes/no/y/n.")
        continue
    break