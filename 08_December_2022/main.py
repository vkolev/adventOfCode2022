
import os
from typing import List

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.strip()

def create_grid(lines: List[str]) -> List[List[int]]:
    return [[int(x) for x in line] for line in lines]

def create_considered_grid(grid: List[List[int]]):
    return [x[1:-1] for x in grid[1:-1]]

def get_column(grid, column):
    return [x[column] for x in grid]

def is_visible(grid, row, column):
    element = grid[row][column]
    left = grid[row][:column]
    right = grid[row][column+1:]
    top = get_column(grid, column)[:row]
    bottom = get_column(grid, column)[row+1:]
    #return element > max(left) and element > max(right) and element > max(top) and element > max(bottom)
    # left
    if element > max(left):
        return True
    # Right
    if element > max(right):
        return True
    # Bottom
    if element > max(bottom):
        return True
    # Top
    if element > max(top):
        return True
    return False

def count_edge(grid_size):
    return grid_size * 2 + ((grid_size - 2)*2) 
    

def count_visible_trees(possible_grid: List[List[int]], full_grid: List[List[int]]) -> int:
    count = count_edge(len(full_grid))
    for row in range(len(possible_grid)):
        for column in range(len(possible_grid[row])):
            if is_visible(full_grid, row+1, column+1):
                count += 1
    return count

def single_score(row: List[int], element: int):
    count = 0
    for item in row:
        if item < element:
            count += 1
        else:
            count += 1
            break
    return count

def get_scenic_score(grid, row, column):
    element = grid[row][column]
    left_score = single_score(grid[row][:column][::-1], element)
    right_score = single_score(grid[row][column+1:], element)
    top_score = single_score(get_column(grid, column)[:row][::-1], element)
    bottom_score = single_score(get_column(grid, column)[row+1:], element)
    return left_score * right_score * top_score * bottom_score


def highest_scenic_score(possible_grid: List[List[int]], full_grid: List[List[int]]) -> int:
    scores = []
    for row in range(len(possible_grid)):
        for column in range(len(possible_grid[row])):
            scores.append(get_scenic_score(full_grid, row+1, column+1))
    return max(scores)


def main():
    lines = list(load_file())
    grid = create_grid(lines)
    considered_grid = create_considered_grid(grid)
    sum = count_visible_trees(considered_grid, grid)
    sum_two = highest_scenic_score(considered_grid, grid)
    print("Visible trees: ", sum)
    print("Highest scenic score: ", sum_two)


if __name__ == "__main__":
    main()
