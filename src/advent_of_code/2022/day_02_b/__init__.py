ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

lose_win_map = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

win_lose_map = {v: k for k, v in lose_win_map.items()}

outcome_map = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

play_map = { 
   "A": ROCK,
   "B": PAPER,
   "C": SCISSORS,
}

def _calc_round(opponent, outcome):
    me = 0

    if outcome == DRAW:
        me = opponent

    elif outcome == WIN:
        me = lose_win_map[opponent]

    else:
        me = win_lose_map[opponent]

    return outcome + play_map[me]

def run(input):
    lines = input.readlines()

    result = 0
    for line in lines:
        opponent, me = line.rstrip().split(' ')
        result += _calc_round(opponent, outcome_map[me])

    print(f"Points: {result}")