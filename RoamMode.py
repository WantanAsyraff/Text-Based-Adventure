import EventHandler
import random
import time

Steps = 0
EventRate = 0.1
EventOccurence = 0.4

Floors = ["Level 0: Ground Floor", "Level 1: Basement", "Level 2: Hidden Laboratory", "Level 3: Confidential Experimental Department",
          "Level 4: Control Room", "Level 5: War Preparations Room"]

print(f"You are currently on {Floors[0]}")
print("-------------------------------------------------------------||")

while Steps <= 30:
    
    print("-------------------------------------------------------------||")
    print(f"Current steps: {Steps} \nType 'walk' to advance")
    print("-------------------------------------------------------------||")
    PChoice = str(input(">>> "))
    
    if PChoice.lower() == "walk":
        Steps += 1
        EventRate += random.uniform(0.05, 0.10)
        EventRate = round(EventRate, 2)
        
        print("-------------------------------------------------------------||")
        print("Walking..")
        time.sleep(0.3)
        print("Walking...")
        time.sleep(0.2)
        print(EventRate)
        
        if EventRate > EventOccurence:
            EventHandler.RandomEvent()
            EventRate = 0.1
            print(f"resetted the event rate: {EventRate}")
    else:
        print("I don't quite get you...")
        print("-------------------------------------------------------------||")
        
print("Out of the loop!")