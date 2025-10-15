n = 5
o = n - 2

for i in range(n):
    if i == 0 or i == n-1:
        print("x" * n)
    else:
        print("x" + ("o" * o) + "x")
        
        
# Alternative way - using nested loops

safe = 0

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n-1:
            print("x", end=" ")
        else:
            print("o", end=" ")
            safe += 1
    print()
    
print(f"Safe: {safe}")