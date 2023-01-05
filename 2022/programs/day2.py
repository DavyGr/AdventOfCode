"""
Day 2 of Advent of Code:
Number of points for Rock Paper Scissors contest
"""

from pathlib import Path
# import numpy as np

FILENAME = Path("02.txt")
PATH = Path("2022/inputs/")


def main():
    """Number of points for Rock Paper Scissors contest"""
    score = 0

    # points from the action chosen:
    score_action_dict = {'X': 1, 'Y': 2, 'Z': 3}

    # points from the win/draw/lose outcome:
    score_win_dict = {'A X': 3, 'A Y': 6, 'A Z': 0,
                      'B X': 0, 'B Y': 3, 'B Z': 6,
                      'C X': 6, 'C Y': 0, 'C Z': 3}

    with open(PATH/FILENAME, 'r') as f:
        for line in f:
            # points from the action chosen:
            action_list = line.split()
            score += score_action_dict[action_list[1]]

            # points from the win/draw/lose outcome:
            score += score_win_dict[line.strip()]

    print(score)

if __name__=="__main__":
    main()
