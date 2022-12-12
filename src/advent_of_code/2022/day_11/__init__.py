import re


def parse_monkey_id(monkey_line):
    x = re.search("^Monkey (\d+):$", monkey_line)
    return int(x.group(1))


def parse_starting_items(starting_items_line):
    _, items = starting_items_line.split(":")

    return [int(item) for item in items.rstrip().strip().split(", ")]


def mult(a, b):
    return a * b

def sum(a, b):
    return a + b

def parse_operand(operand, item):
    return item if operand == "old" else int(operand)


def parse_operation(operation_line):
    _, operation_expression = operation_line.split("=")

    operandA, operator, operandB = operation_expression.rstrip().strip().split(" ")

    fn = sum if operator == "+" else mult

    def inspect(item):
        return fn(parse_operand(operandA, item), parse_operand(operandB, item))

    return inspect


def last_number(line):
    return int(line.rstrip().split(" ")[-1])

def create_monkey(input, worry_relaxer):
    monkey_id = parse_monkey_id(input.readline())
    items = parse_starting_items(input.readline())
    inspection = parse_operation(input.readline())
    divider = last_number(input.readline())
    if_true_monkey = last_number(input.readline())
    if_false_monkey = last_number(input.readline())

    return Monkey(monkey_id, items, inspection, divider, if_true_monkey, if_false_monkey, worry_relaxer)


class Monkey:
    def __init__(self, id, starting_items, inspect, divider, true_monkey, false_monkey , worry_relaxer) -> None:
        self.id = id
        self.items = starting_items
        self.inspect = inspect
        self.divider = divider
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.worry_relaxer = worry_relaxer

        self.inspected = 0

    def process_item(self):
        if len(self.items) == 0:
            return (-1, -1)

        item_after_inspection = self.inspect(self.items.pop(0)) // self.worry_relaxer
        self.inspected += 1

        return self.test(item_after_inspection)

    def receive_item(self, item):
        self.items.append(item)

    def test(self, item):
        monkey = self.true_monkey if item % self.divider == 0 else self.false_monkey

        return [monkey, item]



def parse_input(input, worry_relaxer):
    input.seek(0)
    monkeys = dict()

    while True:
        monkey = create_monkey(input, worry_relaxer)
        monkeys[monkey.id] = monkey

        skip_line = input.readline()
        if skip_line == "":
            break

    return monkeys


def run(file):
    part_1(file)
    part_2(file)

def part_1(input):
    monkeys = parse_input(input, 3)
    for rounds in range(20):
        for monkey_id in range(len(monkeys)):
            while True:
                to_monkey, item = monkeys[monkey_id].process_item()
                if to_monkey == -1:
                    break

                monkeys[to_monkey].receive_item(item)

    processed_items = [monkey.inspected for monkey in monkeys.values()]
    processed_items.sort(
        reverse=True
    )

    print("Part_1", processed_items[0] * processed_items[1])


def part_2(input):
    monkeys = parse_input(input, 1)

    reducer = 1
    for monkey in monkeys.values():
        if (reducer % monkey.divider != 0):
            reducer *= monkey.divider

    for rounds in range(10000):
        for monkey_id in range(len(monkeys)):
            while True:
                to_monkey, item = monkeys[monkey_id].process_item()
                if to_monkey == -1:
                    break

                monkeys[to_monkey].receive_item(item % reducer)

    processed_items = [monkey.inspected for monkey in monkeys.values()]
    processed_items.sort(
        reverse=True
    )

    print("Part_2", processed_items[0] * processed_items[1])
