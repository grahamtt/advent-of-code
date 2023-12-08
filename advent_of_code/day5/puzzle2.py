from typing import List, Set, Iterable, Tuple

from intervaltree import IntervalTree, Interval

from advent_of_code.day5 import day5_input, parse_input


def execute(input):
    seeds, mappings = parse_input(input)
    seed_intervals = [Interval(seeds[i], seeds[i]+seeds[i+1], seeds[i]) for i in range(0, len(seeds), 2)]

    fully_mapped_seeds = [apply_mappings(seed_interval, mappings) for seed_interval in seed_intervals]
    return min(min(j.begin for j in i) for i in fully_mapped_seeds)

def apply_mappings(seed_interval: Interval, mappings: List[IntervalTree]) -> Iterable[Interval]:
    current_intervals: Set[Interval] = {seed_interval,}
    mapping_num = 1
    for mapping in mappings:
        print(f"Calculating mapping {mapping_num} for current {len(current_intervals)} intervals")
        new_intervals = set()
        remainders = IntervalTree()
        for input_interval in current_intervals:

            output_intervals, remainders = calculate_mapping_intersections(input_interval, mapping, remainders, )
            new_intervals |= output_intervals
            print(f"Input: {input_interval}; mapping: {mapping}; output: {output_intervals}; remainders: {remainders}")

        new_intervals |= remainders.items()
        current_intervals = {Interval(i.data, i.end-i.begin+i.data, i.data) for i in new_intervals}
        mapping_num += 1

    return current_intervals

def calculate_mapping_intersections(input_interval: Interval, mapping: IntervalTree, remainders: IntervalTree) -> Tuple[Set[Interval], IntervalTree]:
    output_intervals = set()
    overlapping_remainders = remainders[input_interval.begin:input_interval.end]
    if overlapping_remainders:
        _remainders = IntervalTree()
        for remainder in overlapping_remainders:
            output_intervals.add(Interval(max(input_interval.begin, remainder.begin), min(input_interval.end, remainder.end), remainder.data - input_interval.begin + max(input_interval.begin, remainder.begin)))
            if input_interval.begin < remainder.begin:
                _remainders.add(Interval(input_interval.begin, remainder.begin, remainder.data))
            if input_interval.end > remainder.end:
                _remainders.add(Interval(remainder.end, input_interval.end, remainder.data - input_interval.begin + remainder.end))
    else:
        _remainders = IntervalTree(remainders)

    overlapping_intervals = mapping[input_interval.begin:input_interval.end]
    if overlapping_intervals:
        for overlapping_interval in overlapping_intervals:
            output_intervals.add(Interval(max(input_interval.begin, overlapping_interval.begin), min(input_interval.end, overlapping_interval.end), overlapping_interval.data - overlapping_interval.begin + max(input_interval.begin, overlapping_interval.begin)))
            if input_interval.begin < overlapping_interval.begin:
                _remainders.add(Interval(input_interval.begin, overlapping_interval.begin, input_interval.data))
            if input_interval.end > overlapping_interval.end:
                _remainders.add(Interval(overlapping_interval.end, input_interval.end, input_interval.data - input_interval.begin + overlapping_interval.end))
    else:
        _remainders.add(input_interval)

    return output_intervals, _remainders


if __name__ == "__main__":
    print(execute(day5_input))