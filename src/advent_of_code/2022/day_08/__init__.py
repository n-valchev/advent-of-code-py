def parse_input(input):
    grid = list()
    for line in input.readlines():
        row = list()
        for char in line.rstrip():
            row.append(int(char))

        grid.append(row)

    return grid


def run(file):
    data = parse_input(file)

    part_1(data)
    part_2(data)


def get_visible_internal_trees(grid):
    all_internal_visible_trees = set()
    width = len(grid[0])
    height = len(grid)

    max_column_trees = [*grid[0]]
    max_col_tree_reversed = [*grid[-1]]

    for y, row in enumerate(grid[1:-1]):
        last_max = row[0]
        last_max_reversed = row[-1]

        row_index = y + 1
        reverse_row_index = height - row_index - 1

        for x, _ in enumerate(row[1:-1]):
            col_index = x + 1
            reverse_col_index = width - col_index - 1

            # left
            if row[col_index] > last_max:
                last_max = row[col_index]
                all_internal_visible_trees.add(f"{row_index},{col_index}")

            # top
            if row[col_index] > max_column_trees[col_index]:
                max_column_trees[col_index] = row[col_index]
                all_internal_visible_trees.add(f"{row_index},{col_index}")

            # right
            if row[reverse_col_index] > last_max_reversed:
                last_max_reversed = row[reverse_col_index]
                all_internal_visible_trees.add(f"{row_index},{reverse_col_index}")

            # bottom
            if grid[reverse_row_index][col_index] > max_col_tree_reversed[col_index]:
                max_col_tree_reversed[col_index] = grid[reverse_row_index][col_index]
                all_internal_visible_trees.add(f"{reverse_row_index},{col_index}")

    return all_internal_visible_trees


def part_1(data):
    internal_trees = get_visible_internal_trees(data)

    print("Part_1", len(internal_trees) + len(data) * 2 + len(data[0]) * 2 - 4)


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def multiply_viewing_distance(grid, viewing_distance_matrix):

    for row_index, row in enumerate(grid):
        weights_positions = [-1] * 10
        
        for col_index, tree_height in enumerate(row):
            last_visible_position = max(weights_positions[tree_height:])
            viewing_distance_matrix[row_index][col_index] *= (col_index - last_visible_position)

            weights_positions[tree_height] = col_index

def flatten(l):
    return [item for sublist in l for item in sublist]

def part_2(grid):
    # edges are insignificant
    grid = grid[1:-1]
    grid = [row[1:-1] for row in grid]

    width = len(grid[0])
    height = len(grid)

    matrix = [[1] * width for _, __ in enumerate(range(height))]

    multiply_viewing_distance(grid, matrix)

    grid = rotated(grid)
    matrix = rotated(matrix)
    multiply_viewing_distance(grid, matrix)
    
    grid = rotated(grid)
    matrix = rotated(matrix)
    multiply_viewing_distance(grid, matrix)

    grid = rotated(grid)
    matrix = rotated(matrix)
    multiply_viewing_distance(grid, matrix)

    print("Part_2", max(flatten(matrix)))

