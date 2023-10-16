import random
import time
#import PersonalityQuiz
import Stats
import EventHandler
# NOTICE: I KNOW THAT THIS CODE COULD BE USED BETTER IF I ALSO USED LIST ESPECIALLY FOR THE COMMANDS & ACTIONS. BUT,
# I'M WORKING WITH WHAT WORKS FOR NOW LOL!
# ENEMY WILL ENHERIT FROM STATS

Player = Stats.CAT # PLACEHOLDER, WILL INHERET FROM PERSONALITY QUIZ ONCE COMPLETED

PartnerName = "Partner" # ASK THIS QUESTION IN THE STORY FILE LATER
PlayerName = "You"

Enemy = EventHandler.Enemy


Damage = (Player["ATTACK"] + (Player["ATTACK"] * Player["WEAPONS MASTERY"]))
Damage = round(Damage)
Crit = Damage * 4

PlayerRoll = 0
PChoice = ""
EnemyInfo = 0
EnemyUpdate = {}

CombatMode = True 



def EnemyTurn():
    if Player["HP"] <= 0:
        PlayerDeath()
        breakpoint
    else:
        print(f"{Enemy['NAME']} turn to attack")
        TotalAttack = Player["HP"]
        
        TotalAttack = (Player["HP"] - (Enemy["ATTACK"] - Player["DEF"]))
        Player["HP"] - TotalAttack
        time.sleep(1)
        print(f"{PartnerName} got hurt! Damage: {TotalAttack}")
        
        if Player["HP"] <= 0:
            PlayerDeath()
            breakpoint
        


def PlayerTurn():
    if Enemy["HP"] < 1:
        EnemyDeath()
        breakpoint
    else:
        print(f"{PartnerName} turn to attack")
        TotalAttack = Enemy["HP"]
        
        TotalAttack = (Enemy["HP"] - (Damage - Enemy["DEF"])) 
        Enemy["HP"] -= TotalAttack
        time.sleep(1)
        print(f"{Enemy['NAME']} got hurt! Damage: {TotalAttack}")
        
        if Enemy["HP"] <= 0:
            PlayerDeath()
            breakpoint


def EnemyDeath():
    global CombatMode

    print(f"{Enemy['NAME']} enemy decommissioned.")
    CombatMode = False
    breakpoint

def PlayerDeath():
    global CombatMode 
    
    print(f"{PartnerName} lost contact")
    CombatMode = False
    breakpoint

def CombatAttack():
    global CombatMode
    global Player

    if Player["HP"] > 0:
        PlayerTurn()
    
    elif Player["HP"] < 1 : #Incorporate SPEED CHECK HERE
        PlayerDeath()
        CombatMode = False
        breakpoint
        

    if Enemy["HP"] > 0:
        EnemyTurn()
        
    elif Enemy["HP"] < 1:
        EnemyDeath()
        CombatMode = False
        breakpoint

    CombatChoice()
        



def CombatChoice():
        time.sleep(1)
        print("-------------------------------------------------------------||")
        print(f"{PartnerName}: {Enemy['NAME']} here! What should we do?")
        time.sleep(0.5)
        print("Commands -> |Status| Attack| Inventory| Actions| ")
        print("-------------------------------------------------------------||")


def CombatStatus():
    global EnemyInfo
    global EnemyUpdate
    
    if EnemyInfo <= 0:
        print("-------------------------------------------------------------||")
        print(f"{PartnerName} status: \n{Player}")
        print("-------------------------------------------------------------||")
        time.sleep(0.8)
        print("Unknown...")
        time.sleep(0.8)
        print(f"{PartnerName}: You need to scan it...")
        print("-------------------------------------------------------------||")
        CombatChoice()
    
    if EnemyInfo > 0:
        EnemyUpdate = Enemy
        print("-------------------------------------------------------------||")
        print(f"{PartnerName} status: \n{Player}")
        print("-------------------------------------------------------------||")
        time.sleep(0.8)
        print(f"The {Enemy['NAME']}'s status: \n{EnemyUpdate}")
        print("-------------------------------------------------------------||")
        CombatChoice()


def Scan():
    global EnemyInfo
    
    if EnemyInfo >= 1:
        print("Their data is already scanned...")
        print("-------------------------------------------------------------||")
        breakpoint

    if EnemyInfo == 0:
        print("Scanning.")
        time.sleep(0.7)
        print("Scanning..")
        time.sleep(0.7)
        print("Scanning...")
        time.sleep(0.7)
        print("Scanning complete!")
        print("-------------------------------------------------------------||")
        print(f'{PlayerName}: I added their data into the "status" command.')
        print("-------------------------------------------------------------||")
        EnemyInfo += 1
        time.sleep(0.8)
        print("-------------------------------------------------------------||")
        print(f"{Enemy['NAME']} used this opportunity to attack!")
        time.sleep(0.8)
        EnemyTurn()
        
        
        print("-------------------------------------------------------------||")
        breakpoint
    CombatChoice()

def Weakness_Search():
    global PlayerRoll
    global CombatMode
    
    print(f"{PartnerName}: Alright, searching for weaknesses...")
    time.sleep(0.8)
    
    
    PlayerRoll = float((random.uniform(0.1, 1)) - 0.10) / 2  
    PlayerRoll = round(PlayerRoll, 2) + Player["ACTIONS"]
    print("DEBUG: ROLL ->", PlayerRoll)
    
    if PlayerRoll > 0.55:
        
        print(f"{Player}: I see a weakness in the enemy's body!")
        time.sleep(0.8)
        print(f"{PartnerName}: Should I strike it down?")
        
        CombatActions()
        return PlayerRoll
    else:
        print(f"{Player}: I can't find anything...")
        time.sleep(0.8)
        print("You: Watch out!")
        print("-------------------------------------------------------------||")
        EnemyTurn()
        
        if Player["HP"] <= 0:
            time.sleep(0.8)
            print(f"{PartnerName} died.")
            CombatMode = False
            breakpoint
        else:
            CombatChoice()
            breakpoint


def Weakness_Strike():
    global CombatMode
    
    
    PlayerRoll = float((random.uniform(0.1, 1)) - 0.10) / 2  
    PlayerRoll = round(PlayerRoll, 2) + Player["ACTIONS"]
    print("DEBUG: ROLL ->", PlayerRoll)
    
    print("-------------------------------------------------------------||")
    print(f"{Player}: Going all in!")
    time.sleep(0.8)
    if PlayerRoll > 0.75:
        Enemy["HP"] -= Crit
        print(f"{PartnerName}: Critical hit! That did {Damage} Damage.")
    
    time.sleep(0.8)
    
    if Enemy["HP"] <= 0:
        EnemyDeath()
        
    else:
        
        print(f"{PartnerName}: I missed!")
        EnemyTurn()
        
        if Player["HP"] <= 0:
            print(f"{[PartnerName]} died.")
            CombatMode = False
            breakpoint
        else:
            CombatChoice() 
            breakpoint


def Retreat():
    global CombatMode
    
    PlayerRoll = float((random.uniform(0.1, 1)) - 0.10) / 2  
    PlayerRoll = round(PlayerRoll, 2) + Player["ACTIONS"]
    print("DEBUG: ROLL ->", PlayerRoll)
    
    print("-------------------------------------------------------------||")
    print(f"{PlayerName} Fall back! This battle's not worth it.")
    time.sleep(0.8)
    print("DEBUG -> ", PlayerRoll)
    if PlayerRoll > 0.3:
        print(f"{PartnerName} Leaving combat...")
        print("-------------------------------------------------------------||")
        time.sleep(0.8)
        CombatMode = False
        breakpoint
    else:
        print(f"{PartnerName} Dang it, the enemy blocked me!")
        EnemyTurn()

    PlayerTurn()


def Hit_and_Run():
    
    PlayerRoll = float((random.uniform(0.1, 1)) - 0.10) / 2  
    PlayerRoll = round(PlayerRoll, 2) + Player["ACTIONS"]
    print("DEBUG: ROLL ->", PlayerRoll)
    
    print("-------------------------------------------------------------||")
    print(f"{PlayerName} Act swiftly, I'm activating a L-EMP.")
    time.sleep(0.8)
    print(f"{PartnerName} Alright!")
    if PlayerRoll > 0.6:
        PlayerTurn()
        print("-------------------------------------------------------------||")
        time.sleep(0.8)
        print(f"{PartnerName} Not a scratch.")
        CombatChoice()
        breakpoint
    else:
        print(f"{PartnerName} I missed!")
        print("-------------------------------------------------------------||")
        EnemyTurn()
        print("-------------------------------------------------------------||")
        CombatChoice()
        breakpoint
        
    

# ACTIONS WILL BE PERCENT BASED
def CombatActions():
    
    
    print("Actions -> | Retreat| Scan| Hit and Run| Weakness search| Weakness strike|")
    print("-------------------------------------------------------------||")
    
    PChoice = input(">>> ")
    
    if PChoice.lower() =="retreat":
        Retreat() 
        breakpoint
        
    elif PChoice.lower() == "scan":
        Scan()
        breakpoint
        
    elif PChoice.lower() == "hit and run":
        Hit_and_Run()
        breakpoint
        
    elif PChoice.lower() == "weakness search":
        Weakness_Search()
        breakpoint
        
    elif PChoice.lower() == "weakness strike":
        
        if PlayerRoll > 0.55:
            Weakness_Strike()
            breakpoint
        else:
            print("Partner: Let's not rush things... We gotta know what we're dealing with.")
        breakpoint
    else:
        print("Partner: Huh... I don't get you...")
        CombatChoice()


def Combat(): # ROOT COMBAT FUNCTION
    global CombatMode
    
    while CombatMode:

        PChoice = input(">>> ")
        
        if PChoice.lower() == "attack":
            
            if Enemy["HP"] > 0:
                CombatAttack()
            elif Enemy["HP"] < 1:
                break
            
        elif PChoice.lower() == "status":
            CombatStatus()
        
        elif PChoice.lower() == "inventory":
            print("FUNCTION COMING SOON!")
        
        elif PChoice.lower() == "actions":
            CombatActions()
        
        else:
            print(f"{PartnerName}: I don't understand... Give me a proper order.")
            CombatChoice()
# Call the Combat function to start the combat

if CombatMode == True:
    print(Enemy['NAME'], "Emerges.")
    if Player["HP"] > 0 or Enemy > 0:
        CombatChoice()
        Combat()