with open("day14_input.txt", 'r') as fp:
    lines = [line.rstrip() for line in fp.readlines()]

memory = {}
masks = []
curr_mask = None
curr_value = None
curr_address = None

for line in lines:
    k, v = line.split(" = ")
    if k == "mask":
        masks.append(v)
        curr_mask = v
    else:
        # get address
        curr_address = int(k[4:-1])
        curr_value = int(v)

        bin_value = list(bin(curr_value)[2:].zfill(36))
        new_value = [0] * 36

        for i, (mask, value) in enumerate(zip(curr_mask, bin_value)):
            # do nothing if X
            if mask == "X":
                new_value[i] = value
            else:
                # change value to mask else
                new_value[i] = mask

        memory[curr_address] = int("".join(new_value), 2)
print(f"Part one solution: {sum(memory.values())}")

"""
If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
"""
with open("day14_input.txt", 'r') as fp:
    lines = [line.rstrip() for line in fp.readlines()]

memory = {}
for line in lines:
    k, v = line.split(" = ")
    if k == "mask":
        masks.append(v)
        curr_mask = v
    else:
        # get address
        curr_address = int(k[4:-1])
        curr_value = int(v)

        bin_add = list(bin(curr_address)[2:].zfill(36))
        new_add = ["0"] * 36

        v = len(list(bin(curr_address)[2:]))

        for i, (mask, value) in enumerate(zip(curr_mask, bin_add)):
            # if mask bit is floating then keep it floating on new address too
            if mask == "X":
                new_add[i] = "X"
            elif mask == "0":

                # change value to mask else
                new_add[i] = value
            elif mask == "1":
                new_add[i] = "1"

        new_add = "".join(new_add)

        # count floatings
        num_poss = new_add.count("X")

        flucts = []
        for i in range(2**num_poss):
            flucts.append( list(bin(i)[2:].zfill(num_poss)))

        for fluct in flucts:
            i = 0
            nadd = ""
            for a in new_add:
                if a == "X":
                    nadd+=str(fluct[i])
                    i+=1
                else:
                    nadd+=str(a)
            memory[int(nadd, 2)]=curr_value
print(sum(memory.values()))
