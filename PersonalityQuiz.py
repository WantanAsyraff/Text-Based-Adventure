import Stats
import time

PartnerStats = {}


Answer = ""
A1 = 0
A2 = 0
A3 = 0
A4 = 0

def AnswerUpdate():
    global A1
    global A2
    global A3
    global A4
    
    Answer = input(">>> ")
    if Answer == "a":
        A1 += 2
        breakpoint
    elif Answer == "b":
        A2 += 2
        breakpoint
    elif Answer == "c":
        A3 += 2
        breakpoint
    elif Answer == "d":
        A4 += 2
        breakpoint
    else:
        print('Please type a valid answer, "a, b, c, d"')

# Buffer timer
def loading():
    print("Loading...")
    time.sleep(1)
    

print("Before we begin, you are required to answer these personality questions, this will affect your gameplay." 
      "\nThere is no right answer.")
loading()

# Q1
while True:
    print("\nQuestion 1: You see a friend getting bullied, what do you do?")
    print("a) You try and rescue them by quickly running away from the bully.")
    print("b) You stand up for your friend and protect them from any abuse.")
    print("c) You report the bully to the teacher.")
    print("d) You fight back and beat up the bully.")

    AnswerUpdate()
    break
loading()

# Q2
while True:
    print("\nQuestion 2: There is a yearly mall sale going on in town, you…")
    print("a) Without no hesitation, dash towards the mall.")
    print("b) Take your time and wait for a better sale.")
    print("c) Check your budget and see if it is worth shopping.")
    print("d) Buy anything that is already 90%' off.")
    
    AnswerUpdate()
    break
loading()

# Q3
while True:
    print("\nQuestion 3: You are given a chance to either master an instrument or learn a new weapon, you…")
    print("a) Try to go for the once that seems the quickest to master.")
    print("b) Choose the one that will be more worth mastering.")
    print("c) Go for the one that will benefit you more in the long run.")
    print("d) Obviously weapons, you never know what will happen.")
    
    AnswerUpdate()
    break
loading()

# Q4
while True:
    print("\nQuestion 4: You heard news hearing that its your friend's birthday, what would you do first?")
    print("a) Text your friend, wishing your friend a happy birthday.")
    print("b) Plan a secret surprise party for your friend.")
    print("c) Buy a present that you know your friend will dearly cherish.")
    print("d) Bring in your friends and celebrate the birthday together.")
    
    AnswerUpdate()
    break
loading()

# Q5
while True:
    print("\nQuestion 5: The national Anthem of your country plays, you…")
    print("a) Stand up quickly and sing along.")
    print("b) Slowly stand up and let others sing.")
    print("c) Stand up firmly and enjoy the patriotism.")
    print("d) Sing loudly and proudly of your national Anthem.")
    
    AnswerUpdate()
    break
loading()

# Q6
while True:
    print("\nQuestion 6: Your lecturer has given you a new assignment, you…")
    print("a) Get back home and immediately finish your assignment.")
    print("b) Keep it in the back of your mind and do it later.")
    print("c) Figure out when to exactly to do it in your schedule and then complete it.")
    print("d) Do it the night before the due date.")
    
    AnswerUpdate()
    break
loading()

# Q7
while True:
    print("\nQuestion 7: You were given a hard question. What do you do?")
    print("a) Look up answers online, the faster the better.")
    print("b) Search for your classmates and work out the question together.")
    print("c) Ask other lecturers and seniors to figure out the question.")
    print("d) Copy your friend’s answer.")
    
    AnswerUpdate()
    break
loading()

# Q8
while True:
    print("\nQuestion 8: Your parents went on a vacation without you. You’re alone at home, what do you do?")
    print("a) Immediately hang out with my friends. Maybe even do a sleepover.")
    print("b) Use this opportunity to enjoy and relax throughout the week.")
    print("c) Study and finish any assignments or chores and then relax.")
    print("d) Have a party at your home.")
    
    AnswerUpdate()
    break
loading()

# Q9
while True:
    print("What is your favourite music?")
    print("a) Upbeat songs/ Pop songs")
    print("b) Slow paced/ Sad/ Jazz songs")
    print("c) Classical music")
    print("d) Rock n Roll songs")
    
    AnswerUpdate()
    break
loading()

# Q10
while True:
    print("Final Question: Are you a male or female?")
    print("a) Male")
    print("b) Female")
    
    Answer = input(">>> ")
    if Answer == "a":
        A3 += 2
        A4 += 2
        break
    elif Answer == "b":
        A1 += 2
        A2 += 2
        break
    else:
        print('Please type a valid answer, "a, b, c, d" (CASE SENSITIVE)')
        
print(".........")
#Used for checking total stats
print("A1: ", A1)
print("A2: ", A2)
print("A3: ", A3)
print("A4: ", A4)

TotalAnswer = (A1 + A2 + A3 + A4)
print("Total: ", TotalAnswer)
print("Calculating...")
time.sleep(1)

# Partner evaluation
if A1 and (A1 + A2) >= TotalAnswer/2:
    print("Your partner is a cat")
    PartnerStats.update(Stats.CAT)

elif A2 and (A2 + A4) >= TotalAnswer/2:
    print("Your partner is a dog")
    PartnerStats.update(Stats.DOG)
    
elif A3 and (A1 + A3) >= TotalAnswer/2:
    print("Your partner is a fox")
    PartnerStats.update(Stats.FOX)
    
elif A4 and (A2 + A4) >= TotalAnswer/2:
    print("Your partner is a wolf")
    PartnerStats.update(Stats.WOLF)
    

    
print("Partner's Stats: ", PartnerStats)
PartnerStats["SPEED"] += A1
PartnerStats["HP"] += A2
PartnerStats["ACTIONS"] += ((A3/4) / 10)
PartnerStats["ACTIONS"] = round(PartnerStats["ACTIONS"], 2)
PartnerStats["ATTACK"] += A4
print("New Partner's Stats: ", PartnerStats)