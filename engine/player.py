import json

class Player:
    def __init__(
        self, name, desc, flavour, archetype,
        hp, defense, attack, mana,
        spellbook, inventory
    ):
        self.name = name
        self.desc = desc
        self.flavour = flavour
        self.archetype = archetype

        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.mana = mana

        self.spellbook = spellbook  # Dictionary of spells
        self.inventory = inventory  # Dictionary of items

    def spellcast(self, enemy):
        # Get from spellbooks.json and then parse
        try:
            with open("units/spellbooks.json", "r") as f:
                codex = json.load(f)
        except Exception as e:
            print("\nInvalid input, error: ", e)
            
        spells = codex.get(self.spellbook)
        spell_list = list(spells.keys())
            
        if not spells:
            print("No spells found")
        else:
            print(f"\n📖 Which spell do you wish to conjure?\nTarget: {enemy}")
            for idx, (spell, desc) in enumerate(spells.items(), 1):
                print(f""" [{idx}] {spell} — {desc["description"]}
                      \n   Damage: {desc["damage"]} | Mana Cost: {desc["mana cost"]}""")

        while True:
            try:
                spellcasted = int(input("Spell Index: "))
                
                if 1 <= spellcasted <= len(spell_list):
                    chosen_spell = spell_list[spellcasted - 1]
                    spell_data = spells[chosen_spell]
                    
                    print(f">> You're casting: {chosen_spell}")
                    if self.mana < spell_data["mana cost"]:
                        print(">> You don't have the energy to cast this it.")
                    else:
                        self.mana -= spell_data["mana cost"]
                        #attack enemy line
                        print(f">> You sucessfully casted {chosen_spell}")
                        total_damage = self.attack + spell_data["damage"]
                        print(f"Total damage: {total_damage}")
                        return total_damage
                    
            except ValueError:
                print(f"Invalid input, choose from [1-{idx}].")
            except SyntaxError:
                print(f"Invalid input, choose from [1-{idx}].")

    def use_item(self):
        print("\n🎒 Which item do you wish to use?\n")
        for idx, (item, desc) in enumerate(self.inventory.items(), 1):
            print(f" [{idx}] {item} — {desc}")
            
        while True:
            try:
                choose_item = int(input("Item Index: "))
                
                if 1 <= choose_item <= len(self.inventory):
                    item_keys = list(self.inventory.keys())
                    chosen_item = item_keys[choose_item - 1]
                    item_info = self.inventory[chosen_item]
            except ValueError:
                print(f"Invalid input, choose from [1-{idx}].")
            except SyntaxError:
                print(f"Invalid input, choose from [1-{idx}].")

    def check_environment(self):
        print("\n🌿 You take a moment to observe your surroundings...\n")
        # To be implemented based on environment system

    def converse_with_opponent(self):
        print("\n🗨️ You attempt to speak with your foe...\n")
        # To be implemented with branching dialogue or reaction system

   
messenger_bag = {
    # Item, desc-0, quantity-1, healing-2, damage(enemy)-3, damage(player)-4, HP(player)-5, HP(enemy)-6,
    "Pocket Watch": "The night is still young.",
    "Tin Can Of Latte": "A student's job is never without it's caffeine.",
    "Bandages": "Putting the boo! in boo boos."
    
}
amal_fakhri = Player("Amal Fakhri", "Researcher of Magis Al-Zalam", "There's no shame in obtaining knowledge.", "Magis AlNur-Walzalam", 200, 50, 75, 300, "codex_of_the_fools_spellblades_edition", messenger_bag)
#amal_fakhri.spellcast("opp")