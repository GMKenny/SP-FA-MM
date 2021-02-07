import random
import itertools


colours = ["Rood", "Groen", "Wit", "Zwart", "Blauw", "Geel"]


def correct_coller_code(chosen_colers):
    """"Correct_coler_code loops through every word in the given list and returns a list with the index numbers  """
    colours_nummbers = []
    for item in chosen_colers:
        coler_code = colours.index(item)
        colours_nummbers.append(coler_code)
    return colours_nummbers


def all_possible_answer():
    """"All_possible_answer loops trough every item from 0 t/m 5 and returns a list with tuples with all possible combinations"""
    al_codes = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=4))
    return al_codes


def random_code(lst):
    """Random_code retuns a random code from the given list"""
    code_choice = lst[random.randint(0, (len(lst)-1))]
    return code_choice


def guessing_feedback(secret_code, guess_list):
    """"Given the secret code and guess determine how many colours and positions are correct. Create a list copy of
    the given secret and guess tuples. Loop though the items and determine if the item is the same colour and position,
    if true add one to the correct pins and remove current item form the copy lists.
    Loop trough the items that are left and determine if the guess colours are in the secret code. """
    position_correct = 0
    color_correct = 0
    copy_secret = list(secret_code[:])
    copy_guess = list(guess_list[:])
    for index in range(0, 4):
        if guess_list[index] == secret_code[index]:
            position_correct += 1
            copy_secret.remove(secret_code[index])
            copy_guess.remove(secret_code[index])
    for index in range(0, len(copy_guess)):
        if copy_guess[index] in copy_secret:
            color_correct += 1
            copy_secret.remove(copy_guess[index])
    return position_correct, color_correct


def reduce_code_list(all_possible_list, guess, guess_feedback):
    """Given the list with current possibilities, guess and feedback determine what answers are left.
     Loop trough the every item in the list and determine if the current item would have created the same feedback as the
     current feedback. if true add the item to a new list of codes"""
    current_list = []
    for item in all_possible_list:
        if guessing_feedback(guess, item) == guess_feedback:
            current_list.append(item)
    return current_list


def simpel_algorithme(secret):
    """Given the secret code return list with all decisions made by the computer. Create a list of all possible answers.
    Loop 10 times and create a random guess given the possible answers.
    Receive feedback on the guess and add the guess and feedback in a decision list,
    receive a list of possible answers based on the feedback. if the guess equal to the secret return all decisions"""
    all_possible_list = all_possible_answer()
    all_decisions = []
    for i in range(10):
        guess = random_code(all_possible_list)
        guess_feedback = guessing_feedback(guess, secret)
        all_decisions.append([guess, guess_feedback])
        all_possible_list = reduce_code_list(all_possible_list, guess, guess_feedback)
        if list(guess) == secret:
            break
    return all_decisions






