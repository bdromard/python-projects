import random

ALLOWED_COLORS = ["blue", "yellow", "green", "red", "purple", "grey", "orange", "pink", "brown"]
CODE_TO_GUESS = ["blue", "blue", "yellow", "green"]
code_to_guess_random = random.sample(ALLOWED_COLORS, 4)
player_guesses = []
number_of_tries = 12
player_victory = False

while number_of_tries <= 12 and not player_victory:
    print(code_to_guess_random)
    player_input = input(f"Devinez la combinaison de deux couleurs ! "
                         f"Les couleurs autorisées sont {', '.join(ALLOWED_COLORS)} : ").lower()
    if player_input not in ALLOWED_COLORS:
        print("Cette couleur n'est pas autorisée !")
    elif player_input in ALLOWED_COLORS and player_input in code_to_guess_random:
        number_of_tries -= 1
        player_guesses.append(player_input)
        print(f"{player_input} est bien dans le code à deviner !")
        if len(player_guesses) == len(CODE_TO_GUESS):
            player_victory = True
            print(f"Bravo, vous avez deviné le code ! Il s'agissait de {', '.join(CODE_TO_GUESS)}")
    else:
        number_of_tries -= 1
        print(f"{player_input} n'est pas dans le code à deviner. Proposez une autre couleur parmi {ALLOWED_COLORS}")


pass
