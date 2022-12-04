
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for line in file.readlines():
            yield line.strip()

def compare_sections(line: str) -> int:
    first = line.split(',')[0].split('-')
    first_list = list(range(int(first[0]), int(first[1])+1))
    second = line.split(',')[1].split('-')
    second_list = list(range(int(second[0]), int(second[1])+1))
    if set(first_list).issubset(set(second_list)):
        return 1
    if set(second_list).issubset(set(first_list)):
        return 1
    return 0


def compare_section_two(line: str) -> int:
    first = line.split(',')[0].split('-')
    first_list = list(range(int(first[0]), int(first[1])+1))
    second = line.split(',')[1].split('-')
    second_list = list(range(int(second[0]), int(second[1])+1))
    intersection = set(first_list) & set(second_list)
    if len(intersection) > 0:
        return 1
    return 0


def main():
    lines = list(load_file())
    sum = 0
    sum_two = 0
    for line in lines:
        sum += compare_sections(line)
        sum_two += compare_section_two(line)
    print(f"Total overlapping sections: {sum}")
    print(f"Total overlapping sections two: {sum_two}")

if __name__ == "__main__":
    main()
