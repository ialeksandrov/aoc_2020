with open("day1_input.txt") as f:
    list = [int(x.strip()) for x in f]

for i, n1 in enumerate(list):
    for j, n2 in enumerate(list[i+1:]):
        if n1 + n2 == 2020:
            part1 = n1 * n2
        for n3 in list[i+j+1:]:
            if n1 + n2 + n3 == 2020:
                part2 = n1 * n2 * n3


print(part1)
print(part2)
