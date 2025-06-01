import player
from enemy import Enemy

class Battle:
    def __init__(self, player, enemy, inventory):
        self.player = player
        self.enemy = enemy
        self.inventory = inventory
    
    def player_turn(self):
        options = {
            "Spellcast": lambda: self.player.spellcast(self.enemy),
            "Use an Item": lambda: self.player.useItem(),
            "Check Environment": lambda: self.player.checkEnvironment(),
            "Converse with Opponent": lambda: self.player.converseOpponent(self.enemy)
        }
        
        idx = 1
        for action in options.keys():
            print(f"[{idx}] {action}")
            idx += 1
        
        print(f"--------------------------")
        try:
            action = int(input(">> Your turn, what will you do?\n>> "))
        except ValueError:
            print(f"Invalid input, choose from [1-{idx}].")
        except SyntaxError:
            print(f"Invalid input, choose from [1-{idx}].")
    
    def enemy_turn(self):
        pass
    
    def update_turn(self):
        pass

char_one = player.amal_fakhri
char_two = "Opp"
innit_battle = Battle(char_one,char_two, 0)
innit_battle.player_turn()