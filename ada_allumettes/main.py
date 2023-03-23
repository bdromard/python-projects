total_matches = 50
is_game_on = True


def remove_matches(matches_to_remove):
    global total_matches
    total_matches = total_matches - matches_to_remove
    return total_matches


def player_choice():
    global total_matches, is_game_on
    player_input = int(input("Combien d'allumettes voulez-vous retirer ? Choisissez entre 1 et 6 : "))
    if total_matches == 0:
        is_game_on = False
        print("Vous avez gagné !")
    elif player_input >= 1 and player_input <= 6:
        new_total = remove_matches(player_input)
        if new_total == 0:
            is_game_on = False
            print("Vous avez gagné !")
        else:
            print(new_total)
    else:
        print("Mauvais choix !")


while is_game_on:
    player_choice()
