with open("day13_input.txt", "r") as fp:
    lines = fp.readlines()
timestamp = int(lines[0][:-1])
bus_ids = [int(x) for x in lines[1].split(",") if x.isdigit()]

import numpy as np
timestamps = range(timestamp-50, timestamp+50)
valid = np.inf
diff = np.inf
bus_id = np.inf

for time in timestamps:
    for bus in bus_ids:
        if time%bus==0:
            d = abs(time-timestamp)
            if time>timestamp and d < diff:
                valid = time
                diff = d
                bus_id = bus

print(bus_id*(valid-timestamp))

LINES=lines
start = int(LINES[0])
busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]

def part2():
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    print(mods)
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val
print(part2())
