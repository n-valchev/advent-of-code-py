LEFT = ">"
DOWN = "v"
EMPTY = "."


def run(input):
    calculator = CucumberTurnsCalculation(input.read())

    turns = calculator.calc()

    print(f"Turns: {turns}")


class CucumberTurnsCalculation:
    def __init__(self, input):
        self.empty_spaces = list()
        self.moved_left = list()
        self.moved_down = list()

        self._init_area(input)

    def _init_area(self, input):
        lines = input.splitlines()

        self.height = len(lines)
        self.width = len(lines[0])

        area = list()

        for row, line in enumerate(lines):
            line_chars = list()

            for col, char in enumerate(line):
                line_chars.append(char)
                if char == ".":
                    self.empty_spaces.append([row, col])

            area.append(line_chars)

        self.area = area

    def calc(self):
        moved = True
        turns = 0

        while moved:
            turns += 1
            moved = self.move_all_direction(self.move_from_left, LEFT)

            moved = self.move_all_direction(self.move_from_up, DOWN) or moved

        return turns

    def move_from_left(self, row, col):
        nextCol = col - 1

        nextCol = nextCol if nextCol >= 0 else self.width - 1
        return [row, nextCol]

    def move_from_up(self, row, col):

        nextRow = row - 1
        nextRow = nextRow if nextRow >= 0 else self.height - 1

        return [nextRow, col]

    def move_all_direction(self, moveFn, sea_cucumber_symbol):
        new_spaces = list()
        moved_cucumbers = list()
        moved = False

        for row, col in self.empty_spaces:
            fromRow, fromCol = moveFn(row, col)

            if self.area[fromRow][fromCol] == sea_cucumber_symbol:
                moved_cucumbers.append([row, col])
                self.area[fromRow][fromCol] = EMPTY

                new_spaces.append([fromRow, fromCol])

                moved = True
            else:
                new_spaces.append([row, col])

        self.empty_spaces = new_spaces

        for row, col in moved_cucumbers:
            self.area[row][col] = sea_cucumber_symbol


        return moved

    def print_area(self, turn):
        print(f"\n\nAfter {turn} turns:\n")
        for row in self.area:
            print("".join(row))
