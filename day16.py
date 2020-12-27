import re
from collections import defaultdict

with open("day16_input.txt") as f:
    lines = [x.strip() for x in f]

rules = defaultdict(list)
ranges = set()
for line in lines[:20]:
    rulename = re.match(r"(\w+( \w+)?):", line).group(1)
    for r in re.findall(r"\d+\-\d+", line):
        rules[rulename].append(tuple(int(x) for x in r.split("-")))
        ranges.add(tuple(int(x) for x in r.split("-")))

error_rate = 0
valid_tickets = []
for line in lines[25:]:
    values = [int(x) for x in line.split(",")]
    for v in values:
        valid = False
        for lo, hi in ranges:
            if lo <= v <= hi:
                valid = True
                break
        if not valid:
            error_rate += v
            break
    if valid:
        valid_tickets.append(values)

# dict mapping each index in a ticket to the fields that are possible for that index
possible_fields = {i: set(rules.keys()) for i in range(len(valid_tickets[0]))}
for ticket in valid_tickets:
    for i, value in enumerate(ticket):
        for field in rules:
            possible = False
            for lo, hi in rules[field]:
                if lo <= value <= hi:
                    possible = True
                    break
            if not possible:
                possible_fields[i].discard(field)

# Some indices fit multiple fields – iterate through the ones that only fit one first, and
# remove this field from all other indices
for i in sorted(possible_fields, key=lambda k: len(possible_fields[k])):
    this_field = next(iter(possible_fields[i]))
    for j in possible_fields:
        if i != j:
            possible_fields[j].discard(this_field)


my_ticket = [int(x) for x in lines[22].split(",")]
ans = 1
for i in possible_fields:
    if possible_fields[i].pop().startswith("departure"):
        ans *= my_ticket[i]

print("Part 1:", error_rate)
print("Part 2:", ans)