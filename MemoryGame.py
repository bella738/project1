import random
import time
import Utils
import Score
def generate_sequence(difficulty): # generate a number according to "difficulty" and represent it to the user for 0.7 seconds
    random_list = []
    for i in range(0,difficulty):
        random_list.append(random.randint(1,101))
#    print(random_list)
    time.sleep(0.7)
    Utils.screen_cleaner()
    return random_list

def get_list_from_user(difficulty):# the user has to wright the numbers he saw
    listA= []
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter")
    for i in range(0, difficulty):
        print("No-{}: ".format(i + 1))
        elment = int(input())
        listA.append(elment)
    return listA

def is_list_equal(list_a,list_b): # comparing between the computer list and the user list
    if list_a == list_b:
        print(True)
        return True
    else:
        print(False)
        return False

def play(difficulty): # calling the function above
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    return is_list_equal(list_a,list_b)



