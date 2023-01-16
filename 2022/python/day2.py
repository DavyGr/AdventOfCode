"""
Day 2 of Advent of Code:
Number of points for Rock Paper Scissors contest
"""

from pathlib import Path
# To improve performance: combine part1 and part2 functions so the file has to be read only once,
# instead of twice.

FILENAME = Path("02.txt")
PATH = Path("2022/inputs/")

def part1():
    """Number of points for Rock Paper Scissors contest part 1"""
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

    return score

def part2():
    """Number of points for Rock Paper Scissors contest part 2"""
    score = 0

    # points from the action chosen:
    score_action_dict = {'A X': 3, 'A Y': 1, 'A Z': 2,
                         'B X': 1, 'B Y': 2, 'B Z': 3,
                         'C X': 2, 'C Y': 3, 'C Z': 1}

    # points from the win/draw/lose outcome:
    score_win_dict = {'X': 0, 'Y': 3, 'Z': 6}

    with open(PATH/FILENAME, 'r') as f:
        for line in f:
            # points from the action chosen:
            action_list = line.split()
            score += score_action_dict[line.strip()]

            # points from the win/draw/lose outcome:
            score += score_win_dict[action_list[1]]

    return score

def main():
    print(part1())
    print(part2())

if __name__=="__main__":
    main()
