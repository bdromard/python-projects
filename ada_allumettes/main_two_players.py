total_matches = 50
is_game_on = True


def remove_matches(matches_to_remove):
    global total_matches
    total_matches = total_matches - matches_to_remove
    return total_matches


def players_choice(player):
    global total_matches, is_game_on
    if player == 1:
        player_input_one = int(input("Joueur 1, combien d'allumettes voulez-vous retirer ? Choisissez entre 1 et 6 : "))
        if player_input_one >= 1 and player_input_one <= 6:
            new_total = remove_matches(player_input_one)
            if new_total == 0:
                is_game_on = False
                print("Joueur 1, vous avez gagné !")
            else:
                print(new_total)
    elif player == 2:
        player_input_two = int(input("Joueur 2, combien d'allumettes voulez-vous retirer ? Choisissez entre 1 et 6 : "))
        if player_input_two >= 1 and player_input_two <= 6 and is_game_on:
            new_total = remove_matches(player_input_two)
            if new_total == 0:
                is_game_on = False
                print("Joueur 2, vous avez gagné !")
            else:
                print(new_total)
    else:
        is_game_on = False
        print("Mauvais choix !")


while is_game_on:
    players_choice(1)
    players_choice(2)
