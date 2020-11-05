import GuessGame
import MemoryGame
import Score
from Utils import BAD_RETURN_CODE


def wellcome(): #getting user name
    name = input("Please Enter Your Name")
    print("Hello",name, "and welcome to the World of Games (WoG).\nHere you can find many cool games to play")

def load_game(): # user choose game and difficulty
    game_to_play = int(input("Please choose a game to play: \n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n2. Guess Game - guess a number and see if you chose like the computer"))
    difficulty = int(input("Please choose game difficulty from 1 to 5:"))
    # calling the games
    if game_to_play == 1:
        result = MemoryGame.play(difficulty)

    elif game_to_play == 2:
        result = GuessGame.play(difficulty)
    else:print(BAD_RETURN_CODE)
    # wright score to score.txt
    if result == True:
        Score.add_score(difficulty)






