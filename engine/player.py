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
        print(f"\n📖 Which spell do you wish to conjure?\nTarget: {enemy}")
        for idx, (spell, desc) in enumerate(self.spellbook.items(), 1):
            print(f" [{idx}] {spell} — {desc[0]} \n     Damage: {desc[1]}\n     Mana Cost: {desc[2]}")

        while True:
            try:
                spellcasted = int(input("Spell Index: "))
                
                if 1 <= spellcasted <= len(self.spellbook):
                    
                    spell_keys = list(self.spellbook.keys())
                    chosen_spell = spell_keys[spellcasted - 1]
                    spell_info = self.spellbook[chosen_spell]
                    
                    print(f">> You're casting: {chosen_spell}")
                    if self.mana < codex_of_the_fools_spellblades[chosen_spell][2]:
                        print("You don't have the energy to cast this it.")
                    else:
                        print(f"You sucessfully casted {chosen_spell}")

            except ValueError:
                print("Invalid input, use integers.")
            except SyntaxError:
                print("Invalid input, use integers.")

    def use_item(self):
        print("\n🎒 Which item do you wish to use?\n")
        for idx, (item, desc) in enumerate(self.inventory.items(), 1):
            print(f" [{idx}] {item} — {desc}")

    def check_environment(self):
        print("\n🌿 You take a moment to observe your surroundings...\n")
        # To be implemented based on environment system

    def converse_with_opponent(self):
        print("\n🗨️ You attempt to speak with your foe...\n")
        # To be implemented with branching dialogue or reaction system


codex_of_the_fools_spellblades = {
    # Spell, desc, DMG, Mana Cost
    "Rend of Regret":["Send scars with multiples cuts from daggers.", 50, 35, ],
    "Moonlit Guillotine":["Strike fear into your opponent with a greatsword.", 60, 40, ],
    "Waltz Of Ignorances": ["Send a flurry of stabs using a rapier.", 30, 15, ]
}    
messenger_bag = {
    "Pocket Watch": "The night is still young.",
    "Tin Can Of Latte": "A student's job is never without it's caffeine.",
    "Bandages": "Putting the boo! in boo boos."
    
}
amal_fakhri = Player("Amal Fakhri", "Researcher of Magis Al-Zalam", "There's no shame in obtaining knowledge.", "Magis AlNur-Walzalam", 200, 50, 75, 300, codex_of_the_fools_spellblades, messenger_bag)
amal_fakhri.spellcast("Opps")