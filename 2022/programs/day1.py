"""
Day 1 of Advent of Code:
Find the maximum number of calories one Elf is carrying
"""

# import numpy as np
from pathlib import Path

FILENAME = Path("01.txt")
PATH = Path("2022/inputs/")


def main():
    """Find the maximum number of calories one Elf is carrying"""
    elves = []
    sum_elf = 0

    with open(PATH/FILENAME, 'r') as f:
        for line in f:

            if line != '\n':
                value = int(line.strip())
                sum_elf += value
            else:
                elves.append(sum_elf)
                sum_elf = 0

    print(max(elves))

if __name__=="__main__":
    main()
