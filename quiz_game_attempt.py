# What is the capital of France? A. Berlin B. Madrid C. Paris D. Rome
# Your answer: c
# If correct, correct! (green text)
# If incorrect, Wrong! The answer is {correct answer}
# Quiz over! Your final score is # out of #.

from termcolor import colored, cprint

QUESTIONS = [
["What is the capital of France?", ["Berlin","Madrid","Paris","Rome"]],
["Which Planet is Known as the Red Planet?", ["Mars","Earth","Jupiter","Saturn"]],
["What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"]]
]

ANSWERS = ["Paris","Mars","Pacific"]
LETTERS = ["A","B","C","D"]
RIGHT_ANSWERS = {
    "What is the capital of France?":"Paris",
    "Which Planet is Known as the Red Planet?":"Mars",
    "What is the largest ocean on Earth?":"Pacific"
}

SCORE = 0

def ask_question():
    for i in range(len(QUESTIONS)):
        print(f"Question {i + 1}: {QUESTIONS[i][0]}")
        for j in range(len(QUESTIONS[i][1])):
            print(f"{LETTERS[j]}. {QUESTIONS[i][1][j]}")
        user_input = get_user_answer()
        response = QUESTIONS[i][1][ord(user_input) - 97]
        display_answer(response, QUESTIONS[i][0], i)
    return

def display_answer(user_response, question, index):
    global SCORE
    if RIGHT_ANSWERS[question] == user_response:
        text = colored("Correct!", "green")
        print(text)
        SCORE += 1
    else:
        letter = LETTERS[find_index(question, RIGHT_ANSWERS[question], index)]
        text = colored(f"Wrong! The correct answer is {letter}", "red")
        print(text)

def find_index(question, correct_response, index):
    print("question: ", question, "coreect response: ", correct_response)

    for i in range(len(QUESTIONS[index][1])):
        if QUESTIONS[index][1][i] == correct_response:
            return i
        

def get_user_answer():
    while True:
        user_input = input("Your answer: ").lower()
        if user_input not in ('a','b','c','d'):
            print("Type a, b , c, or d")
            continue
        return user_input

def display_score():
    print(f"SCORE {SCORE}/{len(QUESTIONS)}")
    return

def main():
    ask_question()
    display_score()

if __name__ == '__main__':
    main()



