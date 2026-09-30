# Enter password length
# include upper?
# numbers?
# special characters

# Ask for password length (must be > 7) check
# Ask for upper?
# Ask for numbers?
# Ask for special char?
# store total asked for
# make random string of size N containng all lower case letters
# if upper replace (1-(size/4) with upper)
# if numebrs replace (1-(size/4) with numbers)
# if special replace (1-(size/4) with special)
import random
import string
import math
import secrets


def get_user_input():
    while True:
        try:
            user_input = int(input("Enter password length: "))
            if user_input < 8:
                print("Length must be at least 8")
                continue
            else:
                break
        except ValueError:
            print("Enter valid number!")
    return user_input


def get_user_option(option):
    while True:
        user_input = input(f"Include {option} (y/n): ").lower()
        if user_input == "y" or user_input == "yes":
            return True
        elif user_input == "n" or user_input == "no":
            return False
        else:
            print("Invalid response! ")


def get_user_options():
    choice = [False, False, False]
    options = ["upper case letters", "digits", "special characters"]

    for i in range(len(options)):
        choice[i] = get_user_option(options[i])

    return choice


def make_password(length, options):
    choices = 0
    for option in options:
        if option == True:
            choices += 1

    password = "".join(secrets.choices(string.ascii_lowercase, k=length))

    # choose random # of indexes for each chosen option
    indices = []
    taken_indices = set()
    for i in range(len(options)):
        number_of_indices = random.randint(1, math.floor(length / 4))

        curr = []
        for i in range(number_of_indices):
            while True:
                number = random.randint(1, length - 1)
                if number not in taken_indices:
                    curr.append(number)
                    taken_indices.add(number)
                    break
        indices.append(curr)

    if options[0]:
        for i in range(len(indices[0])):
            password = replace_at(
                password, indices[0][i], secrets.choice(string.ascii_uppercase)
            )
    if options[1]:
        for i in range(len(indices[1])):
            password = replace_at(password, indices[1][i], secrets.choice(string.digits))
    if options[2]:
        for i in range(len(indices[2])):
            password = replace_at(
                password, indices[2][i], secrets.choice(string.punctuation)
            )

    return password


def replace_at(s, index, char):
    return s[:index] + char + s[index + 1 :]


def main():
    length = get_user_input()
    options = get_user_options()
    print(make_password(length, options))


if __name__ == "__main__":
    main()
