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


def sum_common_keys(filepath):
    # iterate over the file, get every 3 lines
    # find the common item in those 3 lines
    # convert that item to a priority/number
    # add that to the total
