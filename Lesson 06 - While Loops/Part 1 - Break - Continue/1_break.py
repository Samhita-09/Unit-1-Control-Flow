# Break statement in loops
# Break - Exits the loop immediately
# Use Case
'''
*STOP when you find something
*EXIT early based on a condition
*GET OUT of infinite loop
'''

count = 1

while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1
    
    
while True:
    choice = input("Enter something (q for quit): ")
    if choice == "q":
        print("You wanted to exit!")
        break
    print(f"You entered {choice}")
    
# Find first divisor
n = int(input("Enter a number: "))
divisor = 2

while divisor < n:
    if n % divisor == 0:
        break
    divisor += 1
    
print(f"{n} is divisible by {divisor}.")