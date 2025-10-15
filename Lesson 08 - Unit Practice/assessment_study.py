# Example 1

n = 5
safe = 0

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("X", end=" ")
        else:
            print("O", end=" ")
            safe += 1 # remember this goes here, not in if
    print() # REMEMBER THIS!!!
        
print(f"Safe: {safe}")

# Example 2

months = 0
total = 0

while True:
    cost = int(input("Enter monthly cost: "))
    if cost == -1:
        break
    elif cost <= 5 or cost >= 50:
        print("Please enter a cost between 5 and 50.")
    else:
        months += 1
        total += cost

print(f"Months: {months}")
print(f"Total: ${total}")

# Example 3

password = input("Enter a password to check its strength: ")

passwordLen = True
has_uppercase = False
has_lowercase = False
has_digit = 0
strength = "Weak"

if len(password) < 8 or len(password) > 16:
    print("Please make sure password has 8-16 letters.")
    passwordLen = False
for char in password:
    if 'A' <= char <= 'Z':
        has_uppercase = True
    elif 'a' <= char <= 'z':
        has_lowercase = True
    elif '0' <= char <= '9':
        has_digit += 1
if has_uppercase and has_lowercase and has_digit >= 2 and passwordLen:
    strength = "Strong"
else:
    strength = "Weak"
    
print(f"Password: {password}")
print(f"Strength: {strength}")

# Example 4
total = 0

for squad in range(3):
    for player in range(4):
        total += 1
        if total >= 10:
            break
print(total)