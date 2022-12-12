import math
from typing import List

def get_priority_of_letter(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    if letter.isupper():
        return ord(letter) - 38
    else:
        return 0

def find_intersected_letters(string_one: str, string_two: str) -> str:
    intersection = ''
    for letter in string_one:
        if letter in string_two and letter not in intersection:
            intersection += letter
    return intersection

def read_input(filename: str) -> List[str]:
    input = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            input.append(line.strip())
    return input

input = read_input('input.txt')
i = 0
priority_score = 0
while i < len(input):
    intersection1 = find_intersected_letters(input[i], input[i+1])
    intersection2 = find_intersected_letters(intersection1, input[i+2])
    priority_score += get_priority_of_letter(intersection2)
    i += 3

print(priority_score)
