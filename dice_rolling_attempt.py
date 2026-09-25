import random

user_input = ''
user_input = input("Roll the dice? (y/n): ").lower()
while user_input != 'n':
    if user_input != 'y':
        print("Invalid Choice!")
    else:
        print("ran")
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print([num1, num2])
    print("Roll the dice? (y/n): ")
    user_input = input()