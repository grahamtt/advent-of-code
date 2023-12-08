from advent_of_code.day3 import chop_it_up, input_value, SYMBOL_PATTERN, NUMERAL_PATTERN


def add_part(is_part_num, row, col):
    if row not in is_part_num:
        is_part_num[row] = {}

    is_part_num[row][col] = True

def scan_for_part_nums(parsed_schematic):
    is_part_num = {}

    for row_num, col in parsed_schematic.items():
        for col_num, val_str in col.items():
            if not NUMERAL_PATTERN.match(val_str):
                continue
            for i in range(row_num-1, row_num+2):
                if i not in parsed_schematic:
                    continue
                for j in range(col_num - 1, col_num + len(val_str)+1):
                    if j not in parsed_schematic[i]:
                        continue
                    if SYMBOL_PATTERN.match(parsed_schematic[i][j]):
                        if row_num not in is_part_num:
                            is_part_num[row_num] = {}
                        is_part_num[row_num][col_num] = True

    return is_part_num



def execute(current_input=input_value):
    parsed_schematic = chop_it_up(current_input)
    is_part_num = scan_for_part_nums(parsed_schematic)

    sum = 0
    for i, row in is_part_num.items():
        for j, val_str in row.items():
            sum += int(parsed_schematic[i][j])

    return sum


if __name__ == '__main__':
    print(execute())