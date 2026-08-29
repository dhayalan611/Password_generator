print("="*40)
print("\tPASSWORD STRENGTH CHECKER")
print("="*40)

special_charactors = "!@#$%^&*():;,.{=-_}[]?/|"
score = 0
strength = ""
suggestions = []


password = input("\nEnter a password to check: ")

if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")



has_lower = any(char.islower() for char in password)
if has_lower:
    score += 1
else:
    suggestions.append("Add lowercase letters")


has_upper = any(char.isupper() for char in password)
if has_upper:
    score += 1
else:
    suggestions.append("Add uppercase letters")


has_digit = any(char.isdigit() for char in password)
if has_digit:
    score += 1
else:
    suggestions.append("Add numbers")


has_specialChar = any(char in special_charactors for char in password)
if has_specialChar: 
    score += 1
else:
    suggestions.append("Add special characters")



if score <= 2:
    strength = "WEAK"

elif score <= 4:
    strength = "MEADIUM"

else:
    strength = "STRONG"


print("\n","="*40)

print(f"\n\tScore: {score}/5")
print(f"\tStrength: {strength}")

print("\n","="*40)

if suggestions:
    print("\nSuggestions:")

    for suggestion in suggestions:
        print("-",suggestion)

else:
    print("\nYour password meets all security requirements!")

print("="*40)