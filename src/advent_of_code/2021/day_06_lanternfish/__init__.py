import math


def run(input):
    fishes_cycle = list(map(int, input.read().split(",")))

    cycle_fishes = [0] * 7

    for cycle in fishes_cycle:
        cycle_fishes[cycle] += 1

    days = 256
    newborn_maturing_bucket = [0] * 2

    for day in range(days):
        giving_birth = cycle_fishes.pop(0)
        newborn = giving_birth
        cycle_fishes.append(giving_birth + newborn_maturing_bucket.pop(0))
        newborn_maturing_bucket.append(newborn)

    print(f"population: {sum([sum(cycle_fishes), sum(newborn_maturing_bucket)])}")
