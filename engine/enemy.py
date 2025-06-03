from units import enemies
import random as rd


class Enemy:
    def __init__(
        self,name, desc, flavour, archetype, 
        hp, defense, atk, mana, spellbook
    ):
        self.name = name
        self.desc = desc
        self.flavour = flavour
        self.archetype = archetype
        
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.mana = mana
        self.spellbook = spellbook
        
    def attack_opponent(self, player):
        print(f">> {self.name} is about to attack")
    
    def use_ability(self):
        return
    
    def use_item():
        return
    
    def flee():
        return
    