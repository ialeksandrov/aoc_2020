f = open('day22_input.txt').read().strip().split("\n\n")

origp1, origp2 = [[int(x) for x in q.split("\n")[1:]] for q in f]
p1 = origp1.copy()
p2 = origp2.copy()


def war(p1cards, p2cards):
    while len(p1cards) > 0 and len(p2cards) > 0:
        a = p1.pop(0)
        b = p2.pop(0)
        if a > b:
            p1.extend([a, b])
        else:
            p2.extend([b, a])
    return p1cards if len(p1cards) > 0 else p2cards


print(sum((i + 1) * x for i, x in enumerate(war(p1, p2)[::-1])))


def recursive_war(p1cards, p2cards, visited):
    while (len(p1cards) > 0 and len(p2cards) > 0):
        if (tuple(p1cards), tuple(p2cards)) in visited:
            return 1, p1cards

        visited.add((tuple(p1cards), tuple(p2cards)))

        a, b = p1cards.pop(0), p2cards.pop(0)
        if len(p1cards) >= a and len(p2cards) >= b:
            winner, _ = recursive_war(p1cards[:a], p2cards[:b], set())
        else:
            winner = 1 if a > b else 0

        if winner == 1:
            p1cards.extend([a, b])
        else:
            p2cards.extend([b, a])
    return (1, p1cards) if len(p1cards) > 0 else (0, p2cards)


print(sum((i + 1) * x for i, x in enumerate(recursive_war(origp1, origp2, set())[1][::-1])))