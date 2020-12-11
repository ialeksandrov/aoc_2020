with open("day3_input.txt", 'r') as f:
    lines=f.readlines()

curr_x = 0

slope_x = 3
slope_y=1

trees = 0
for curr_y, each_line in enumerate(lines):
    if each_line[curr_x] == "#":
        trees+=1
    curr_x = (curr_x + slope_x) % len(each_line[:-1])
print(f"Solution 1:{trees}")

#2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
mult_trees=1
for slope in slopes:
    print("Slope: ", slope)
    slope_x, slope_y=slope
    trees = 0
    curr_x = 0
    for curr_y, each_line in enumerate(lines):
        if curr_y%slope_y == 0:

            if each_line[curr_x] == "#":
                trees+=1
            curr_x = (curr_x + slope_x) % len(each_line[:-1])
    print("Trees on this slope: ", trees)
    mult_trees*=trees
print("Solution 2: ", mult_trees)

