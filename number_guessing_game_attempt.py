#guess the number between 1 and 100
#Please enter a valid number
import random 

number = random.randint(1,100)

while True:
    user_number = input('Guess the number between 1 and 100: ')
    try:
        int(user_number)
        user_number = int(user_number)
        if user_number > 100 or user_number < 1:
            print('Out of range')
        elif user_number > number:
            print('Too high!')
        elif user_number < number:
            print('Too low!')
        else:
            print('Congratulations you guessed the number!:', number)
            break
    except:
        print('Please enter a valid number')

