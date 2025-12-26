#! usr/bin/python3
import os
import re

base_path = os.path.dirname(__file__)


def get_input() -> list:
    with open(os.path.join(base_path, "input.txt"), "r") as input:
        return [
            (int(id_range.split("-")[0]), int(id_range.split("-")[1]))
            for id_range in input.read().split(",")
        ]


if __name__ == "__main__":
    id_ranges = get_input()
    invalid_pattern = re.compile(r'^(.+)\1+$', re.MULTILINE)
    invalid_sum = 0
    for start, end in id_ranges:
        for id in range(start, end + 1):
            if invalid_pattern.match(str(id)):
                invalid_sum += id
    print(f"Invalid Sum: `{invalid_sum}`")
