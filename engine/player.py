class Player:
    def __init__(self,name, desc, flavour, archetype, HP, DEF, ATK, MANA, spellbook, inventory):
        self.name = name
        self.desc = desc
        self.flavour = flavour
        self.archetype = archetype
        self.HP = HP
        self.DEF = DEF
        self.ATK = ATK
        self.MANA = MANA
        self.spellbook = spellbook
        self.inventory = inventory
        
    def spellcast(self):
        print("Which spells do you wish to conjure?")
        for idx, (spell, desc) in enumerate(self.spellbook.items(), 1):
            print(f"[{idx}] {spell} — {desc}")
    
    def useItem(self):
        print("Which items do you wish to use?")
        for idx, (item, desc) in enumerate(self.inventory.items(), 1):
            print(f"[{idx}] {item} — {desc}")

codex_of_the_fools_spellblades = {
    "Rend of Regret":"Send scars with multiples cuts from daggers.",
    "Moonlit Guillotine":"Strike fear into your opponent with a greatsword.",
    "Waltz Of Ignorances": "Send a flurry of stabs using a rapier."
}    
messenger_bag = {
    "Pocket Watch": "The night is still young.",
    "Tin Can Of Latte": "A student's job is never without it's caffeine.",
    "Bandages": "Putting the boo! in boo boos."
    
}
amal_fakhri = Player("Amal Fakhri", "Researcher of Magis Al-Zalam", "There's no shame in obtaining knowledge.", "Magis AlNur-Walzalam", 200, 50, 75, 300, codex_of_the_fools_spellblades, messenger_bag)
amal_fakhri.spellcast()
amal_fakhri.useItem()