height = input("Enter your hight (in): ")
weight = input("Enter your weight (lbs): ")

BMI = (int(weight) / (int(height)*int(height))) * 703

category = ("Underweight" if BMI < 18.5 else
            "Normal" if 18.5 <= BMI < 25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese"
           )

recommendation = ("Maintain Weight" if category == "Normal" else
        "Gain weight" if category == "Underweight" else
        "Lose weight" if category == "Overweight" else
        "Lose Weight"
        )

risk = ("Low" if category == "Normal" else
        "Moderate" if category == "Overweight" else
        "High" if category == "Obese" else
        "Moderate-High"
        )

print(f"Height: {height} in.")
print(f"Weight: {weight} lbs")
print(f"BMI: {BMI}")
print(f"Category: {category}")
print(f"Recommendation: {recommendation}")
print(f"Health Risk: {risk}")