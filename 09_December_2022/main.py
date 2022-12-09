
import os
from typing import List, Tuple

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.strip()


def main():
    tail_visits = [(0, 0)]
    tail_position = (0, 0)
    head_position = (0, 0)
    for line in load_file():
        direction, steps = line.split(" ")
        for i in range(int(steps)):
            if direction == "D":
                head_position = (head_position[0], head_position[1] - 1)
                if head_position[1] <= tail_position[1] - 2:
                    tail_position = (tail_position[0], tail_position[1] - 1)
                    if head_position[0] != tail_position[0]:
                        tail_position = (head_position[0], tail_position[1])
            if direction == "U":
                head_position = (head_position[0], head_position[1] + 1)
                if head_position[1] >= tail_position[1] + 2:
                    tail_position = (tail_position[0], tail_position[1] + 1)
                    if head_position[0] != tail_position[0]:
                        tail_position = (head_position[0], tail_position[1])
            if direction == "L":
                head_position = (head_position[0] - 1, head_position[1])
                if head_position[0] <= tail_position[0] - 2:
                    tail_position = (tail_position[0] - 1, tail_position[1])
                    if head_position[1] != tail_position[1]:
                        tail_position = (tail_position[0], head_position[1])
            if direction == "R":
                head_position = (head_position[0] + 1, head_position[1])
                if head_position[0] >= tail_position[0] + 2:
                    tail_position = (tail_position[0] + 1, tail_position[1])
                    if head_position[1] != tail_position[1]:
                        tail_position = (tail_position[0], head_position[1])
            tail_visits.append(tail_position)
    print("Total unique visits tail: ", len(set(tail_visits)))


def distance(position1: Tuple, position2: Tuple) -> int:
    if abs(position1[0] - position2[0]) > 1:
        return 2 if position1[1] != position2[1] else 1
    elif abs(position1[1] - position2[1]) > 1:
        return 2 if position1[0] != position2[0] else 1
    return 0



def get_positions(positions: List[Tuple]) -> List[Tuple]:
    for i in range(1, 10):
        dist = distance(positions[i], positions[i - 1])
        if dist == 2:
            positions[i] = (positions[i][0] + 1 if positions[i - 1][0] > positions[i][0] else positions[i][0] - 1, 
                            positions[i][1] + 1 if positions[i - 1][1] > positions[i][1] else positions[i][1] - 1)
        elif dist == 1:
            if positions[i][0] == positions[i - 1][0]:
                positions[i] = (positions[i][0], positions[i][1] + 1 if positions[i - 1][1] > positions[i][1] else positions[i][1] - 1)
            else:
                positions[i] = (positions[i][0] + 1 if positions[i - 1][0] > positions[i][0] else positions[i][0] - 1, positions[i][1])
    return positions


def main_two():
    positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    tail_position = []
    for line in load_file():
        head_position = positions[0]
        direction, steps = line.split(" ")
        for i in range(int(steps)):
            if direction == "D":
                head_position = (head_position[0], head_position[1] -1)
                positions[0] = head_position
                positions = get_positions(positions)
            if direction == "U":
                head_position = (head_position[0], head_position[1] + 1)
                positions[0] = head_position
                positions = get_positions(positions)
            if direction == "L":
                head_position = (head_position[0] - 1, head_position[1]) 
                positions[0] = head_position
                positions = get_positions(positions)
            if direction == "R":
                head_position = (head_position[0] + 1, head_position[1])
                positions[0] = head_position
                positions = get_positions(positions)
            tail_position.append(positions[-1])
    print("Tail positions: ", len(set(tail_position)))


if __name__ == "__main__":
    main()
    main_two()
