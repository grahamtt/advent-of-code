from advent_of_code.day3 import chop_it_up, input_value, SYMBOL_PATTERN, NUMERAL_PATTERN


def add_part(is_part_num, row, col):
    if row not in is_part_num:
        is_part_num[row] = {}

    is_part_num[row][col] = True

def scan_for_part_nums(parsed_schematic):
    part_numbers = {}

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
                        if i not in part_numbers:
                            part_numbers[i] = {}
                        if j not in part_numbers[i]:
                            part_numbers[i][j] = []
                        part_numbers[i][j].append(int(val_str))

    return part_numbers



def execute(current_input=input_value):
    parsed_schematic = chop_it_up(current_input)
    part_nums = scan_for_part_nums(parsed_schematic)

    sum = 0
    for row_num, col in part_nums.items():
        for col_num, nums in col.items():
            if len(nums) == 2:
                sum += nums[0] * nums[1]

    return sum

if __name__ == '__main__':
    print(execute())