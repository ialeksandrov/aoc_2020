from collections import deque

class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

my_input = [int(i) for i in "562893147"]

def part1():
    my_cups = deque(my_input)
    for _ in range(100):
        orig = my_cups[0]
        dest = my_cups[0]-1

        if dest < 1:
            dest = 9
        my_cups.rotate(-1)

        cup1 = my_cups.popleft()
        cup2 = my_cups.popleft()
        cup3 = my_cups.popleft()

        while dest in (cup1, cup2, cup3):
            dest = dest - 1 if dest > 1 else dest + 8

        while my_cups[0] != dest:
            my_cups.rotate(-1)
        my_cups.rotate(-1)

        my_cups.append(cup1)
        my_cups.append(cup2)
        my_cups.append(cup3)

        while my_cups[0] != orig:
            my_cups.rotate(-1)
        my_cups.rotate(-1)

    while my_cups[0] != 1:
        my_cups.rotate(-1)
    my_cups.popleft()

    return ''.join([str(i) for i in my_cups])
print(f"Part 1 solution: {part1()}")


def part2():
    my_nodes = {}

    last_node = None
    for i in my_input:
        curr_node = LinkedListNode(i)
        my_nodes[i] = curr_node

        if last_node is not None:
            last_node.right = curr_node
            curr_node.left = last_node

        last_node = curr_node
    for i in range(len(my_input)+1, 1_000_001):
        curr_node = LinkedListNode(i)
        my_nodes[i] = curr_node
        if last_node is not None:
            last_node.right = curr_node
            curr_node.left = last_node
        last_node = curr_node

    # Complete the circle
    ptr = my_nodes[my_input[0]]
    last_node.right = ptr
    ptr.left = last_node

    ptr = my_nodes[my_input[0]]
    for i in range(10000000):
        p_val = ptr.item

        cup1 = ptr.right
        cup2 = cup1.right
        cup3 = cup2.right

        ptr.right = cup3.right
        ptr.right.left = ptr

        d_val = p_val - 1 or 1000000
        while d_val in (cup1.item, cup2.item, cup3.item):
            d_val = d_val - 1 or 1000000

        d_node = my_nodes[d_val]

        cup3.right = d_node.right
        cup3.right.left = cup3
        d_node.right = cup1
        cup1.left = d_node

        ptr = ptr.right

    while ptr.item != 1:
        ptr = ptr.right

    return ptr.right.item * ptr.right.right.item
print(f"Part 2 solution: {part2()}")
