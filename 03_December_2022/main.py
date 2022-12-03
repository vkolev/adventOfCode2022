import os
import string

from typing import List

WEIGHTS = {letter: weight for weight, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as f:
        for line in f.readlines():
            yield line.strip()

def get_common(first: str, second: str):
    intersection = ""
    for x in first:
        if x in second and x not in intersection:
            intersection += x
    return intersection


def get_common_two(group: List[str]) -> str:
    intersection = ""
    for x in group[0]:
        if x in group[1] and x in group[2] and x not in intersection:
            intersection += x
    return intersection


def calculate_weights(rucksack: str) -> int:
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    return WEIGHTS[get_common(first, second)]


def split_by(rucksacks: List[str], splitter: int):
    for line_num in range(0, len(rucksacks), splitter):
        yield rucksacks[line_num:line_num+splitter]


def calculate_weights_two(rucksack_group: List[str]):
    return WEIGHTS[get_common_two(rucksack_group)]  


def main():
    rucksacks = list(load_file())
    sum_first = 0
    for rucksack in rucksacks:
        sum_first += calculate_weights(rucksack)
    sum_second = 0
    for rucksack_group in split_by(rucksacks, 3):
        sum_second += calculate_weights_two(rucksack_group)
    print(f"First solution: {sum_first}")
    print(f"Second solution: {sum_second}")

if __name__ == "__main__":
    main()
