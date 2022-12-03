def run(challenge_input):

    total = sum(map(find_compartments_intersection_power, challenge_input.readlines()))
    print(f'Total: {total}')


def find_compartments_intersection_power(line):
    line = line.rstrip()

    c1, c2 = set(), set()

    mid = len(line) // 2
    for i in range(0, mid):
        c1.add(line[i])
        c2.add(line[i + mid])

    return calc_power(c1.intersection(c2).pop())

a_ascii = ord('a')
A_ascii = ord('A')
def calc_power(item):
    ascii_value = ord(item)
    if ascii_value < a_ascii:
        return ascii_value - A_ascii + 27

    return ascii_value - a_ascii + 1