# Grading a student based on their score

score = int(input("Please Enter the score : "))

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

elif score >= 60:
    grade = "D"

else:
    grade = "Fail"

print("Your Grade is : ", grade)
