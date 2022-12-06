
import os
from typing import List

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.strip()

def get_marker(line: str, chunk_size: int) -> int:
    for index in range(0, len(line) - chunk_size):
        if len(set(line[index:index + chunk_size])) == chunk_size:
            return index + chunk_size


def main():
    lines = list(load_file())
    for line in lines:
        print("First marker: ", get_marker(line, 4))
        print("Second marker: ", get_marker(line, 14))


if __name__ == "__main__":
    main()
