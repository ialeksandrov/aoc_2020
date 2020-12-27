from collections import *
def day15(filename, turns):
    with open(filename) as fp:
        lines = [l.rstrip() for l in fp.readlines()]
        lines = [int(l) for l in lines[0].split(",")]

    num_to_speak = lines[-1]
    turn_num = defaultdict(deque)

    for v, k in enumerate(lines):
        turn_num[k].append(v+1)

    turn = len(lines)+1
    while turn<=turns:
        l = len(turn_num[num_to_speak])
        if l>1:
            num_to_speak = turn_num[num_to_speak][-1] - turn_num[num_to_speak][-2]
            turn_num[num_to_speak].append(turn)
        elif l==1:
            num_to_speak = 0
            turn_num[num_to_speak].append(turn)
        else:
            num_to_speak = 0
            turn_num[num_to_speak].append(turn)

        turn+=1
    print(num_to_speak)

print(day15("day15_input.txt", 2020))
day15("day15_input.txt", 30000000)
