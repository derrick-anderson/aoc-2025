#! usr/bin/python3
import os
from typing import List

base_path = os.path.dirname(__file__)
print(f"Base Path : {base_path}")


class Safe:
    def __init__(self) -> None:
        self._dial = 0

    def set_dial(self, new_dial: int) -> None:
        self._dial = new_dial

    def get_dial(self) -> int:
        return self._dial

    def rotate_dial(self, direction: str) -> None:
        if direction.upper() == "R":
            self._rotate_right()
        elif direction.upper() == "L":
            self._rotate_left()
        else:
            print(f"Unsupported Roatation Direction :`{direction}`")

    def _rotate_left(self) -> None:
        print("Rotating Left")
        print(f"Dial Was : {self.get_dial()}")
        self._dial -= 1
        if self._dial < 0:
            self._dial = self._dial + 100
        print(f"Dial is :{self.get_dial()}")

    def _rotate_right(self) -> None:
        print("Rotating Right")
        print(f"Dial Was : {self.get_dial()}")
        self._dial += 1
        if self.get_dial() > 99:
            self._dial = self._dial - 100
        print(f"Dial is :{self.get_dial()}")


def get_instructions() -> List[str]:
    instructions = list()
    with open(os.path.join(base_path, "input.txt"), "r") as input:
        instructions = input.readlines()

    print(f"Returning {len(instructions)} instructions.")
    return instructions


if __name__ == "__main__":
    safe = Safe()
    safe.set_dial(50)
    print(f"The Dial starts at {safe.get_dial()}")
    password_count = 0

    for instruction in get_instructions():
        if len(instruction.strip()) == 0:
            continue

        stripped_instruction = instruction.strip()
        direction = stripped_instruction[0:1]
        count = int(stripped_instruction[1:])
        print(f"Rotating Dial `{count}` Clicks to the `{direction}`")
        for click in range(count):
            safe.rotate_dial(direction=direction)
            if safe.get_dial() == 0:
                password_count += 1
        print(
            f"The Dial is rotated {stripped_instruction} to point at {safe.get_dial()}"
        )

    print(f'The password is "{password_count}"')
