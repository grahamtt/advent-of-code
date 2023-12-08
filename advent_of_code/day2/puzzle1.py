from typing import Dict

from advent_of_code.day2 import extract_named_values, input_values


def execute():
    max_values = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    game_possible: Dict[str, bool] = {}
    for game_num, color_name, color_count in extract_named_values(input_values):
        current_value_possible = color_count <= max_values[color_name]
        if game_num in game_possible:
            game_possible[game_num] = game_possible[game_num] & current_value_possible
        else:
            game_possible[game_num] = current_value_possible

    totaled_possible_game_numbers = sum(gn for gn, possible in game_possible.items() if possible)

    print(totaled_possible_game_numbers)


if __name__ == "__main__":
    execute()
