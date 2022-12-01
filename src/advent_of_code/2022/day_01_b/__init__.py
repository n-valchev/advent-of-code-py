def run(challenge_input):
    line = challenge_input.readline()

    calories = 0
    max_calories = 0

    top_3 = [0]*3

    while line != "":
        trimmed_line = line.rstrip()

        line = challenge_input.readline()

        if trimmed_line == "":
            insert_if_in_top_3(calories, top_3)
            calories = 0
            continue
        else:
            calories += int(trimmed_line)


    if (calories > 0):
        insert_if_in_top_3(calories, top_3)

    print(f"Top 3 total: {sum(top_3)}")
    print(f"Top 3 : {top_3}")

def insert_if_in_top_3(calories, sorted_top_3):
    if (calories < sorted_top_3[0]): 
        return

    sorted_top_3.pop(0)

    index = 2
    for i, val in enumerate(sorted_top_3):
        if (val > calories):
            index = i
            break

    sorted_top_3.insert(index, calories)
         
    

