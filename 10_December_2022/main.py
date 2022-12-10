
import os
from typing import List

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.strip()

def create_groups(lines: List[str], group_size):
    for line_num in range(0, len(lines), group_size):
        yield lines[line_num:line_num+group_size]


def main():
    lines = list(load_file())
    result = [-1]
    current_result = 1
    final_result = 0
    for line in lines:
        if line == "noop":
            result.append(current_result)
        else:
            result.append(current_result)
            result.append(current_result)
            current_result += int(line.split(" ")[1])
    for i in range(20, 221, 40):
        check_result = result[i] * i
        final_result += check_result
    print("Part one: ", final_result)

    print("Part two: ")
    for i in range(1, 241, 40):
            l = ""
            for j in range(i, i + 40):
                
                if abs(result[j] - (j - 1) % 40) < 2:
                    l += "#"
                else:
                    l += "."
            print(l)



if __name__ == "__main__":
    main()
