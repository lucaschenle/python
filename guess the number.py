
import random

#choose the difficulty level
def set_difficulty():
    """sets the difficulty level"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5

#function to check the answer
def check_answer(guessed_num, answer, turns):
    """checks the answer against the guess. Returns the number of turns remaining"""
    if guessed_num > answer:
        print("Too high.")
        return turns - 1
    elif guessed_num < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#main game function
def game():
    answer = random.randint(1, 100)
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guessed_num = 0

    while turns > 0:
        guessed_num = int(input("Make a guess: "))
        turns = check_answer(guessed_num, answer, turns)
        if turns > 0:
            print(f"You have {turns} attempts remaining to guess the number.")
        else:
            if guessed_num != answer:
                print("You've run out of guesses, you lose.")
            break
game()


