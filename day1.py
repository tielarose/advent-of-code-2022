
def calculate_most_calories(filepath):
    """given a file of calories carried by elves, return the greatest number of calories

    input example:
        1000
        2000

        3000

        450
        3000

        blank lines represent a new elf; in the example above:
        the first elf is carrying 3000 calories (1000+2000)
        the second elf is carrying 3000 calories
        the third elf is carrying 3450 calories

        this function would return the integer 3450"""

    file = open(filepath)

    curr_total = 0
    max_total = 0

    for line in file:
        line = line.rstrip()

        if line == '':
            if curr_total > max_total:
                max_total = curr_total
            curr_total = 0
            continue

        curr_total += int(line)

    return max_total


def calculate_sum_of_top_3_most_calories(filepath):
    """given a file of calories carried by elves, return the sum of the top 3 most calories carried

    input example:
        1000
        2000

        3000

        450
        3000

        2000

        blank lines represent a new elf; in the example above:
            elf 1: 3000
            elf 2: 3000
            elf 3: 3450
            elf 4: 2000

        this function would return the integer 9450 (3000 + 3000 + 3450)"""

    file = open(filepath)

    curr_total = 0
    list_of_calories_carried = []

    for line in file:
        line = line.rstrip()

        if line == '':
            list_of_calories_carried.append(curr_total)
            curr_total = 0
            continue

        curr_total += int(line)

    list_of_calories_carried.sort()

    return sum(list_of_calories_carried[-3:])
