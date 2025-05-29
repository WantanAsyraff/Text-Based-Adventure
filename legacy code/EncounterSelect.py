import random
import Stats


EnemyList = ["security_droid", "worker_droid", "drone"]

Encounter = random.randrange(0, len(EnemyList))
Encounter = int(Encounter)
    
if Encounter == 0:
        
    Enemy = Stats.SECURITY_DROID

if Encounter == 1:
        
    Enemy = Stats.WORKER_DROID

if Encounter == 2:
        
    Enemy = Stats.DRONE

