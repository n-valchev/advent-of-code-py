def parse_input(input):
    return input


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)


def add_visited(visited, pos):
    visited.add(f"[{pos[0]},{pos[1]}]")


def move_step(direction):
    if direction == "L":
        return [-1, 0]

    if direction == "R":
        return [1, 0]

    if direction == "U":
        return [0, -1]

    return [0, 1]


def move(current_pos, move_dir):
    return [current_pos[0] + move_dir[0], current_pos[1] + move_dir[1]]


def move_component(component):
    if component == 0:
        return 0
    if component > 0:
        return 1

    return -1


def follow_dir(knot, next_knot):
    x_dist = knot[0] - next_knot[0]
    y_dist = knot[1] - next_knot[1]

    return (
        None
        if abs(x_dist) <= 1 and abs(y_dist) <= 1
        else [move_component(x_dist), move_component(y_dist)]
    )


def move_knot(knots, index, move_direction):
    original_position = knots[index]
    knots[index] = move(knots[index], move_direction)

    if index + 1 == len(knots):
        return

    move_direction = follow_dir(knots[index], knots[index + 1])

    if move_direction == None:
        return

    return move_knot(knots, index + 1, move_direction)


def get_tail_pos(input, knots_count):
    input.seek(0)
    visited = set()

    knots = [[0] * 2 for _ in range(knots_count)]

    add_visited(visited, [0, 0])

    for line in input.readlines():
        direction, steps = line.rstrip().split(" ")
        steps = int(steps)

        for step in range(steps):
            tail_pos = knots[-1]
            move_knot(knots, 0, move_step(direction))

            if tail_pos != knots[-1]:
                add_visited(visited, knots[-1])
    
    return len(visited)


def part_1(data):
    print("Part_1", get_tail_pos(data, 2) )

def part_2(data):
    print("Part_2", get_tail_pos(data, 10) )
