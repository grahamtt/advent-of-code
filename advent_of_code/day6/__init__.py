day_6_input = """Time:        62     64     91     90
Distance:   553   1010   1473   1074"""

def parse_puzzle_6_input(my_input=day_6_input):
    race_times_str, record_distance_str = my_input.split('\n', maxsplit=2)
    race_times = [int(r) for r in race_times_str.split()[1:]]
    record_distances = [int(r) for r in record_distance_str.split()[1:]]
    return zip(race_times, record_distances)