most_calories = 0
current_calories = 0

with open("input.txt", "r") as file:
    for line in file:
        if line != "\n":
            current_calories += int(line)
        else:
            if current_calories > most_calories:
                most_calories = current_calories

            current_calories = 0

print(most_calories)
