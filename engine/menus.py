import battle as bt

class Menus:
    def __init__(self, title, player_options):
        self.title = title
        self.player_options = player_options
    
    def display_menu(self):
        print(f"{self.title}\n")
        for idx, option in enumerate(self.player_options, 1):
            print(f"[{idx}] {option}")
        
        while True:
            try:
                player_choice = int(input("Enter choice: "))
                if 1 <= player_choice <= len(self.player_options):
                    print(f">> You selected: ✨ {self.player_options[player_choice - 1]}")
                    return self.player_options[player_choice - 1]
                else:
                    print(f"❌ Choose action [1-{len(player_options)}]")
            except ValueError:
                print(f"❌ Choose a valid action [1-{len(player_options)}]")
    
player_options = ["Spellcast", "Use an Item", "Check environment", "Converse with Opponent"]
test = Menus("What are you going to do?", player_options)
test.display_menu()

spells = ["Sidestep", "Scythe Strike", "Zweihander guard"]
test = Menus("What spell are you going to cast?", spells)
test.display_menu()