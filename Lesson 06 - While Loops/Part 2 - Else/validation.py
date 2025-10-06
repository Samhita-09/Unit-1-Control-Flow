# Input Validation 1 - Username Validation
while True:
    username = input("Enter a username (3 - 15 characters): ")
    if len(username) < 3:
        print("Error: can't be less than 3 characters")
        continue
    if len(username) > 15:
        print("Error: can't be more than 15 characters")
        continue
    # Check if username has spaces
    has_space = False
    for char in username:
        if char == " ":
            has_space = True
            break
    if has_space:
        print("Error: no spaces allowed in username")
        continue
    
    # username validation passed
    print(f"Username: '{username}' accepted!\n")
    break