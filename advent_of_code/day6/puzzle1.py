from math import floor, ceil, log, sqrt

from advent_of_code.day6 import day_6_input, parse_puzzle_6_input


def execute_day6_puzzle1(my_input):
    race_time_and_record_distances = parse_puzzle_6_input(my_input)

    for race_time, record_distance in race_time_and_record_distances:
        max_speed = get_max_speed(race_time)
        charging_time_producing_record_distance = 0
        pass


    pass

def get_max_speed(race_time):
    return floor(race_time/2)*ceil(race_time/2)

if __name__ == "__main__":
    print(execute_day6_puzzle1(day_6_input))