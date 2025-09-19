age = int(input("Enter your age: "))
rating = input("Enter movie rating: ")

# can_watch_G = age and rating == "G"
# can_watch_PG = age >= 6 and rating == "G"
# can_watch_PG13 = age >= 13 and rating == "PG13"
# can_watch_R = age >= 17 and rating == "R"

print(f"Age: {age}, Rating: {rating}")

if age:
    if age and rating == "G":
        print("APPROVED: You can watch this movie!")
    else:
        print("DENIED: Not approved for your age.")
    if age >= 6 and rating == "PG":
        print("APPROVED: You can watch this movie!")
    else:
        print("DENIED: Not approved for your age.")
    if age >= 13 and rating == "PG13":
        print("APPROVED: You can watch this movie!")
    else:
        print("DENIED: Not approved for your age.")
    if age >= 17 and rating == "R":
        print("APPROVED: You can watch this movie!")
    else:
        print("DENIED: Not approved for your age.")
else:
    print("Please enter a valid age and movie rating!")