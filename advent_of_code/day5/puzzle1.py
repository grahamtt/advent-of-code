from typing import List

from intervaltree import IntervalTree

from advent_of_code.day5 import day5_input, parse_input


def execute(input):
    seeds, mappings = parse_input(input)
    fully_mapped_seeds = [apply_mappings(seed, mappings) for seed in seeds]
    return min(fully_mapped_seeds)

def apply_mappings(seed: int, mappings: List[IntervalTree]):
    current_val = seed
    for mapping in mappings:
        if mapping.overlaps_point(current_val):
            interval = next(iter(mapping[current_val]))
            current_val = current_val - interval.begin + interval.data
        pass

    return current_val

if __name__ == "__main__":
    print(execute(day5_input))