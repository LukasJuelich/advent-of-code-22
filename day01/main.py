most_calories = [0, 0, 0]
current_calories = 0

def calcTotalOfArray(array):
    sum = 0
    for element in array:
        sum += element
    
    return sum

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
    print(calcTotalOfArray(most_calories))
