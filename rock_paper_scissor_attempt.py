#Rock, paper, or scissors? (r/p/s):

#ask user for input
# if input is not r or p or is Invalid choice!
# make computer choose between 0 and 2, choices = ['r','p','s']
# again
# r beat s but loses to p
# p beat r but loses to s
# s beak p but loses to r

#continue? (y/n):
import random 
flag = False

def determing_winner(user_input, computer_choice):
        if user_input == 'r':
            result = "win" if computer_choice == 's' else "lose"
        elif user_input == 'p':
            result = "win" if computer_choice == 'r' else "lose"
        else:
            result = "win" if computer_choice == 'p' else "lose" 
        return result

def displaying_results(user_input, comptuter_choice, result):
    print("You", result)
    print("You chose", user_input)
    print("Computer chose", computer_choice)   

while True:
    choices = ['r','p','s']
    computer_int = random.randint(0,2)
    computer_choice = choices[computer_int]


    user_input = input('Rock, paper, or scissors? (r/p/s): ')
    if user_input not in ['r','p','s']:
        print("Invalid choice!")
    elif user_input == computer_choice:
        print('Both the same!')
    else:
        result = determing_winner(user_input, computer_choice)
        displaying_results(user_input, computer_choice, result)
      

    #Ask continue after r/p/s       
    while True:
        user_input = input("Continue? (y/n): ")
        if user_input == 'n':
            flag = True
            break
        elif user_input == 'y':
            break
        else:
            print("Invalid input!")

    # User does not want to continue 
    if flag:
        break
        