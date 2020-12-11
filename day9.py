with open('day9_input.txt') as file:
    preamble = list(map(lambda x: int(x[:-1]), file.readlines()))


class Xmas:
    def __init__(self, preamble):
        self.preamble = preamble

    def is_valid(self, int):
        for i in self.preamble[:-1]:
            for j in self.preamble[1:]:
                if i + j == int:
                    return True
        return False

    def shift(self, number):
        self.preamble.append(number)
        self.preamble = self.preamble[1:]

    def find_weakness(self, invalid):
        not_found = True
        for step in range(2, len(self.preamble)+1):
            start = 0
            array = True
            while array and not_found:
                array = self.preamble[start:step]
                if sum(array) == invalid:
                    print(f'Weakness : {min(array)+max(array)}')
                    not_found = False
                    break
                start += 1
                step += 1


# Part 1
preamble_scale = 25
first_invalid = 0
xmas = Xmas(preamble[:preamble_scale])
for i in preamble[preamble_scale:]:
    if not xmas.is_valid(i):
        first_invalid = i
        print(f'{i} is The First Invalid')
        break
    xmas.shift(i)

# Part 2
xmas = Xmas(preamble)
xmas.find_weakness(first_invalid)

