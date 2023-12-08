from typing import Dict

from advent_of_code.day2 import extract_named_values, input_values


def execute():
    max_values_template = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    game_mins: Dict[int, Dict[str, int]] = {}
    for game_num, color_name, color_count in extract_named_values(input_values):
        if game_num not in game_mins:
            game_mins[game_num] = max_values_template.copy()

        game_mins[game_num][color_name] = max(game_mins[game_num][color_name], color_count)

    game_powers = [m['red'] * m['green'] * m['blue'] for m in game_mins.values()]
    summed_game_powers = sum(game_powers)

    print(summed_game_powers)


if __name__ == "__main__":
    execute()
