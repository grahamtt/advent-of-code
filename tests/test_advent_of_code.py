import pytest

from advent_of_code import extract_first_and_last_numeric_value_as_int


@pytest.mark.parametrize(["input", "expected_output"], [
    ("12", 12),
    ("1", 11),
    ("1asdf3", 13),
    ("1asdf3asdf", 13),
    ("1asdf3asdf4", 14),
    ("asdf1asdf3asdf4asdf", 14),
    ("one", 11),
    ("onetwo", 12),
    ("twone", 21),
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
    ("36fiveight", 38),
])
def test_extract_vales(input, expected_output):
    assert extract_first_and_last_numeric_value_as_int(input) == expected_output
