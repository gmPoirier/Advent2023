# Advent of Code 2023: Star 07
#=============================

import math
import re

def parse(line):
    num = re.compile("[0-9]+")

    card_id = -1
    winning_numbers = []
    my_numbers = []

    numbers_split = line.split("|")
    my_numbers = num.findall(numbers_split[1])

    id_split = numbers_split[0].split(":")
    card_id = id_split[0]
    winning_numbers = num.findall(id_split[1])

    return (card_id, winning_numbers, my_numbers)

def count_matches(list_a, list_b):
    matches = []

    for item_a in list_a:
        for item_b in list_b:
            if item_a == item_b:
                matches.append(item_a)
    
    print(matches)
    return len(matches)

def main():
    file = open("input/day_04.txt", "r", encoding="utf-8")
    total_points = 0

    for line in file:

        data = parse(line)
        card_id = data[0]
        winning_numbers = data[1]
        my_numbers = data[2]

        num_matches = count_matches(winning_numbers, my_numbers)
        if num_matches > 0:
            total_points += math.pow(2, num_matches - 1)

    print(total_points)
    file.close()
    return 0

if __name__ == "__main__":
    main()
