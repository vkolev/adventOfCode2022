import os
from typing import List

score_table_one = {
    "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6
}

score_table_two = {
    "A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7
}

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_file() -> List:
    with open(os.path.join(BASE_DIR, "input.txt")) as f:
        lines = f.readlines()
        return lines


def main():
    draws = load_file()
    sum_first = 0
    sum_second = 0
    for draw in draws:
        sum_first += score_table_one[draw.strip()]
        sum_second += score_table_two[draw.strip()]
    print(f"First strategy {sum_first}")
    print(f"Second strategy {sum_second}")

if __name__ == "__main__":
    main()