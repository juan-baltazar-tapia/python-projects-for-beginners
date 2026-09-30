# bulls correct digit in correct place
# cows correct digit

# CREATE NUMBER with unique digits (set and random)
# Get user input:
#    validate
# count which digits are in correct place
# count which digits show up in number
# print cows and bulls
import random


DIGIT_LENGTH = 4


def generate_number():
    return "".join(random.sample("0123456789", DIGIT_LENGTH))


def user_input_is_unique(user_input):
    return len(set(user_input)) == len(user_input)


def get_user_input():
    while True:
        user_input = input("Guess: ")
        if (
            not user_input_is_unique(user_input)
            or len(user_input) != DIGIT_LENGTH
            or not user_input.isdigit()
        ):
            print("Invalid number!")
        else:
            return user_input


def get_cows_bulls(user_input, digit):
    bulls = sum([1 for i in range(DIGIT_LENGTH) if user_input[i] == digit[i]])
    cows = sum([1 for i in range(DIGIT_LENGTH) if user_input[i] in digit]) - bulls

    return [cows, bulls]


def main():
    digit = generate_number()
    print(
        f"I have generated a {DIGIT_LENGTH}-digit number with unique digits. Try to guess it!"
    )
    print(digit)
    while True:
        user_input = get_user_input()
        if digit == user_input:
            print("Congratulations you have guessed the correct number!")
            break
        cows, bulls = get_cows_bulls(user_input, digit)
        print(f"{cows} cows, {bulls} bulls")


if __name__ == "__main__":
    main()
