import rpg_game


def play_game():
    new_game = rpg_game.Game()
    new_name = input()
    if new_name == "":
        new_game.create_players()
    else:
        new_game.create_players(new_name)
    # new_game.print_players()
    round_num = 1
    for hero in new_game.hero_list:
        new_game.num_wins = 0
        new_game.num_loss = 0
        while len(new_game.opponent_list) > 0:
            print(f"Please enter [a] to attack, or [q] to quit.")
            user_action = input()
            if user_action == "q":
                break
            elif user_action == "a":
                print(f"-----Round {round_num}-----")
                print(new_game.encounter(hero))
                round_num += 1
            else:
                pass
        print(f"-----Final hero status: {hero}-----")
        print(f"---------Wins: {new_game.num_wins} | Losses: {new_game.num_loss}---------")
        print("End Game")


play_game()
