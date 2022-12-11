def parse_input(input):
    return input


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)


def part_1(data):
    data.seek(0)

    cycles = 1
    next_cycle = 20
    sign_cycles = [60, 100, 140, 180, 220]
    sum = 1
    sign_sum = 0

    for line in data.readlines():
        instr = line.rstrip().split(" ")

        if instr[0] == "noop":
            cycles += 1
        else:
            cycles += 2

        x = 0 if (len(instr) == 1) else int(instr[1])
        sum += x

        if cycles >= next_cycle:
            sign_sum += next_cycle * (sum if cycles - next_cycle == 0 else sum - x)
            if len(sign_cycles) == 0:
                break

            next_cycle = sign_cycles.pop(0)

    print("Part_1", sign_sum)


def draw_pixel(pixels, sprite_pos, cycle):
    cycle -= 1
    col = cycle % 40

    pixels[cycle] = pixels[cycle] and (col >= sprite_pos and col <= sprite_pos + 2)


def part_2(data):
    data.seek(0)

    pixels = [1] * 240

    sprite_pos = 0
    cycle = 0

    for line in data.readlines():
        instr = line.rstrip().split(" ")

        cycle += 1
        draw_pixel(pixels, sprite_pos, cycle)

        if instr[0] == "noop":
            continue

        cycle += 1
        draw_pixel(pixels, sprite_pos, cycle)

        sprite_pos += int(instr[1])


    rows = len(pixels) // 40
    for row in range(rows):
        row_values = pixels[row * 40 : (row + 1) * 40]

        print("".join(list(map(lambda x: "#" if x else ".", row_values))))
