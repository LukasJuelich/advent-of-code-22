import math

def get_priority_of_letter(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    if letter.isupper():
        return ord(letter) - 38
    else:
        return 0

def find_intersected_letters(string_one: str, string_two: str) -> str:
    intersection = ""
    for letter in string_one:
        if letter in string_two and letter not in intersection:
            intersection += letter
    return intersection

priority_score = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        length_half = math.ceil(len(line)/2)
        first_half = slice(0, length_half)
        second_half = slice(length_half, len(line))
        letters_to_score = find_intersected_letters(line[first_half], line[second_half])
        for letter in letters_to_score:
            priority_score += get_priority_of_letter(letter)

    print(priority_score)
