# 5. Student Score Entry

try:
    score = int(input("Enter examination score: "))
    if score >= 0 and score <= 100:
        print("Valid score.")
    else:
        print("Invalid score. Score must be between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter a number.")