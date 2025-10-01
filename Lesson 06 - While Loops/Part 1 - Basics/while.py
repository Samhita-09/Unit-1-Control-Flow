# Syntax:
'''
initialize variable

while condition(test variable):
    code block
    increment/decrement
''' 

num = 5

while num >= 1:
    print(num)
    num-=1
    
print("Blast off!🚀")

# Sum 1 - 10

num = 1
sum = 0

# while num < 11:
#     sum += num
#     num += 1
    
# print(f"Sum of numbers 1-10: {sum}")

while num < 11:
    sum += num
    if num < 10:
        print(num, end="+")
    else:
        print(num, end="=")
    num += 1

print(sum)

# Sum of digits
# take a user input as int, and sum the digits of it

userNum = input("Enter a number: ") # 1234
sum = 0

# for char in userNum:
#     print(f"{char} {type(char)}")
#     sum += int(char)

# print(sum)

i = 0

while i < len(userNum):
    sum += int(userNum[i])
    i += 1
    
print(f"Total: {sum}")