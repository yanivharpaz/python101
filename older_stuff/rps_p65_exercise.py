

list_choice = ['R', 'P', 'S', 'r', 'p', 's']

game_results_history = []
players_info = dict()

players_info[0] = "No one"
players_info[1] = raw_input("Player 1: Please enter your name ===> ")
players_info[2] = raw_input("Player 2: Please enter your name ===> ")

print ("hello players {} and {}".format(players_info[1], players_info[2]))

game_rules = {
    'rs': 1,
    'sr': 2,
    'ps': 2,
    'sp': 1,
    'rp': 2,
    'pr': 1,
    'ss': 0,
    'rr': 0,
    'pp': 0,
}

game_tools_usage = {
    'r': {1: 0,
          2: 0},
    'p': {1: 0,
          2: 0},
    's': {1: 0,
          2: 0},
}

players_wins = {0: 0,
                1: 0,
                2: 0,
                }

for round_counter in range(2):
    p1_choice = ""
    p2_choice = ""
    while p1_choice not in list_choice:
        p1_choice = raw_input("{} Please enter legitimate choice: R - Rock, P - Paper or S - Scissors ===> ".format(players_info[1]))

    while p2_choice not in list_choice:
        p2_choice = raw_input("{} Please enter legitimate choice: R - Rock, P - Paper or S - Scissors ===> ".format(players_info[2]))

    current_game = p1_choice + p2_choice
    game_results_history.append((round_counter, game_rules[current_game], current_game))

    game_tools_usage[p1_choice][1] += 1
    game_tools_usage[p2_choice][2] += 1

    players_wins[game_rules[current_game]] += 1

print(game_results_history)

for round_counter in game_results_history:
    print("Round {} | {} won | {} picked {} | {} picked {} ".format(
                                                                round_counter[0],
                                                                players_info[round_counter[1]],
                                                                players_info[1],
                                                                round_counter[2][0],
                                                                players_info[2],
                                                                round_counter[2][1]
    ))

print(game_tools_usage)
print(players_wins)

