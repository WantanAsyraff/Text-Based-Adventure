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
        
        action_key = list(options.keys())
        
        print("Your options:")
        for idx, action in enumerate(options.keys(), 1):
            print(f"[{idx}] {action}")
        
        print(f"--------------------------")
        try:
            choice = int(input(">> Your turn, what will you do?\n>> "))
            
            if 1 <= choice <= len(action_key):
                chosen_action = action_key[choice-1]
                print(f"\n>> You chose: {chosen_action}")
                options[chosen_action]()
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