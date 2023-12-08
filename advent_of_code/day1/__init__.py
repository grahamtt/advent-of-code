import re

DIGIT_TRANSFORM = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
EXTRACT_NUMERIC_VALUE = re.compile(f'([0-9]|{"|".join(DIGIT_TRANSFORM.keys())}).*$')
def extract_first_and_last_numeric_value_as_int(input):
    match1 = match2 = EXTRACT_NUMERIC_VALUE.search(input)
    while True:
        temp_match = EXTRACT_NUMERIC_VALUE.search(input, match2.start(1) + 1)
        if temp_match:
            match2 = temp_match
        else:
            break

    str_value = f"{DIGIT_TRANSFORM[match1.group(1)] if match1.group(1) in DIGIT_TRANSFORM else match1.group(1)}{DIGIT_TRANSFORM[match2.group(1)] if match2.group(1) in DIGIT_TRANSFORM else match2.group(1)}"
    return int(str_value)


DIGIT_TRANSFORM_PATTERN = re.compile('|'.join(DIGIT_TRANSFORM.keys()))
def extract_first_and_last_numeric_value_or_string_as_int(input_str: str):

    while True:
        match = DIGIT_TRANSFORM_PATTERN.search(input_str)
        if not match:
            break
        input_str = input_str[:match.start(0)] + DIGIT_TRANSFORM[match.group(0)] + input_str[match.end(0):]

    return input_str
