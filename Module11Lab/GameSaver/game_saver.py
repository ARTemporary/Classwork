## Module 11 Lab Part 2



## from instructionsa
class GameState:
    def __init__(self, score, level, lives):
        self.score = score
        self.level = level
        self.lives = lives

    def add_to_score(self, amount):
        self.score += amount
        return self

    def next_level(self):
        self.level += 1
        return self

    def add_or_subtract_lives(self, amount):
        if self.lives + amount < 0:
            self.lives = 0
            print("No more lives")
        else:
            self.lives += amount
        return self

    def __str__(self):
        return f"score:{self.score},level:{self.level},lives:{self.lives}"

def save_game(game_state, file_name):
    """saves game state to file - attribute_name,attribute_value three lines"""
    with open(file_name, 'w') as file:
        file.write(f'score,{game_state.score}\nlevel,{game_state.level}\nlives,{game_state.lives}')
    
def load_game(file_name):
    """takes file and makes new gamestate"""
    with open(file_name, 'r') as file:
        saved = {}
        for line in file:
            attribute, value = line.split(',')
            saved[str(attribute.strip())] = int(value.strip())
    loaded_game = GameState(saved['score'], saved['level'], saved['lives'])
    return loaded_game

game = GameState(0,0,5)
# print(game)

game = game.add_or_subtract_lives(-2)
game = game.add_to_score(50)
game = game.add_or_subtract_lives(3)
game = game.next_level()

# print(game)

save_game(game, './Class/Module11Lab/GameSaver/save.txt')

new_game = load_game('./Class/Module11Lab/GameSaver/save.txt')

print(new_game)
