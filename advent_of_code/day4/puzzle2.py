from advent_of_code.day4 import input_values, parse_input


def execute(input_str):
    copies_count = {}
    sum = 0
    for game_num, winning_vals, actual_vals in parse_input(input_str):
        next_copy = game_num + 1
        if game_num not in copies_count:
            copies_count[game_num] = 1
        sum += copies_count[game_num]
        for actual_val in actual_vals:
            if actual_val in winning_vals:
                if next_copy not in copies_count:
                    copies_count[next_copy] = copies_count[game_num] + 1
                else:
                    copies_count[next_copy] += copies_count[game_num]
                next_copy+=1

    return sum


if __name__ == "__main__":
    print(execute(input_values))