# 2. Grade Checker

grade = int(input("Enter your grade: "))

if grade > 0 and grade <= 100:
    print("Valid grade.")
else:
    print("Invalid grade. Grade must be between 0 and 100.")