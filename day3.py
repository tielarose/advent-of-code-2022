# each line is one rucksack
# the first half of the items is in compartment 1, 2nd half is compartment 2
# find the item that is in both compartments
# translate that to a priority
# add the priorities together

def create_priorities_key():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    priorities_key = {}

    priority = 1
    for char in alphabet:
        priorities_key[char] = priority
        priority += 1

    for char in alphabet:
        priorities_key[char.upper()] = priority
        priority += 1

    return priorities_key


def sum_priorities(filepath):
    priorties_key = create_priorities_key()

    file = open(filepath)

    priorities_total = 0

    for line in file:
        line = [*line.rstrip()]
        middle_ind = int(len(line) / 2)
        compartment1 = set(line[0:middle_ind])
        compartment2 = set(line[middle_ind:])
        shared_item_set = compartment1 & compartment2
        shared_item = shared_item_set.pop()
        priorities_total += priorties_key[shared_item]

    return priorities_total


# part 2

with open("day3_input.txt") as file:
    # put each elf string into a list
    elves = file.read().strip().split("\n")

    # group the elves into 3
    elf_groups = [elves[i:i+3] for i in range(0, len(elves), 3)]

    # find the common item in those 3 lines
    badges = [(set(elf_group[0]) & set(elf_group[1]) & set(elf_group[2]))
              for elf_group in elf_groups]

    priorities_key = create_priorities_key()

    # convert that item to a priority/number
    priorities = [priorities_key[item.pop()] for item in badges]

    print(f'Part 2 answer: {sum(priorities)}')

[['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'],
    ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']]
