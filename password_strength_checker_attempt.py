# RULES
# if numbers and less than 8 characters, very weak
# if contains lower case letters weak
# if contains uppercase and greater than 8 medium
# if contains lowercase, uppercase strong, more than 8 strong
# if contains lowercase, uppercase, special character, more than 8, very strong
#
import re


def calculate_strength(password):
    total_score = 0

    if len(password) >= 8:
        total_score += 1
    if bool(re.search(r"[a-z]", password)):
        total_score += 1
    if bool(re.search(r"[0-9]", password)):
        total_score += 1
    if bool(re.search(r"[A-Z]", password)):
        total_score += 1
    if bool(re.search(r"[^A-Za-z0-9\s]", password)):
        total_score += 1

    match total_score:
        case 1:
            return "Very Weak"
        case 2:
            return "Weak"
        case 3:
            return "Medium"
        case 4:
            return "Strong"
        case 5:
            return "Very Strong"


def main():
    while True:
        user_input = input("Enter a password (q to quit): ").strip()
        if user_input == "q":
            break
        print(f"Password strength: {calculate_strength(user_input)}")


if __name__ == "__main__":
    main()
