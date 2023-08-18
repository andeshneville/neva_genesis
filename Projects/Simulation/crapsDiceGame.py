from random import*

def main():
    printIntro()
    no_of_games=getInputs()
    wins=playGame(no_of_games)
    printSummary(wins,no_of_games)
    
def printIntro():
    print("This program simulates the probability of winning Craps")
    print(" games. The user enters the number of games to be simulated")
    print("The program then plays the game keeping track of the number")
    print(" of wins. It then prints the number of wins and the ")
    print("probability of winning the game.\n")
    
def getInputs():
    games=int(input("Enter the Number of games to be simulated: "))
    return games

def playGame(no_of_games):
    count=0
    wins=0
    while count<no_of_games:
        if simOneGame():
            wins=wins+1
        count=count+1
    return wins

def simOneGame():
    diceA=randrange(1,7)
    diceB=randrange(1,7)
    win=0
    while not gameOver(diceA + diceB):
        if diceA+diceB ==7 or diceA + diceB ==11:
            win=win+1
            break
        else:
            diceA=randrange(1,7)
            diceB=randrange(1,7)
    return win==1

def gameOver(a):
    return a==2 or a==3 or a==12

def printSummary(wins,no_of_games):
    print("Number of games played: ",no_of_games)
    prob=wins/no_of_games
    print("Wins: ",wins)
    print("The Probability of winning is: {0:0.1%}".format(prob))
    print("You are good to Try playing It....The End")


if __name__=='__main__':
    main()







