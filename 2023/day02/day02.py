from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=2)
data = puzzle.input_data.split('\n')

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def parse_line(line):
    game_id = line.split(':')[0][4:]
    game_subsets = line.split(':')[1].split(';')

    game_subsets = [x.strip(' ') for x in game_subsets]
    game_subsets = [x.split(',') for x in game_subsets]
    game_subsets = [x.strip(' ').split(' ') for sublist in game_subsets for x in sublist]

    return (game_id, game_subsets)

def check_valid_game(game):
    for set in game:
        num, color = set
        if int(num) > MAX_CUBES[color]:
            return False
    
    return True

def get_max_cubes(game):
    max_red = max_green = max_blue = 0

    for set in game:
        num, color = set
        match color:
            case 'red':
                max_red = max(max_red, int(num))
            case 'green':
                max_green = max(max_green, int(num))
            case 'blue':
                max_blue = max(max_blue, int(num))

    return (max_red, max_green, max_blue)

res1 = 0
res2 = 0
for line in data:
    game_id, game_subsets = parse_line(line)
    
    if check_valid_game(game_subsets):
        res1 += int(game_id)

    max_red, max_green, max_blue = get_max_cubes(game_subsets)
    res2 += max_red * max_green * max_blue
    
print('part 1:', res1)
print('part 2:', res2)
