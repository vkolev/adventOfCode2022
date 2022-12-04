import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def read_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as f:
        test = f.read()
        return test.split("\n\n")


def main():
    lines = list(map(lambda x: sum([int(i) for i in x.split("\n") if i != ""]), read_file()))
    total = 0
    for i in range(3):
        max_value = max(lines)
        total += max_value
        lines.pop(lines.index(max_value))
    print(total)


if __name__ == "__main__":
    main()