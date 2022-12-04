def run(input):
    lines = [l.rstrip() for l in input.readlines()]
    part_1(lines)
    part_2(lines)

def to_set(start, end):
    return set(list(range(start, end + 1)))

def parse(line):
    return [
        to_set(*[int(sections) for sections in elf_assignment.split("-")])
        for elf_assignment in line.split(",")
    ]

def is_one_subset_of_the_other(sets):
    return sets[0].issubset(sets[1]) or sets[0].issuperset(sets[1])


def is_intersecting(sets):
    return len(sets[0].intersection(sets[1])) > 0 


def part_1(lines):
    subsets = filter(
        is_one_subset_of_the_other,
        [parse(line) for line in lines],
    )

    print(f"Part_1: {len(list(subsets))}")


def part_2(lines):
    subsets = filter(
        is_intersecting,
        [parse(line) for line in lines],
    )
    print(f"Part_2: {len(list(subsets))}")
