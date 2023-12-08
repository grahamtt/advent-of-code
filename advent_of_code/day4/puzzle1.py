from advent_of_code.day4 import input_values, parse_input


def execute(input_str):
    sum = 0
    for game_num, winning_vals, actual_vals in parse_input(input_str):
        acc = 0
        for actual_val in actual_vals:
            if actual_val in winning_vals:
                if acc == 0:
                    acc = 1
                else:
                    acc *= 2
        sum += acc

    return sum


if __name__ == "__main__":
    print(execute(input_values))