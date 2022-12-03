a_ascii = ord('a')
A_ascii = ord('A')

def calc_power(item):
    ascii_value = ord(item)
    if ascii_value < a_ascii:
        return ascii_value - A_ascii + 27

    return ascii_value - a_ascii + 1

def run(challenge_input):
    part_1(challenge_input)
    part_2(challenge_input)


def part_1(challenge_input):
    total = sum(map(find_compartments_intersection_power, challenge_input.readlines()))
    print(f'Part_1 Total: {total}')

def find_compartments_intersection_power(line):
    line = line.rstrip()

    c1, c2 = set(), set()

    mid = len(line) // 2
    for i in range(0, mid):
        c1.add(line[i])
        c2.add(line[i + mid])

    return calc_power(c1.intersection(c2).pop())


def part_2(challenge_input):
    lines = challenge_input.readlines()
    total = sum(map(find_elves_intersection_power, [lines[i:i+3] for i in range(0, len(lines), 3)]))

    print(f'Part_2 Total: {total}')

def find_elves_intersection_power(elves_rucksacks):
    intersection = None
    for elf_items in elves_rucksacks:
        elf_items_types = set(elf_items.rstrip())

        if (intersection == None):
            intersection = elf_items_types
        else:
            intersection = intersection.intersection(elf_items_types)


    return calc_power(intersection.pop())
