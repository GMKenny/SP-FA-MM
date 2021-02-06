import random
import itertools


kleuren = ["Rood", "Groen", "Wit", "Zwart", "Blauw", "Geel"]


def correct_coller_code(colers):
    coler_nummbers = []
    for item in colers:
        coler_code = kleuren.index(item)
        coler_nummbers.append(coler_code)
    return coler_nummbers


def all_possible_answer():
    al_codes = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=4))
    return al_codes


def random_code(lst):
    code_choice = lst[random.randint(0, (len(lst)-1))]
    return code_choice


def guessing_feedback(secret_code, guess_list):
    position_correct = 0
    color_correct = 0
    # Zonder copy word er 1 een color bij opgeteld of vergeten als dat niet moet.
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


def simpel_algorithme(secret):
    all_possible_list = all_possible_answer()
    all_decisions = []
    for i in range(10):
        guess = random_code(all_possible_list)
        guess_feedback = guessing_feedback(guess, secret)
        all_decisions.append([guess, guess_feedback])
        current_list = []
        for item in all_possible_list:
            if guessing_feedback(guess, item) == guess_feedback:
                current_list.append(item)
        all_possible_list = current_list
        if list(guess) == secret:
            break
    return all_decisions






