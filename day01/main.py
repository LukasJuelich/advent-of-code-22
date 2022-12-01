most_calories = [0, 0, 0]
current_calories = 0

def calc_total_of_array(array):
    total = 0
    for element in array:
        total += element
    
    return total

with open("input.txt", "r") as file:
    for line in file:
        if line != "\n":
            current_calories += int(line)
        else:
            for index, calories in enumerate(most_calories):
                if current_calories > calories:
                    most_calories[index] = current_calories
                    break
            
            most_calories.sort()
            current_calories = 0

    print(most_calories)
    print(calc_total_of_array(most_calories))
