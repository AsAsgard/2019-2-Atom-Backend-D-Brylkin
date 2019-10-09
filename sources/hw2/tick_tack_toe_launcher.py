#!/usr/bin/env python3
# coding: utf-8

from tick_tack_toe import TickTackToe

game_instance = TickTackToe()


if __name__ == "__main__":
    print("Hello, players! Let's start the game!")
    print("Free cells marked with numbers. Choose one at your turn and go on!")
    while not game_instance.is_game_over():
        print("-------------------------------------------")
        print(f"{game_instance.get_current_player()} turn.")
        game_instance.render_area()
        print("Choose the free cell!")
        user_value = input()

        validation_result = game_instance.validate_input(user_value)
        if validation_result.bad():
            print("Validation input result is error! Reason:")
            print(f"{validation_result.reason()}")
            print("Try again!")
            continue

        game_instance.set_entity(user_value)
        game_instance.check_game_for_winner()

        if not game_instance.is_game_over():
            game_instance.change_turn()

    game_instance.render_area()
    winner_optional = game_instance.get_winner_state()
    if winner_optional.exists():
        print(f"Congratulations! The player {winner_optional.get_winner_name()} wins!")
    else:
        print("The result of the match is a draw!")
