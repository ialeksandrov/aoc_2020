import re
from collections import defaultdict

with open("day24_input.txt") as fp:
    lines = fp.read().splitlines()

curr_floor = defaultdict(lambda: False)
for line in lines:
    coo = re.findall(r"e|se|sw|w|nw|ne", line)
    ns = coo.count("se") + coo.count("sw") - coo.count("ne") - coo.count("nw")
    we = coo.count("e") + coo.count("ne") - coo.count("w") - coo.count("sw")

    curr_floor[((ns, we))] = not curr_floor[(ns, we)]
print(f"Total tiles with back side up: {sum(list(curr_floor.values()))}")

floor = curr_floor

for _ in range(100):
    new_floor = defaultdict(lambda: False)

    # Add the outer ring of the current floor for consideration.
    for k, v in floor.items():
        for o in [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]:
            tile = (k[0] + o[0], k[1] + o[1])
            if tile not in new_floor:
                new_floor[tile] = floor.get(tile, False)
    for k, v in new_floor.items():

        neighbors = sum([floor[(k[0] + o[0], k[1] + o[1])] for o in [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]])
        if v:
            if not neighbors or neighbors > 2:
                new_floor[k] = False
        else:
            if neighbors == 2:
                new_floor[k] = True

    floor = new_floor


print(f"Total tiles with back side up: {sum(list(new_floor.values()))}")

