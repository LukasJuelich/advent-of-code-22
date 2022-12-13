from typing import List

def read_input(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file]

def init_stacks() -> List[List[str]]:
    stacks: List[List[str]] = []
    for stack_height in range(0,8):
        stacks.append([str])
    return stacks

def build_stacks(stacks: List[List[str]], input: List[str]) -> None:
    for row in range(0, 8):
        for column in range(1, 36, 4):
            stacks[row].append(input[row][column])

def 


input = read_input('input.txt')

stacks = init_stacks()
build_stacks(stacks, input)

print(stacks)


