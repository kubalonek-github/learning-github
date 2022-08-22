# -------IMPORT_SECTION---------

from quiz_config import Questions,Options,Other
import math

# ---------QUESTIONS------------

questions = Questions.questions

# ----------OPTIONS------------

options = Options.options

# -----------OTHER-------------

line = Other.dashes
empty = Other.empty
quiz_title = Other.quiz_title
results_top = Other.results_top
correct_message = Other.correct_message
incorrect_message = Other.incorrect_message
win_message = Other.win_message
lose_message = Other.lose_message
goodbye_message = Other.goodbye_message

# -----------CODE--------------

def goodbye():
    print("Cya!")

def new_Game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(empty)
        print(line)
        print(key)
        print(line)
        for i in options[question_num-1]:
            print(i)
        print(line)
        guess = input("").upper()
        if questions[key]==guess:
            question_num += 1
            correct_guesses += 1
            guesses.append(guess)
            print(empty)
            print("Correct!")
        else:
            print(empty)
            print("Incorrect :<")
            question_num += 1
            guesses.append(guess)
    if len(questions)<question_num:
        print("")
        print(line)
        print(results_top)
        print(line)
        print("Your Answears: "+ str(guesses)[1:-1])
        cor_ans = str(questions.values())[11:]
        print("Correct Answears: " + cor_ans[2:-2])
        print(line)
        correct_percent = math.floor(float(correct_guesses/len(questions))*100)
        print(str(correct_percent) + "% Correct " + "[" + str(correct_guesses) + "/" + str(len(questions)) + "]")
        print(line)
        if correct_percent==100:
            print(win_message)
            print(line)
        else:
            print(lose_message)
        player_choice = input("Do you want play again? (yes or no) ").lower()
        if player_choice=="yes":
            new_Game()
        else:
            goodbye()

print("Please press enter key under this message to start quiz")
op = input(empty)
if op=="":
    print(quiz_title)
    new_Game()
else:
    print("Bruh")
    print(empty)
    print(quiz_title)
    new_Game()