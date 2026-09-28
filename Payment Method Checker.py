# 1. Payment Method Checker

method = ("GCash", "Cash", "Card")

pmethod = str(input("Enter payment method: "))

if pmethod in method:
    print("Valid payment method.")
else:
    print("Invalid payment method.")