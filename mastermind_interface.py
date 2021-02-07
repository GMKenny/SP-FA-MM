import mastermind_functions as mf

def game_text(num):
    tekst = ["Kies in de main menu welke opties je wilt met 1, 2, 3, 4", "1: Een code kraken, de computer bedenkt"
              " een code en je moet de code van de computer kraken.\n2: een code bedenken, je vult een secret code "
              "in en de computer gokt met verschillende algoritmes naar het antwoord \n3: Spelregels "
              "\n4: Stoppen\nJe kan uit de volgende kleuren kiezen", [*mf.colours],
             "1, Een code kraken\n2, Een code bedenken\n3, Spelregels\n4, Stoppen"]
    return tekst[num]


def main_menu():
    while True:
        print("Mastermind")
        print(game_text(0))
        print(game_text(3))
        input_game = str(input("Keuze:"))
        if input_game == '1':
            game_kraken()
        elif input_game == "2":
            show_simpel_algorithme_results()
        elif input_game == "3":
            print(game_text(1))
            print(*game_text(2), sep=" ")
        elif input_game == "4":
            break


def input_code():
    colours_list = []
    for i in range(1, 5):
        code_input = ""
        while code_input not in mf.colours:
            code_input = input("Pin {}:".format(i))
        colours_list.append(code_input)
    code_list = mf.correct_coller_code(colours_list)
    return code_list


def game_kraken():
    code_list = mf.all_possible_answer()
    secret_code = mf.random_code(code_list)
    counter = 11
    print("Kies uit de volgende kleuren:", *mf.colours)
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


def show_simpel_algorithme_results():
    print("Kies uit de volgende kleuren:", *mf.colours)
    secret = input_code()
    answers = mf.simpel_algorithme(secret)
    colours_and_pegs = []
    for item in answers:
        colour_string = ""
        for colour in item[0]:
            colour_string += str(mf.colours[colour]) + " "
        colours_and_pegs.append(colour_string)
        correct_position = "Correct position: " + str(item[1][0]) + " Colour correct: " + str(item[1][1])
        colours_and_pegs.append(correct_position)
    for item in colours_and_pegs:
        print(item)
    return


main_menu()
