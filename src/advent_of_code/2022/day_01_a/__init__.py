def run(challenge_input):
    line = challenge_input.readline()

    calories = 0
    max_calories = 0
    while line != "":
        trimmed_line = line.rstrip()

        line = challenge_input.readline()

        if trimmed_line == "":
            calories = 0
            continue
        else:
            calories += int(trimmed_line)

        max_calories = max(calories, max_calories)

    print(f"Max calories: {max_calories}")
