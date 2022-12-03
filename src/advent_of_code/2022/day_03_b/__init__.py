def run(challenge_input):
    lines = challenge_input.readlines()
    total = sum(map(find_compartments_intersection_power, [lines[i:i+3] for i in range(0, len(lines), 3)]))

    print(f'Total: {total}')

def find_compartments_intersection_power(elves_rucksacks):
    intersection = None
    for elf_items in elves_rucksacks:
        elf_items_types = set(elf_items.rstrip())

        if (intersection == None):
            intersection = elf_items_types
        else:
            intersection = intersection.intersection(elf_items_types)


    return calc_power(intersection.pop())

a_ascii = ord('a')
A_ascii = ord('A')
def calc_power(item):
    ascii_value = ord(item)
    if ascii_value < a_ascii:
        return ascii_value - A_ascii + 27

    return ascii_value - a_ascii + 1