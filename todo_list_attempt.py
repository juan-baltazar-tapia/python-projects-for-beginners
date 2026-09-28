#Todo list menu:
# 1. View Tasks
# 2. Add Tasks
# 3. Remove a Task
# 4. Exit

#main function
# loop
# get user input
# if 1 view task()
# if 2 add task() 
# if 3 remove task()
# if 4 break
def get_user_input():
    while True:
        try:
            user_input = int(input("Enter your choice: "))
            if user_input < 1 or user_input > 4:
                print("Invalid choice")
                continue
        except ValueError:
            print("Invalid choice")
            continue
        return user_input

def display_menu():
    print(" ")
    print("Todo List Menu: \n 1. View Tasks \n 2. Add Tasks \n 3. Remove a Task\n 4. Exit")

def view_task(myList):
    if not myList:
        print("No tasks in your list")
        return
    for i in range(len(myList)):
        print(f" {i + 1} {myList[i]}")

def add_task(myList):
    while True:
        user_input = input("Enter new task: ")
        if user_input == '' or user_input == " ":
            print("Invalid task")
            continue
        myList.append(user_input)
        break

def remove_task(myList):
    for i in range(len(myList)):
        print(f"{i+1}. {myList[i]}")
    while True:
        try:
            user_input = int(input("Enter task number: "))
            if user_input < 1 or user_input > len(myList):
                print("Too low or too high")
                continue
        except ValueError:
            print("Invalid input")
        myList.remove(myList[user_input - 1])
        break



def main():
    myList = []
    while True:
        display_menu()
        user_input = get_user_input()
        if user_input == 1:
            view_task(myList)
        elif user_input == 2:
            add_task(myList)
        elif user_input == 3:
            remove_task(myList)
        else:
            break

if __name__ == '__main__':
    main()