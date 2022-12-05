
from collections import defaultdict
import os
import re
from typing import List, Dict, Tuple

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Stack:
    def __init__(self, input_matrix: List[str]):
        self.columns = self.create_columns(input_matrix)

    def create_columns(self, input_matrix: List[str]) -> Dict[str, List[str]]:
        result = defaultdict()
        for key in input_matrix[len(input_matrix) - 1:][0].split('   '):
            result[key.strip()] = []
        for line in input_matrix[:len(input_matrix) - 1]:
            list_values = list(self.__create_chunks(line + " "))
            for index, item in enumerate(list_values):
                new_item = item.strip()
                if new_item != "":
                    result[str(index + 1)].insert(0, new_item.replace("[", "").replace("]", ""))
        return result

    def __create_chunks(self, line):
        for chunk in range(0, len(line), 4):
            yield line[chunk:chunk+4]

    def perform_moves(self, repeats: int, start: str, stop: str):
        for r in range(repeats):
            self.columns[stop].append(self.columns[start].pop())
    
    def perform_moves_preserve(self, repeats: int, start: str, stop: str):
        temp = []
        for r in range(repeats):
            temp.append(self.columns[start].pop())
        temp.reverse()
        self.columns[stop] += temp

    def print_result(self):
        return "".join([col[-1] for index, col in self.columns.items()])


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.replace("\n", "")


def get_moves(lines: List[str]) -> List[Tuple]:
    for line in lines:
        temp = re.findall(r"\d+", line)
        yield tuple(map(int, temp))


def main():
    lines = list(load_file())
    stack = Stack(lines[:9])
    for move in get_moves(lines[10:]):
        stack.perform_moves(move[0], str(move[1]), str(move[2]))
    print(stack.print_result())

def main_two():
    lines = list(load_file())
    stack = Stack(lines[:9])
    for move in get_moves(lines[10:]):
        stack.perform_moves_preserve(move[0], str(move[1]), str(move[2]))
    print(stack.print_result())


if __name__ == "__main__":
    print("First strategy: ")
    main()
    print("Second strategy: ")
    main_two()
