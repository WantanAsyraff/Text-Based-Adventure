import EncounterSelect
import random
import time


EventList = ["EnemyEncounter", "Loot", "Trap"]


def Loot():

    print("-------------------------------------------------------------||")
    time.sleep(1)
    print("Partner: I found some loot under some debris...")
    time.sleep(1)
    print("Partner: Would you look at that, a rejuvenator.")
    time.sleep(1)
    print("Partner: Don't mind if I do...")
    time.sleep(1)

    Rejuvinators = random.randrange(0, 3)  # Change the range to include 3 as well
    from RoamMode import Player

    if Rejuvinators == 0:
        Player['HP'] += random.randint(6, 16)
        print("HP increased!")
    elif Rejuvinators == 1:
        Player['DEF'] += random.randint(6, 16)
        print("DEF increased!")
    elif Rejuvinators == 2:
        Player['ATTACK'] += 4
        print("ATTACK increased!")
    elif Rejuvinators == 3:
        Player['SPEED'] += random.randint(6, 16)
        print("SPEED increased!")
    
    time.sleep(1)


Enemy = EncounterSelect.Enemy

def EnemyEncounter():
    global Enemy
    
    Enemy = EncounterSelect.Enemy
    
    import Battle
    Battle.CombatMode = True

def RandomEvent():
    
    ChooseEvent = random.randrange(0, 1)
    
    if ChooseEvent == 0:
        print("Enemy Encounter")
        EnemyEncounter()
    
    if ChooseEvent == 1:
        print("Loot")
        Loot()
        
    if ChooseEvent == 2:
        print("Trap")