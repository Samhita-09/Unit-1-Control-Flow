# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = input("Enter student age: ")
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("Student Information:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()

# TODO: Check if age is valid (between 16 and 100)

age_valid = int(age) >= 16 and int(age) <= 100

# TODO: Check if GPA is valid (between 0.0 and 4.0)

gpa_valid = gpa >= 0 and gpa <= 4.0

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)

enrollment = age >= 18 and gpa >= 2.0

# TODO: Check voting eligibility (age >= 18)
can_vote = age >= 18

# TODO: Check honor roll status (gpa >= 3.5)

honor_roll = gpa >= 3.5 and gpa_valid

invalid_input = False

if name == "":
    print("Error: Name cannot be empty")
    invalid_input = True
if age_valid == False:
    print("Error: Age must be a valid number.")
    invalid_input = True
if gpa_valid == False:
    print("Error: GPA must be between 0.0 and 4.0")
    invalid_input = True
if enrollment:
    print("Eligible for Enrollment")
else:
    print("Not eligible for Enrollment")
if can_vote:
    print("Eligible to Vote")
else:
    print("Not eligible to Vote")
if honor_roll:
    print("On Honor Roll")
else:
    print("Not on Honor Roll")
if invalid_input:
    print("Invalid input. Please try again.")