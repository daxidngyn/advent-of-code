from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=3)
data = puzzle.input_data

schematic = []
for line in data.split('\n'):
    schematic.append(line)

len_r, len_c = len(schematic), len(schematic[0])
delta_r, delta_c = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]

def get_neighbors(r, c):
    for i in range(len(delta_r)):
        new_r, new_c = r + delta_r[i], c + delta_c[i]
        if 0 <= new_r < len_r and 0 <= new_c < len_c:
            yield (new_r, new_c)

def get_part_num(r, c, visited):
    visited.add((r, c))
    val, new_c = schematic[r][c], c
    while 0 <= new_c - 1 and schematic[r][new_c - 1].isnumeric(): # left
        new_c -= 1
        visited.add((r, new_c))
        val = schematic[r][new_c] + val

    new_c = c
    while new_c + 1 < len_c and schematic[r][new_c + 1].isnumeric(): # right
        new_c += 1
        visited.add((r, new_c))
        val = val + schematic[r][new_c]

    return int(val)

# part 1 utility
def check_valid_part(r, c):
    for neighbor in get_neighbors(r, c):
        n_r, n_c = neighbor
        x = schematic[n_r][n_c]
        if not x.isnumeric() and x != '.':
            return True
                
    return False

res1 = res2 = 0
visited1, visited2 = set(), set()

for r in range(len_r):
    for c in range(len_c):
        # part 1
        if schematic[r][c].isnumeric():
            if (r, c) in visited1: continue
            if check_valid_part(r, c):
                res1 += get_part_num(r, c, visited1)

        # part 2
        if schematic[r][c] != '*': continue

        valid_neighbors = []
        neighbors = get_neighbors(r, c)
        for neighbor in neighbors:
            if neighbor in visited2: continue

            n_r, n_c = neighbor
            if schematic[n_r][n_c].isnumeric():
                valid_neighbors.append(get_part_num(n_r, n_c, visited2))

        if len(valid_neighbors) == 2:
            res2 += valid_neighbors[0] * valid_neighbors[1]

        visited2 = set()
        valid_neighbors = []
        
print('part 1:', res1)
print('part 2:', res2)
