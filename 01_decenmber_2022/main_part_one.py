import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def read_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as f:
        test = f.read()
        return test.split("\n\n")


def main():
    lines = list(map(lambda x: sum([int(i) for i in x.split("\n") if i != ""]), read_file()))
    print(max(lines))


if __name__ == "__main__":
    main()