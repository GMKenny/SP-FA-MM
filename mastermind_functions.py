import random
import itertools

# Feedback was dat ik meer notaties moest schrijven bij de functies.

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


def worst_algorithme(secret):
    """Given the secret code return list with all decisions made by the computer. Create a list of all possible answers.
     Create the first guess of the worst algorithm to reduce the list size. receive feedback for given guess.
     Reduce the amount of possible answers with the feedback. Loop 5 times (The maximum needed to solve the the secret),
     for each guess left determine what feedback you would get for all possible secrets and count and add the amount of
     feedback you would get. from the list of counted feedback take the most frequent feedback in the dict and update it
     to a dict. from the dict with the most frequent combination feedback return the item with the least feedback.
     receive feedback from the new guess, if the guess is equal to the secret break the loop and return all decisions,
     else reduce the possible guesses and continue the loop."""

    # list to hold all te decisions made by the computer
    all_decisions = []
    # list with all the possible decisions
    all_possible_list = all_possible_answer()
    # The first guess to reduce the list
    guess = [1, 1, 2, 2]
    # Retrieve the feedback made from the guess
    guess_feedback = guessing_feedback(guess, secret)
    # Reduce the list with all codes with the feedback from the last guess
    code_list = reduce_code_list(all_possible_list, guess, guess_feedback)
    # Add the guess and feedback to the list for the return
    all_decisions.append([guess, guess_feedback])
    # Loop 4 times (The maximum guesses for the worst case 4 + 1)
    for i in range(5):
        # dict for possible answers
        possible_answers = {}
        # For each guess in code list
        for guesses in code_list:
            # dict for al possible feedback
            feedback_container = {}
            for possible_secrets in code_list:
                # receive the possible feedback
                feedback = guessing_feedback(guesses, possible_secrets)
                # If the current feedback is in the dict add 1 else create a new feedback with 1
                if feedback in feedback_container:
                    feedback_container[feedback] += 1
                else:
                    feedback_container[feedback] = 1
            # Add to the dictionary the guess with the maximum value of feedback
            possible_answers[guesses] = max(feedback_container.values())
        # Retrieve the least worst case from the dict (Lambda is required to retrieve from dict with min)
        possible_answers = min(possible_answers.keys(), key=(lambda key: possible_answers[key]))
        # Retrieve the feedback from the guess
        guess_feedback = guessing_feedback(possible_answers, secret)
        # Add the guess and feedback to the list for the return
        all_decisions.append([possible_answers, guess_feedback])
        # Break the range loop of the possible_answers is equeal to the secret
        if list(possible_answers) == secret:
            break
        # Reduce the list with guesses left with the feedback from the last guess
        code_list = reduce_code_list(code_list, possible_answers, guess_feedback)
    return all_decisions


def heuristiek_human_beginners_bias(secret):
    """Side node: This algorithm is based upon given results received from 5 people who never played mastermind before.
       Given the question: What secret number would you create, the question repeated 10 times each.
       the conclusion of the results where the following statements:
        1. A average beginner for at least 5 rounds would never create a secret with multiple of the same colour.
        2. A average beginner will start to guess 2 of the same colours after 5 rounds but never next to each other.
        3. A average beginner would not place the same colour next to each other
        4. A average beginner would not place multiple of the same colour
        This algorithm is created to play against beginners once figured out this algorithm wil be easy to beat"""

    """Given the secret code return a list with all decisions made by the computer. Create a variable with all  
      possible answers and create a copy of the list to hold the most common codes. Loop trough the possible codes and 
      remove and append to another list x based upon the statements 1, 2, 3 and 4. As long as the most common codes 
      list is not empty and the amount of guesses is not below 0. Guess a random code from the list until the list 
      is empty. if the list is empty but the secret was not found use list x and repeat until the secrets is found or 
      the amount of turn has expired."""
    # Create a list with all possible answers.
    all_possible_list = all_possible_answer()
    # Create a copy of the list.
    all_possible_list_copy = all_possible_list.copy()
    # Create a list for codes not anticipated by beginners.
    above_average_codes = []
    # Create a list for.
    all_decisions = []
    # For each item in all possible codes.
    for item in all_possible_list:
        # for range until index 2.
        for num in range(3):
            # if the item is the same as its neighbour.
            if item.count(item[num]) > 2 or item[num] == item[num+1] or item[0] == item[2] and item[1] == item[3]:
                # Remove the code from the copy list.
                all_possible_list_copy.remove(item)
                # Add the item to the above average codes list.
                above_average_codes.append(item)
                break
    # Keep track of the maximum amount of turns.
    turn_counter = 10
    # While there are still codes in the predicted list and the turn counter is not 0.
    while len(all_possible_list_copy) > 0 and turn_counter > 0:
        # Guess a random item from the copy list and receive feedback and reduce the list based upon the feedback.
        all_decisions, all_possible_list_copy, guess = heuristiek_sub(all_possible_list_copy, secret, all_decisions)
        # Minus 1 turn counter.
        turn_counter -= 1
        # If the guess is equal to the secret.
        if list(guess) == secret:
            # Return the list with all decisions.
            return all_decisions
    # While the counter is not below zero but the secret was not found. (algorithm fail save).
    while turn_counter > 0:
        # Guess a random item from the above average list and receive feedback and reduce the list based upon the feedback.
        all_decisions, above_average_codes, guess = heuristiek_sub(above_average_codes, secret, all_decisions)
        # Minus 1 turn counter.
        turn_counter -= 1
        # If the guess is equal to the secret.
        if list(guess) == secret:
            # Return the list with all decisions.
            return all_decisions

def heuristiek_sub(code_list, secret, all_decisions):
    """Sub function for human beginners bias. Given the code list, secret and list of all decisions return a list with
     decisions the reduced code list and current guess"""
    # Get a random code from the code list.
    guess = random_code(code_list)
    # Retrieve feedback.
    guess_feedback = guessing_feedback(guess, secret)
    # Add the guess and feedback to the list with all decisions.
    all_decisions.append([guess, guess_feedback])
    # Reduce the code list based on the feedback.
    code_list = reduce_code_list(code_list, guess, guess_feedback)
    # return all decisions, code list and guess.
    return all_decisions, code_list, guess


