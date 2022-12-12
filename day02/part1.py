game_won = { "A Y", "B Z", "C X" }
game_draw = { "A X", "B Y", "C Z"}
game_lost = { "A Z", "B X", "C Y"}

def check_game_outcome_score(game: str) -> int:
    if game in game_won:
        return 6
    if game in game_draw:
        return 3
    if game in game_lost:
        return 0
        
    return 0

def get_score_selected_shape(game: str) -> int:
    if "X" in game:
        return 1
    if "Y" in game:
        return 2
    if "Z" in game:
        return 3

    return 0

score = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        score += check_game_outcome_score(line)
        score += get_score_selected_shape(line)

print(score)