import EncounterSelect
import random
import time

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

    if Rejuvinators == 0:
        HP = random.randint(6, 16)
        print("HP increased!")
    elif Rejuvinators == 1:
        DEF = random.randint(6, 16)
        print("DEF increased!")
    elif Rejuvinators == 2:
        ATTACK = 4
        print("ATTACK increased!")
    elif Rejuvinators == 3:
        SPEED = random.randint(6, 16)
        print("SPEED increased!")
    return HP, DEF, ATTACK, SPEED


def EnemyEncounter():

    global CombatMode
    CombatMode = True


def RandomEvent():
    
    ChooseEvent = random.randint(0, 1)

    if ChooseEvent == 0:
        print("Enemy Encounter")
        EnemyEncounter()
    
    elif ChooseEvent == 1:
        print("Loot")
        Loot()
        
    elif ChooseEvent == "Trap":
        print("Trap")
