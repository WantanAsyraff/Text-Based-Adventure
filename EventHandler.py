import EncounterSelect
import random
import time

EventList = ["EnemyEncounter", "Loot", "Trap"]
Enemy = EncounterSelect.Enemy
CombatMode = False

def Loot():

    print("-------------------------------------------------------------||")
    time.sleep(1)
    print("Partner: I found some loot under some debris...")
    time.sleep(1)
    print("Partner: Would you look at that, a rejuvenator.")
    time.sleep(1)
    print("Partner: Don't mind if I do...")
    time.sleep(1)

    Rejuvinators = random.randint(0, 3)  # Change the range to include 3 as well
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
    breakpoint


def EnemyEncounter():

    global CombatMode
    CombatMode = True

def RandomEvent():
    
    ChooseEvent = random.choice(EventList)
    
    if ChooseEvent == "Enemy Encounter":
        print("Enemy Encounter")
        EnemyEncounter()
    
    elif ChooseEvent == "Loot":
        print("Loot")
        Loot()
        
    elif ChooseEvent == "Trap":
        print("Trap")

RandomEvent()