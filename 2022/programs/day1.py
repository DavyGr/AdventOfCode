"""
Day 1 of Advent of Code:
Find the maximum number of calories elves are carrying
"""

from pathlib import Path
import numpy as np

FILENAME = Path("01.txt")
PATH = Path("2022/inputs/")


def find_maximum_calories():
    """Find the maximum number of calories elves are carrying"""
    elves = np.array([])
    sum_elf = 0

    with open(PATH/FILENAME, 'r') as f:
        for line in f:

            if line != '\n':
                value = int(line.strip())
                sum_elf += value
            else:
                elves = np.append(elves, sum_elf)
                sum_elf = 0

    # If the input_file doesn't end with an empty line ('\n'), then the last value still needs
    # to be appended:
    if sum_elf > 0:
        elves = np.append(elves, sum_elf)

    print("Maximum of top 1 elf:", elves.max())

    # Part 2
    top_n = 3
    elves_sorted = np.sort(elves)[::-1]

    print("Maximum of top 3 elves:", np.sum(elves_sorted[:top_n]))

def main():
    find_maximum_calories()

if __name__=="__main__":
    main()
