import mastermind_functions as mf
import time

def game_text(num):
    tekst = ["Kies met 1, 2, 3 en 4 welke opties je wilt", "1: Een code kraken, de computer bedenkt"
              " een code en je moet de code van de computer kraken.\n2: een code bedenken, je vult een secret code "
              "in en de computer gokt met verschillende algoritmes naar het antwoord \n3: Spelregels "
              "\n4: Stoppen\nJe kan uit de volgende kleuren kiezen", [*mf.colours],
             "1, Een code kraken\n2, Een code bedenken\n3, Spelregels\n4, Stoppen"]
    return tekst[num]


def main_menu():
    """" Main menu for the given mastermind game. the input is given with int 0/4"""
    ui_choice = ["1", "2", "3"]
    while True:
        print("Mastermind")
        print(game_text(0))
        print(game_text(3))
        input_game = str(input("Keuze:"))
        if input_game == '1':
            game_kraken()
        elif input_game == "2":
            input_game = ""
            print("Kies 1 voor het Simple algorithm, Kies 2 voor het Knuth algorithm, Kies 3 voor het Beginners bias algorithm:")
            while input_game not in ui_choice:
                input_game = str(input("Keuze:"))
            print("Kies uit de volgende kleuren:", *mf.colours)
            secret = input_code()
            if input_game == "1":
                # Start simpel algorithme
                answers = mf.simpel_algorithme(secret)
                show_algorithme_results(answers)
            if input_game == "2":
                # Start worst algorithme
                answers = mf.worst_algorithme(secret)
                show_algorithme_results(answers)
            if input_game == "3":
                # Start human beginners bias algorithme
                answers = mf.heuristiek_human_beginners_bias(secret)
                show_algorithme_results(answers)
        elif input_game == "3":
            print(game_text(1))
            print(*game_text(2), sep=" ")
            time.sleep(5)
        elif input_game == "4":
            break


def input_code():
    """" Loop 5 times and ask for correct inpuf, while the input is not in the colour collection ask for input"""
    colours_list = []
    # Loops 4 tims for the given pin input
    for i in range(1, 5):
        code_input = ""
        # While the given code is not in colours
        while code_input not in mf.colours:
            code_input = input("Pin {}:".format(i))
        colours_list.append(code_input)
    code_list = mf.correct_coller_code(colours_list)
    return code_list


def game_kraken():
    """" While the counter is below 10 ask for input colour and process the guess. Print the amount of colours
    correct and position correct and reduce de counter by 1"""
    code_list = mf.all_possible_answer()
    secret_code = mf.random_code(code_list)
    counter = 10
    print("Kies uit de volgende kleuren:", *mf.colours)
    # While counter is bigger than zero
    while counter > 0:
        print("Nog", counter, "gokken te gaan")
        counter -= 1
        input_guess = input_code()
        position_correct, color_correct = mf.guessing_feedback(secret_code, input_guess)
        if position_correct == 4:
            print("Goed gegokt")
            return
        if counter != 0:
            print("Goede plek:", position_correct)
            print("Correcte kleur:", color_correct)
    print("Game over")


def show_algorithme_results(answers):
    """" Shows the result of playing against the simple algorithm"""
    colours_and_pegs = []
    # For each item in answers
    for item in answers:
        # Change the returned answers data for the print statements 
        colour_string = ""
        for colour in item[0]:
            colour_string += str(mf.colours[colour]) + " "
        colours_and_pegs.append(colour_string)
        correct_position = "Correct position: " + str(item[1][0]) + " Colour correct: " + str(item[1][1])
        colours_and_pegs.append(correct_position)
    for item in colours_and_pegs:
        print(item)
    time.sleep(5)
    return


main_menu()
