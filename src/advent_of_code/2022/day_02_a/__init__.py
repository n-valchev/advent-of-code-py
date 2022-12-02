ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

play_map = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

def _calc_round(opponent, me):
    outcome = LOSE
    if me - opponent == 1 or me - opponent == -2:
        outcome = WIN
    elif me == opponent:
        outcome = DRAW

    return outcome + me

def run(input):
    lines = input.readlines()

    result = 0
    for line in lines:
        opponent, me = line.rstrip().split(" ")
        result += _calc_round(play_map[opponent], play_map[me])

    print(f"Points: {result}")
