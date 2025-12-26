#! usr/bin/python3
import os

base_path = os.path.dirname(__file__)


def get_input() -> list:
    with open(os.path.join(base_path, "input.txt"), "r") as input:
        return input.readlines()


if __name__ == "__main__":
    pass
