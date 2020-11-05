
import Score
import random
def generate_number(difficulty): #generating a number according to "difficulty"
    secret_number = random.randint(1,difficulty)
    return str (secret_number)

in1 = "guess a number between 1 to "

def get_guess_from_user(difficulty):# getting a number from user
    guess_number = input(in1+str(difficulty))
    return guess_number


def compare_results(user_number, secret_number):# comparing between computer number and user number
    if secret_number == user_number:
        print('True')
        return True
    else:
        print("False")
        return False


def play(difficulty):#calling the function above
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    return compare_results(user_number,secret_number)



