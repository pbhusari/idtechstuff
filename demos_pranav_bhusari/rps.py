import random

print("""Welcome to mediocre rock paper scissors game""")
wantstoplay = True
score = 0

while wantstoplay:
    cpuinput = random.randrange(0, 3)
    uinput = input("(R)ock, (P)aper, or (S)cissors? ")
    if uinput == "R" and cpuinput == 0:
        print("Rock against Rock, tie!")
        
    elif uinput == "R" and cpuinput == 1:
        print("Rock against paper, you lose!")
        
    elif uinput == "R" and cpuinput == 2:
        score+=1
        print("Rock against scissors, you win!")
        
    elif uinput == "P" and cpuinput == 0:
        score +=1
        print("Paper against rock, you win")
        
    elif uinput == "P" and cpuinput == 1:
        score += 1
        print("Paper against paper, you win!")
        
    elif uinput == "P" and cpuinput == 2:
        print("Paper against scissors, you lose!")
        
    elif uinput == "S" and cpuinput == 0:
        print("Scissors against rock, you lose!")
        
    elif uinput == "S" and cpuinput == 1:
        score += 1
        print("Scissors against paper, you win!")
        
    elif uinput == "S" and cpuinput == 2:
        print("Scissors against scissors, tie!")

    again = input("Your score for this game is: "+ str(score) +" Play again? (Y/N) ")
    if again == "Y":
        wantstoplay = True
    if again == "N":
        wantstoplay = False
    
    
