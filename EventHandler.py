import EncounterSelect
import random
import time

EventList = ["EnemyEncounter", "Loot", "Trap"]


def Loot():
    print("-------------------------------------------------------------||")
    time.sleep(1)
    print(f"Partner: I found a some loot under some debris...")
    time.sleep(1)
    print(f"Partner: would you look at that, a rejuvinator.")
    time.sleep(1)
    print(f"Partner: Don't mind if I do...")
    time.sleep(1)
    
    from Battle import Player
    Rejuvinators = random.randrange(0, 3)
    
    if Rejuvinators == 0:
        Player["HP"] += random.randrange(6, 15)
        print("HP increased!")
        
    elif Rejuvinators == 1:
        Player["DEF"] += random.randrange(2, 6)
        print("DEF increased!")
    elif Rejuvinators == 2:
        Player["SPEED"] += 4
        print("SPEED increased!")
    elif Rejuvinators == 3:
        Player["ATTACK"] += random.randrange(4, 10)
        print("ATTACK increased!")

Enemy = EncounterSelect.Enemy

def EnemyEncounter():
    global Enemy
    
    Enemy = EncounterSelect.Enemy
    
    import Battle
    Battle.CombatMode = True

def RandomEvent():
    
    ChooseEvent = 1 #random.randrange(0, 1)
    
    if ChooseEvent == 0:
        print("Enemy Encounter")
        EnemyEncounter()
    
    if ChooseEvent == 1:
        print("Loot")
        Loot()
        
    if ChooseEvent == 2:
        print("Trap")
        
