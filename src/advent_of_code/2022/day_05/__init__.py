import copy


def parse_input(input):
    stacks = None
    instructions = list()

    lines = list(map(lambda l: l.replace("\n", ""), input.readlines()))
    empty_line_index = lines.index("")

    stacks_input = lines[: empty_line_index - 1]
    instructions_input = lines[empty_line_index + 1 :]

    stacks = [[] for x in list(range((len(stacks_input[0]) // 4 + 1)))]

    stacks_count = len(stacks)

    for stack_input in stacks_input:
        for i in list(range(stacks_count)):
            crate = stack_input[i * 4 + 1]
            if crate == " ":
                continue

            stacks[i].append(crate)

    for instructions_line in instructions_input:
        _, move, __, from_, ___, to = instructions_line.split(" ")
        instructions.append([int(move), int(from_) - 1, int(to) - 1])

    return stacks, instructions


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)


def reverse(list):
    list.reverse()
    return list


def part_1(data):
    stacks, instructions = data
    stacks = copy.deepcopy(stacks)

    for move, from_, to in instructions:
        stacks[to] = reverse(stacks[from_][:move]) + stacks[to]
        del stacks[from_][:move]

    print("Part_1", "".join([stack[0] for stack in stacks]))


def part_2(data):
    stacks, instructions = data
    stacks = copy.deepcopy(stacks)

    for move, from_, to in instructions:
        stacks[to] = stacks[from_][:move] + stacks[to]
        del stacks[from_][:move]

    print("Part_2", "".join([stack[0] for stack in stacks]))
