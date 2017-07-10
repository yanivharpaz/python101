
list_choice = ['R', 'P', 'S', 'r', 'p', 's']

list_results = []

player_1 = raw_input("Pleas enter your name:\n")
player_2 = raw_input("Pleas enter your name:\n")

print ("hello players {} and {}".format(player_1, player_2))

choice_player_1 = raw_input("{} Pleas enter your choice: R - Rock, P - Paper or S - Scissors\n".format(player_1))

for num_game in range(2):
    while choice_player_1 not in list_choice:
        choice_player_1 = raw_input("{} Pleas enter legitimate choice: R - Rock, P - Paper or S - Scissors\n".format(player_1))

    choice_player_2 = raw_input("{} Pleas enter your choice: R - Rock, P - Paper or S - Scissors\n".format(player_2))

    while choice_player_2 not in list_choice:
        choice_player_2 = raw_input("{} Pleas enter legitimate choice: R - Rock, P - Paper or S - Scissors\n".format(player_2))

    if choice_player_1 == choice_player_2:
        list_results.append('No one')

    elif choice_player_1.lower() == 'r' and choice_player_2.lower() == 's':
        res = (num_game, player_1, choice_player_1, choice_player_2)
        list_results.append(res)

    elif choice_player_1.lower() == 'r' and choice_player_2.lower() == 'p':
        res = (num_game, player_2, choice_player_1, choice_player_2)
        list_results.append(res)

    elif choice_player_1.lower() == 'p' and choice_player_2.lower() == 's':
        res = (num_game, player_2, choice_player_1, choice_player_2)
        list_results.append(res)

    elif choice_player_1.lower() == 'p' and choice_player_2.lower() == 'r':
        res = (num_game, player_1, choice_player_1, choice_player_2)
        list_results.append(res)

    elif choice_player_1.lower() == 's' and choice_player_2.lower() == 'r':
        res = (num_game, player_2, choice_player_1, choice_player_2)
        list_results.append(res)

    elif choice_player_1.lower() == 's' and choice_player_2.lower() == 'p':
        res = (num_game, player_1, choice_player_1, choice_player_2)
        list_results.append(res)


for winner in list_results:
    print("Round {0} : {1} won - {4} had {2} and {5} had {3}".format(winner[0], winner[1], winner[2], winner[3], player_1, player_2))
