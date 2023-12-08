import pytest

from advent_of_code.day6 import parse_puzzle_6_input
from advent_of_code.day6.puzzle1 import execute_day6_puzzle1, get_max_speed


def test_parse_puzzle_6_input():
    assert list(parse_puzzle_6_input()) == [(62, 553), (64, 1010), (91, 1473), (90, 1074)]


def test_execute_day6_puzzle1():
    assert execute_day6_puzzle1("""Time:      7  15   30
Distance:  9  40  200""") == 288


@pytest.mark.parametrize(["race_time", "expected_max_speed"], [
    (3, 2),
    (4, 4),
    (5, 6),
    (7, 12),
])
def test_get_max_speed(race_time, expected_max_speed):
    assert get_max_speed(race_time) == expected_max_speed
