def parse_input(input):
    return [line.rstrip() for line in input.readlines()]


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)

def part_1(data):
    print(f'Part_1: {data}')

def part_2(data):
    print(f'Part_2: {data}')