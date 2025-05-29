class Battle:
    def __init__(self, player, enemy, inventory):
        self.player = player
        self.enemy = enemy
        self.inventory = inventory
    
    def player_turn(self):
        options = {
            "Spellcast": lambda: self.player.spellcast(self.enemy)
            "Use an Item": lambda: self.player.useItem()
            "Check Environment": lambda: self.player.checkEnvironment()
            "Converse with Opponent": lambda:  self.player.converseOpponent(self.enemy)
        }
    
    def attack(self):
        pass
    
    def update_turn(self):
        pass