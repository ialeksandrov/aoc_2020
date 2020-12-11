

with open("day6_input.txt", "r") as fp:
    lines=fp.readlines()

groups = []
group = []
for question in lines:
    if question!="\n":
        group.append(question.split("\n")[0])
    else:
        groups.append(group)
        group=[]
groups.append(group)

# solution to challenge 1
solution_1 = []
for group in groups:
    #print(f"Group: ", group)
    unique_ques = []
    for ques in group:
        unique_ques.extend([uq for uq in ques])

    #print(f"Unique questions: {set(unique_ques)}")
    solution_1.extend(list(set(unique_ques)))
print(f"Solution 1: {len(solution_1)}")


# solution to challenge 2
from collections import Counter
total = 0
for group in groups:
    #print(f"\nGroup: {group}")
    group_size = len(group)
    #print(f"Length of group: {group_size}")

    # make single list of enitire group and count occurence
    counts = Counter("".join(group))
    #print(counts)

    counts = Counter(list(counts.values()))[group_size]
    total+=counts
print(f"Solution 2:", total)
