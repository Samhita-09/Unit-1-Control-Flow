text = input("Enter text:")

# initialize counters
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

# Track first and last characters
first_letter = None
last_letter = None

print(f"Analyzeing: '{text}")
print("=" * 40)

# Process each character
for char in text:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count+=1
        if first_letter is None:
            first_letter = char
        last_letter = char # keep updating (last one wins)
    # count uppercase
    if 'A' <= char <= 'Z':
        uppercase_count+=1
    # count lowercase
    elif 'a' <= char <= 'z':
        lowercase_count+=1
    # count digits
    elif '0' <= char <= '9':
        digit_count+=1
        
print(f"Total Tharacters: {total_chars}")
print(f"Total Letters: {letter_count}")
print(f"Total Digits: {digit_count}")
print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
print(f"First Letter: {first_letter}")
print(f"Last Letter: {last_letter}")