from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)
data = puzzle.input_data.split('\n')

def determine_points(wins):
    if wins <= 1: return wins
    return 2**(wins-1)

res1 = res2 = 0
copies = {}

for line in data:
    split = line.split('|')
    winning_nums_split = split[0].split(':')

    card_num = int(winning_nums_split[0][5:])
    winning_nums = set(winning_nums_split[1].split())
    owned_nums = set(split[1].split())

    wins = len(owned_nums.intersection(winning_nums))
    points = determine_points(wins)
    res1 += points

    for i in range(card_num + 1, card_num + wins + 1, 1):
        copies[i] = copies.get(i, 0) + 1 + copies.get(card_num, 0)

res2 = len(data) + sum(copies.values())

print('part 1', res1)
print('part 2', res2)
    