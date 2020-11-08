import os


SCORES_FILE_NAME = "./Score.txt"
BAD_RETURN_CODE = "Something went wrong.."

def screen_cleaner(): #cleaning the screen
    os.system('cls' if os.name == 'nt' else 'clear')

