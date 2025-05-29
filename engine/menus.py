class Menus:
    def __init__(self, title, player_options):
        self.title = title
        self.player_options = player_options
    
    def display_menu(self):
        print(f"{self.title}")
        for idx, option in enumerate(self.player_options, 1):
            print(f"[{idx}] {option}")
        
        while True:
            try:
                player_choice = int(input("Enter choice: "))
                if 1 <= player_choice <= len(player_options):
                    print(f">> You selected: {player_options[player_choice - 1]}")
                    return player_options[player_choice - 1]
                else:
                    print(f"Choose action [1-{len(player_options)}]")
            except ValueError:
                print(f"Choose a valid action [1-{len(player_options)}]")
    
player_options = ["Start", "New game", "Reset", "Action"]
test = Menus("Test menu", player_options)
test.display_menu()