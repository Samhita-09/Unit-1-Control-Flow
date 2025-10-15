print("\n" + "=" * 50)
print("EXAMPLE 5: Centered Asterisk Pyramid")
print("=" * 50)

'''
    *
   ***
  *****
 *******
*********
'''

rows = 5

# step 1 - create an outer loop for the rows
for i in range(rows):
    # step 2 - print the spaces (rows - i - 1)
    for j in range(rows - i - 1):
        print(" ", end="")
    # step 3 - print the stars (2 * i + 1)
    for k in range(2 * i + 1):
        print("*", end="")
    # step 4 - print a new line
    print()