height = input("Enter your hight (in): ")
weight = input("Enter your weight (lbs): ")

BMI = (int(weight) / (int(height)*int(height))) * 703

category = ("Underweight" if BMI < 18.5 else
            "Normal" if 18.5 <= BMI < 25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese"
           )

print(f"Weight: {weight}, Height: {height}, BMI: {BMI}, Category: {category}")