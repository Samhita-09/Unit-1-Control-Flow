age = input("Enter your age: ")
rating = input("Enter movie rating: ")

# can_watch_G = age and rating == "G"
# can_watch_PG = age >= 6 and rating == "G"
# can_watch_PG13 = age >= 13 and rating == "PG13"
# can_watch_R = age >= 17 and rating == "R"

print(f"Age: {age}, Rating: {rating}")

if age:
    if int(age) and rating == "G":
        print("APPROVED: You can watch this movie!")
    elif int(age) < 6 and rating == "PG":
        print("DENIED: Must be 6+ to watch PG-rated movies.")
    elif int(age) < 13 and rating == "PG13":
        print("DENIED: Must be 13+ to watch PG13-rated movies.")
    elif int(age) < 17 and rating == "R":
        print("DENIED: Must be 17+ to watch R-rated movies.")
    else:
        print("APPROVED: You can watch this movie!")
else:
    print("Please enter a valid age and movie rating!")