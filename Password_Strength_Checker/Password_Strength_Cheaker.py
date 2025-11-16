# A strong password must contain:

# Minimum 8 chars

# Uppercase

# Lowercase

# Number

# Special character



import re

def check_password(pwd):
    strength = 0
    remarks = []

    if len(pwd) >= 8:
        strength += 1
    else:
        remarks.append("Minimum 8 characters needed")

    if re.search("[A-Z]", pwd):
        strength += 1
    else:
        remarks.append("Add at least 1 uppercase letter")

    if re.search("[a-z]", pwd):
        strength += 1
    else:
        remarks.append("Add at least 1 lowercase letter")

    if re.search("[0-9]", pwd):
        strength += 1
    else:
        remarks.append("Add at least 1 digit")

    if re.search("[@#$%^&*]", pwd):
        strength += 1
    else:
        remarks.append("Add at least 1 special character (@#$%^&*)")

    level = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]

    print("\nPassword Strength:", level[strength])
    if remarks:
        print("Suggestions:")
        for r in remarks:
            print("-", r)

# Run
pwd = input("Enter password: ")
check_password(pwd)
