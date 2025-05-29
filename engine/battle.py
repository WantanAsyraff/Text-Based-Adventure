from player import Player

class Battle:
    def __init__(self, player, enemy, inventory):
        self.player = player
        self.enemy = enemy
        self.inventory = inventory
    
    def player_turn(self):
        options = {
            "Spellcast": lambda: Player.spellcast(self.enemy),
            "Use an Item": lambda: Player.useItem(),
            "Check Environment": lambda: Player.checkEnvironment(),
            "Converse with Opponent": lambda: Player.converseOpponent(self.enemy)
        }
    
    def attack(self):
        pass
    
    def update_turn(self):
        pass