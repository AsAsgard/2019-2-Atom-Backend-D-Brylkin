#!/usr/bin/env python3
# coding: utf-8


class TickTackToe:

    first_player = "Player1"
    second_player = "Player2"

    player_symbols = {
        first_player: 'X',
        second_player: 'O'
    }

    win_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    def __init__(self):
        self._winner_optional = TickTackToe.WinnerOptional()
        self._game_over = False
        self._current_player = TickTackToe.first_player
        self._field = {i: str(i) for i in range(1, 10)}

    class ValidationResult:

        def __init__(self, status, reason):
            self.__status = status
            self._reason = reason

        def bad(self):
            return self.__status is False

        def good(self):
            return self.__status is True

        def reason(self):
            return self._reason

    class WinnerOptional:

        def __init__(self):
            self._winner = None

        def _set_winner(self, winner):
            self._winner = winner

        def exists(self):
            return self._winner is not None

        def get_winner_name(self):
            return self._winner if self._winner is not None else ""

    def is_game_over(self):
        return self._game_over

    def get_current_player(self):
        return self._current_player

    def get_winner_state(self):
        return self._winner_optional

    def render_area(self):
        print("-------------")
        print(f"| {self._field.get(1)} | {self._field.get(2)} | {self._field.get(3)} |")
        print("-------------")
        print(f"| {self._field.get(4)} | {self._field.get(5)} | {self._field.get(6)} |")
        print("-------------")
        print(f"| {self._field.get(7)} | {self._field.get(8)} | {self._field.get(9)} |")
        print("-------------")

    def validate_input(self, user_value):
        if user_value not in [str(i) for i in range(1, 10)]:
            return TickTackToe.ValidationResult(
                False,
                "Wrong input! You should input number of a cell (number in range 1-9)"
            )
        if self._field.get(int(user_value)) != user_value:
            return TickTackToe.ValidationResult(
                False,
                "This cell is occupied! You should input number of a free cell"
            )
        return TickTackToe.ValidationResult(
            True,
            ""
        )


    def set_entity(self, user_value):
        self._field[int(user_value)] = TickTackToe.player_symbols.get(self._current_player)

    def check_game_for_winner(self):
        for combination in TickTackToe.win_combinations:
            if len({self._field.get(i) for i in combination}) == 1:
                self._winner_optional._set_winner(self._current_player)
                self._game_over = True
                return
        if {self._field.get(i) for i in range(1, 10)} == set(TickTackToe.player_symbols.values()):
            self._game_over = True


    def change_turn(self):
        self._current_player = \
            TickTackToe.second_player if self._current_player == TickTackToe.first_player else TickTackToe.first_player
