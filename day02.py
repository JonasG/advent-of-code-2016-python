INITIAL_NUMBER = '5'


SimpleKeypad = {
    '1': {'R': '2', 'D': '4'},
    '2': {'L': '1', 'R': '3', 'D': '5'},
    '3': {'L': '2', 'D': '6'},
    '4': {'U': '1', 'R': '5', 'D': '7'},
    '5': {'U': '2', 'L': '4', 'R': '6', 'D': '8'},
    '6': {'U': '3', 'L': '5', 'D': '9'},
    '7': {'U': '4', 'R': '8'},
    '8': {'U': '5', 'L': '7', 'R': '9'},
    '9': {'U': '6', 'L': '8'},
}


FancyKeypad = {
    '1': {'D': '3'},
    '2': {'R': '3', 'D': '6'},
    '3': {'U': '1', 'L': '2', 'D': '7', 'R': '4'},
    '4': {'L': '3', 'D': '8'},
    '5': {'R': '6'},
    '6': {'U': '2', 'L': '5', 'R': '7', 'D': 'A'},
    '7': {'U': '3', 'L': '6', 'R': '8', 'D': 'B'},
    '8': {'U': '4', 'L': '7', 'R': '9', 'D': 'C'},
    '9': {'L': '8'},
    'A': {'U': '6', 'R': 'B'},
    'B': {'U': '7', 'L': 'A', 'R': 'C', 'D': 'D'},
    'C': {'U': '8', 'L': 'B'},
    'D': {'U': 'B'}
}


def enter_procedure(procedure, keypad):
    lines = (s.strip() for s in procedure.splitlines())
    current_number = INITIAL_NUMBER
    result = ''

    for line in lines:
        current_number = _find_destination_number(current_number, line, keypad)
        result += current_number

    return result


def _find_destination_number(start_number, sequence, keypad):
    current_number = start_number

    for character in sequence:
        if character in keypad[current_number].keys():
            current_number = keypad[current_number][character]

    return current_number
