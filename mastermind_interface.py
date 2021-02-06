import mastermind_functions as mf

def game_text(num):
    rules = ["Kies in de main menu welke optie je wilt met 1, 2, 3, 4\nInput 1: Een code kraken, de computer bedenkt"
              "een code en je moet de code van de computer kraken\nInput 2: een code bedenken, je vult een secret code "
              "in en de computer gokt met verschilende algoritmes naar het antwoord \nInput 3: Spelregels "
              "\nInput 4: Stoppen\nJe kan uit de volgende kleuren kiezen\n", *mf.kleuren]
    return print(rules[num])


def main_menu():
    while True:
        print("Mastermind")
        print("1, Een code kraken", "\n2, Een code bedenken", "\n3, Spelregels", "\n4, Stoppen")
        input_game = str(input())
        if input_game == '1':
            game_kraken()
        elif input_game == "2":
            return
        elif input_game == "3":
            game_text(0)
            game_text(1)
            return
        elif input_game == "4":
            break


def input_code():
    coler_list = []
    for i in range(1, 5):
        code_input = ""
        while code_input not in mf.kleuren:
            code_input = input("Pin {}:".format(i))
        coler_list.append(code_input)
    code_list = mf.correct_coller_code(coler_list)
    return code_list


def game_kraken():
    code_list = mf.all_possible_answer()
    secret_code = mf.random_code(code_list)
    counter = 11
    print("Kies uit de volgende kleuren:", *mf.kleuren)
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


main_menu()
