password = input("Enter a password: ")
has_uppercase = 0
has_lowercase = 0
has_digit = 0
special_char = 0
password_strength = "Strong"

if len(password) < 8:
    print("Password is not long enough.")
    quit()
   
for char in password:
    if 'A' <= char <= 'Z':
        has_uppercase += 1
    elif 'a' <= char <= 'z':
        has_lowercase += 1
    elif '0' <= char <= '9':
        has_digit += 1
    else:
        if char != " ":
            special_char += 1

repeated = 1;    
for i in range((len(password)-1)):
    if password[i] == password[i+1]:
        repeated+=1
        if repeated >= 3:
            password_strength = "WEAK"
            break
    else:
        repeated = 1
    
sequence = 1 
seqString = password[0]   
for i in range(len(password) - 1):
    if ord(password[i]) + 1 == ord(password[i+1]) or ord(password[i]) - 1 == ord(password[i+1]):
        sequence += 1
        seqString += password[i+1]
        if sequence >= 3:
            password_strength = "MEDIUM"
            break
    else:
        sequence = 1
        seqString = password[i+1]
        
print("CHARACTER COUNTS:")
print(f"Length: {len(password)}")
print(f"Uppercase Letters: {has_uppercase}")
print(f"Lowercase Letters: {has_lowercase}")
print(f"Digits: {has_digit}")
print(f"Special Characters: {special_char}")

print("REQUIREMENTS CHECK:")

if has_uppercase > 0:
    print(f"Uppercase Letters: PASSED")
else:
    print(f"Uppercase Letters: FAILED")
if has_lowercase > 0:
    print(f"Lowercase Letters: PASSED")
else:
    print(f"Lowercase Letters: FAILED")
if has_digit > 0:
    print(f"Digits: PASSED")
else:
    print(f"Digits: FAILED")
if special_char > 0:
    print(f"Special Characters: PASSED")
else:
    print(f"Special Characters: FAILED")
    quit()
    
print("SECURITY ISSUES:")
if repeated >= 3:
    print("Repeated characters exist (3+)")
else:
    print("No repeated characters (3+)")
    
if sequence >= 3:
    print(f"Contains sequence '{seqString}'")
else:
    print("Does not contain sequence")

print(f"FINAL RATING: {password_strength}")
if sequence >=3:
    print("All requirements met but has a simple sequence")
if repeated >= 3:
    print("All requirements met but has 3+ repeated characters.")