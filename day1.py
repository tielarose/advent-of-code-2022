
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


###########
# seema solution
###########

# open the file
with open("day1_input.txt") as file:
    # since elves are separated by two blank lines, put each elf into a string
    # know it's a new string when you see two newline characters
    elves = file.read().strip().split("\n\n")
    # elves now looks like this ['1000\n2000\n3000', '4000', '5000\n6000', '7000\n8000\n9000', '10000']

# split each elf-string into a list of integers
elves = [[int(n) for n in num_string.split("\n")] for num_string in elves]
# elves now looks like this [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

# sum each sub-array
calories = [sum(amounts) for amounts in elves]


part_1 = max(calories)
part_2 = sum(sorted(calories)[-3:])

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
