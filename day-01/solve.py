#! usr/bin/python3
import os

from typing import List
base_path = os.path.dirname(__file__)
print(f'Base Path : {base_path}')

def get_instructions() -> List[str]:
    instructions = list()
    with open(os.path.join(base_path, "input.txt"), "r") as input:
        instructions = input.readlines()

    print(f'Returning {len(instructions)} instructions.')
    return instructions

def rotate(direction: str, start: int, count: int) -> int:
    norm_count = count % 100
    end = 0
    if direction.upper() == "L":
        end = start - norm_count
        if end < 0:
            end += 100
    elif direction.upper() == "R":
        end = start + norm_count
        if end > 99:
            end -= 100
    return end

if __name__ == "__main__":
    dial = 50
    print(f'The Dial starts at {dial}')
    password = 0
    for instruction in get_instructions():
        if len(instruction.strip()) < 2:
            print(f'Bad Instruction: `{instruction.strip()}`')
            continue
        stripped_instruction = instruction.strip()
        direction = stripped_instruction[0:1]
        count = int(stripped_instruction[1:])
        dial = rotate(direction=direction, start=dial, count=count)
        print(f'The Dial is rotated {stripped_instruction} to point at {dial}')
        if dial == 0:
            password += 1
    print(f'The password is "{password}"')