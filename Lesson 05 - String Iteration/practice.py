text = "Hello World"
count = 0

# for char in text:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         count+=1
#     elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#         count+=1

# print(count)

vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count+=1

print(count)

text = "ABC123xyz"

for i in range(len(text)):
    if '0' <= text[i] <= '9':
        print(f"Digit at position {i}: {text[i]}")
        
word = "Hello"

for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {-1-i}")