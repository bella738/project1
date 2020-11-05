import os


SCORES_FILE_NAME = "/Users/bellamarkovitz/Documents/devops/project 1/Score.txt"
BAD_RETURN_CODE = "Something went wrong.."

def screen_cleaner(): #cleaning the screen
    os.system('cls' if os.name == 'nt' else 'clear')

