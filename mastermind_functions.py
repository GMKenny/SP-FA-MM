import random
import itertools

# Feedback was dat ik meer notaties moest schrijven bij de functies

colours = ["Rood", "Groen", "Wit", "Zwart", "Blauw", "Geel"]


def correct_coller_code(chosen_colers):
    """"Correct_coler_code loops through every word in the given list and returns a list with the index numbers  """
    # Variable for the colour numbers
    colours_nummbers = []

    # Loop trough the given colours and return the index numbers
    for item in chosen_colers:
        coler_code = colours.index(item)
        colours_nummbers.append(coler_code)
    return colours_nummbers


def all_possible_answer():
    """"All_possible_answer loops trough every item from 0 t/m 5 and returns a list with tuples with all possible combinations"""
    # Create a list of all combinations as tuples
    al_codes = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=4))
    return al_codes


def random_code(lst):
    """Random_code retuns a random code from the given list"""
    # Creates a random number from 0 until te length of te list
    code_choice = lst[random.randint(0, (len(lst)-1))]
    return code_choice


def guessing_feedback(secret_code, guess_list):
    """"Given the secret code and guess determine how many colours and positions are correct. Create a list copy of
    the given secret and guess tuples. Loop though the items and determine if the item is the same colour and position,
    if true add one to the correct pins and remove current item form the copy lists.
    Loop trough the items that are left and determine if the guess colours are in the secret code. """
    # Variables for the black and white feedback pins
    position_correct = 0
    color_correct = 0
    # Copy of the tuple items in list form
    copy_secret = list(secret_code[:])
    copy_guess = list(guess_list[:])

    # For each item in the code
    for index in range(0, 4):
        # If the current guess item is equal to the secret code
        if guess_list[index] == secret_code[index]:
            position_correct += 1
            # Remove items from the copy codes.
            copy_secret.remove(secret_code[index])
            copy_guess.remove(secret_code[index])

    # For each item left in the guess
    for index in range(0, len(copy_guess)):
        # If the current item is equal to the secret code
        if copy_guess[index] in copy_secret:
            color_correct += 1
            # Remove item from list if found
            copy_secret.remove(copy_guess[index])
    return position_correct, color_correct


def reduce_code_list(all_possible_list, guess, guess_feedback):
    """Given the list with current possibilities, guess and feedback determine what answers are left.
     Loop trough the every item in the list and determine if the current item would have created the same feedback as the
     current feedback. if true add the item to a new list of codes"""
    # List for the codes left after sorting
    current_list = []

    # For each item in the list
    for item in all_possible_list:
        # If the feedback for the given item is the same as the guess feedback
        if guessing_feedback(guess, item) == guess_feedback:
            # Add the item to the list.
            current_list.append(item)
    return current_list


def simpel_algorithme(secret):
    """Given the secret code return list with all decisions made by the computer. Create a list of all possible answers.
    Loop 10 times and create a random guess given the possible answers.
    Receive feedback on the guess and add the guess and feedback in a decision list,
    receive a list of possible answers based on the feedback. if the guess equal to the secret return all decisions"""
    # Create a list of all possible answers
    all_possible_list = all_possible_answer()
    # list for all decisions made by the computer
    all_decisions = []
    # For 10 times (amount of guesses allowed)
    for i in range(10):
        # Get a random guess from the given list
        guess = random_code(all_possible_list)
        # Get the feedback from the guess
        guess_feedback = guessing_feedback(guess, secret)
        # Add the guess and feedback to a list for the return values
        all_decisions.append([guess, guess_feedback])
        # reduce the given list
        all_possible_list = reduce_code_list(all_possible_list, guess, guess_feedback)
        # If the item is equal to the secret
        if list(guess) == secret:
            # stop the loop and return all_decisions
            break
    return all_decisions






