#! usr/bin/python3
import os
from typing import List

base_path = os.path.dirname(__file__)

def get_instructions() -> List[str]:
    with open(os.path.join(base_path, "input.txt"), "r") as input:
        return [line.strip().upper() for line in input.readlines() if line]

#TODO: Add a tracker / statistics to the Safe?
#TODO: Allow for multiple clicks

class Safe:
    def __init__(self) -> None:
        self._dial = 0

    def set_dial(self, new_dial: int) -> None:
        self._dial = new_dial

    def get_dial(self) -> int:
        return self._dial

    def rotate_dial(self, direction: str) -> None:
        if direction == "R":
            self._rotate_right()
        elif direction == "L":
            self._rotate_left()
        else:
            pass

    def _rotate_left(self) -> None:
        self._dial -= 1
        if self._dial < 0:
            self._dial = self._dial + 100

    def _rotate_right(self) -> None:
        self._dial += 1
        if self._dial > 99:
            self._dial = self._dial - 100


if __name__ == "__main__":
    safe = Safe()
    safe.set_dial(50)
    password_count = 0

    for instruction in get_instructions():
        direction = instruction[0:1]
        count = int(instruction[1:])

        for click in range(count):
            safe.rotate_dial(direction=direction)
            if safe.get_dial() == 0:
                password_count += 1
        # print(
        #     f"The Dial is rotated {instruction} to point at {safe.get_dial()}"
        # )

    print(f'The password is "{password_count}"')
