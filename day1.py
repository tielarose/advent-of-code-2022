import sys


def calculate_most_calories(filepath):
    """given a file of calories carried by elves, return the greatest number of calories

    input format:
        one integer per line
        blank lines represent a new elf"""

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
