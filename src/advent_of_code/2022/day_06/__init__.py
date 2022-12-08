def parse_input(input):
    return input.read()


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)



def part_1(data):
    queue = list()

    for i, letter in enumerate(data):
        letter_index = queue.index(letter) if letter in queue else -1
        if letter_index != -1:
            del queue[:letter_index + 1]

        queue.append(letter)

        if len(queue) == 4:
            print("Part_1", i + 1)
            break


def part_2(data):

    queue = list()

    for i, letter in enumerate(data):
        letter_index = queue.index(letter) if letter in queue else -1
        if letter_index != -1:
            del queue[:letter_index + 1]

        queue.append(letter)

        if len(queue) == 14:
            print("Part_1", i + 1)
            break
