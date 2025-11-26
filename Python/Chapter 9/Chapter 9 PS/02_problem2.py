import random

def game():
    print("You are playing this game...")
    score = random.randint(1,62)
    #Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your Score: {score}")
    if(score>hiscore):
        #write to file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        
        
    return score

game()