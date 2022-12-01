
def run(input):
    increments = 0
    measure, *measures = input.read().splitlines()

    for currentMeasure in measures:
        increments += 1 if currentMeasure > measure else 0
        measure = currentMeasure

    print(f'Increments: {increments}')