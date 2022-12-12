from typing import List
import re

def read_input(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def fully_contains(values: List[int]) -> bool:
    if values[2] <= values[0] <= values[1] <= values[3] or \
        values[0] <= values[2] <= values[3] <= values[1]:
        return True
    return False

def overlaps(values: List[int]) -> bool:
    if values[2] <= values[0] <= values[3] or \
        values[2] <= values[1] <= values[3] or \
        values[0] <= values[2] <= values[1] or \
        values[0] <= values[3] <= values[1]:
        return True
    return False

input = read_input('input.txt')

result_contains = 0
result_overlaps = 0
for line in input:
    regex_res = re.findall('\d+', line)
    regex_res = [int(value) for value in regex_res]
    if fully_contains(regex_res):
        result_contains += 1
    if overlaps(regex_res):
        result_overlaps += 1

print(str(result_contains) + '\n' + str(result_overlaps))
