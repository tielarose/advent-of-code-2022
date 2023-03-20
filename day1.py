import sys


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


# print(calculate_most_calories(sys.argv[1]))
