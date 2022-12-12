game_won = { "A Y", "B Z", "C X" }
game_draw = { "A X", "B Y", "C Z"}
game_lost = { "A Z", "B X", "C Y"}


def translate_game(game: str, set: set) -> str:
    for element in set:
        if game[0] in element:
            return element
    
    return ""

def get_needed_game_outcome(game: str) -> str:
    if "X" in game:
        return translate_game(game, game_lost)
    if "Y" in game:
        return translate_game(game, game_draw)
    if "Z" in game:
        return translate_game(game, game_won)
    
    return ""
        
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
        game = get_needed_game_outcome(line)
        score += check_game_outcome_score(game)
        score += get_score_selected_shape(game)

print(score)