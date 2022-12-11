
from collections import deque
from math import lcm
import os
from typing import List

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Monkey:
    def __init__(self, monkey_id: str, items: str, operation: str, test: str, if_true: str, if_false: str):
        self.monkey_id: int = self.get_monkey_id(monkey_id)
        self.items = deque(self.create_items(items))
        self.operation, self.operation_value = self.create_operation(operation)
        self.test = self.create_test(test)
        self.if_true = self.create_if_true(if_true)
        self.if_false = self.create_if_false(if_false)
        self.counter = 0

    def get_monkey_id(self, monkey_id: str) -> int:
        return int(monkey_id.replace("Monkey ", "").replace(":", ""))

    def create_items(self, items) -> List[int]:
        return [int(x) for x in items.replace("Starting items: ", "").split(", ")]

    def create_operation(self, operation: str):
        return operation.replace("Operation: new = old ", "").split(" ")

    def create_test(self, test: str):
        return int(test.replace("Test: divisible by ", ""))

    def create_if_true(self, if_true: str):
        return int(if_true.replace("If true: throw to monkey ", ""))

    def create_if_false(self, if_false: str):
        return int(if_false.replace("If false: throw to monkey ", ""))

    def get_worry_level_for_item(self, item, devider = None) -> int:
        operation_value = int(self.operation_value) if self.operation_value != "old" else item
        self.counter += 1
        if self.operation == "+":
            if devider:
                return (item + operation_value) % devider
            else:
                return int((item + operation_value) / 3)
        if self.operation == "*":
            if devider:
                return (item * operation_value) % devider
            else:
                return int((item * operation_value) /3 )

    def throw_item(self, devider=None):
        item = self.items.popleft()
        worry_level = self.get_worry_level_for_item(item, devider)
        if worry_level % self.test == 0:
            return self.if_true, worry_level
        else:
            return self.if_false, worry_level

    def add_item(self, item):
        self.items.append(item)


def load_file():
    with open(os.path.join(BASE_DIR, "input.txt")) as file:
        for monkey in file.read().split('\n\n'):
            yield monkey

def create_monkey_dictionary():
    monkey_dict = {}
    for monkey_str in load_file():
        monkey = Monkey(
            monkey_id = monkey_str.split("\n")[0].strip(),
            items = monkey_str.split("\n")[1].strip(),
            operation = monkey_str.split("\n")[2].strip(),
            test = monkey_str.split("\n")[3].strip(),
            if_true = monkey_str.split("\n")[4].strip(),
            if_false = monkey_str.split("\n")[5].strip(),
        )
        monkey_dict[monkey.monkey_id] = monkey


def main():
    monkey_dict = create_monkey_dictionary()

    for i in range(20):
        for _, monkey in monkey_dict.items():
            for _ in range(len(monkey.items)):
                receiver, worry_level = monkey.throw_item()
                monkey_dict[receiver].add_item(worry_level)

    sorted_result = sorted([m.counter for id, m in monkey_dict.items()])
    sorted_result.reverse()
    solution_one = sorted_result[:2]
    print(solution_one[0] * solution_one[1])
    
    
def main_two():
    monkey_dict = create_monkey_dictionary()
    
    lcm_val = lcm(*[m.test for _, m in monkey_dict.items()])

    for i in range(10000):
        for _, monkey in monkey_dict.items():
            for _ in range(len(monkey.items)):
                receiver, worry_level = monkey.throw_item(lcm_val)
                monkey_dict[receiver].add_item(worry_level)

    sorted_result = sorted([m.counter for id, m in monkey_dict.items()])
    sorted_result.reverse()
    solution_one = sorted_result[:2]
    print(solution_one[0] * solution_one[1])


if __name__ == "__main__":
    print("First part:")
    main()
    print("Second part:")
    main_two()
