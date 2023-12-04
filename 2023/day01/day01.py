from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=1)
data = puzzle.input_data.split('\n')

DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def check_digit(line):
    if line[0].isnumeric(): return line[0]

    d = next(filter(line.startswith, DIGITS), None)
    if d: return DIGITS[d]

    return None

def get_calibration(line):
    digit1 = digit2 = None

    for i in range(len(line)):
        digit1 = check_digit(line[i:])
        if digit1: break

    for i in range(len(line)-1, -1, -1):
        digit2 = check_digit(line[i:])
        if digit2: break
    

    return digit1 + digit2

res = 0
for line in data:
    res += int(get_calibration(line))

print(res)