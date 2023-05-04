#import art and game data from py files
from art import logo, vs
from game_data import data

# import random module
import random

#clear screen function
def clear(score = None):
    print("\033c", end="")
    print("\033[H\033[J")

#main game function
def game(score = 0, previous_data1 = None, previous_data2 = None):
    clear()
    print(logo)
    if score == 0:
        print("Welcome to the game!")
    else:
        print(f"You're right! Current score: {score}.")
    #randomly select one set of data from game_data.py, if previous_data1 is not None, data1 = previous_data2
    if previous_data1 is None:
        data1 = random.choice(data)
    else:
        data1 = previous_data2
    #randomly select one set of data from game_data.py
    data2 = random.choice(data)


    #check if data1 and data2 are the same
    while data1 == data2:
        data2 = random.choice(data)
    #print data1
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
    #print vs
    print(vs)
    #print data2
    print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}.")
    #ask user to guess which data has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #compare the follower number from the two set of data

    #correct answer is equal to the bigger one
    if data1['follower_count'] > data2['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'


    #compare their answer with the correct answer
    #check if user's guess is correct, if true, score += 1,  make correct answer data1, repeat the game
    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
        game(score, data1, data2)

    #if false, print("Sorry, that's wrong. Final score: {score}") then clear screen
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        
        



game()