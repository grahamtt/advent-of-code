from textwrap import dedent

from advent_of_code.day3 import chop_it_up
from advent_of_code.day3.puzzle1 import execute, scan_for_part_nums

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_chop_it_up():
    assert chop_it_up(test_input) == {0: {0: '467', 5: '114'},
                                         1: {3: '*'},
                                         2: {2: '35', 6: '633'},
                                         3: {6: '#'},
                                         4: {0: '617', 3: '*'},
                                         5: {5: '+', 7: '58'},
                                         6: {2: '592'},
                                         7: {6: '755'},
                                         8: {3: '$', 5: '*'},
                                         9: {1: '664', 5: '598'}}

def test_scan_for_part_nums():
    assert scan_for_part_nums({0: {0: '467', 5: '114'},
                                         1: {3: '*'},
                                         2: {2: '35', 6: '633'},
                                         3: {6: '#'},
                                         4: {0: '617', 3: '*'},
                                         5: {5: '+', 7: '58'},
                                         6: {2: '592'},
                                         7: {6: '755'},
                                         8: {3: '$', 5: '*'},
                                         9: {1: '664', 5: '598'}}) == {0: {0: True},
                                                                         2: {2: True, 6: True},
                                                                         4: {0: True},
                                                                         6: {2: True},
                                                                         7: {6: True},
                                                                         9: {1: True, 5: True}}


def test_execute():
    assert execute(test_input) == 4361

