import EventHandler
import random
import time
import Stats

Player = Stats.CAT # PLACEHOLDER, WILL INHERET FROM PERSONALITY QUIZ ONCE COMPLETED

Steps = 0
EventRate = 0.1
EventOccurence = 0.5
Progress = 30

Floors = ["Level 0: Ground Floor", "Level 1: Basement", "Level 2: Hidden Laboratory", "Level 3: Confidential Experimental Department", "Level 4: War Preparations Room"]

def FloorStatus():
    print("-------------------------------------------------------------||")
    time.sleep(1)
    print(f"You are currently on {Floors[0]}")
    print("-------------------------------------------------------------||")
    time.sleep(1)

def Roaming():
    global Steps
    global EventRate

    while Steps < Progress:
        
        print("-------------------------------------------------------------||")
        print(f"Current steps: {Steps} \nType 'walk' to advance")
        print("-------------------------------------------------------------||")
        PChoice = str(input(">>> "))
        
        if PChoice.lower() == "status":
            print(f"Partner's status: {Player}")
        
        elif PChoice.lower() == "walk":
            Steps += 1
            EventRate += random.uniform(0.05, 0.11)
            EventRate = round(EventRate, 2)
            
            print("-------------------------------------------------------------||")
            print("Walking..")
            time.sleep(0.3)
            print("Walking...")
            time.sleep(0.2)
            print(EventRate)
            
            if EventRate > EventOccurence:

                EventHandler.RandomEvent()

                if EventHandler.RandomEvent() == 0:
                    print("Enemy")

                elif EventHandler.RandomEvent() == 1:
                    HP, DEF, ATTACK, SPEED = EventHandler.Loot() # Assign the returned values to variables

                
                EventRate = 0.1
                print(f"resetted the event rate: {EventRate}")
    else:
        print("I don't quite get you...")
        print("-------------------------------------------------------------||")

FloorStatus() 
Roaming()

print("Out of the loop!")
Progress += 30
print(Progress)