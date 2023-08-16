
from random import random
from graphics import*
from buttons import Button

def intro():
    return """"This Program Simulates a game of racquetball between")
        players called "A" and "B". The ability of each play
        indicated by a probability (a number between o and 1)
        the player wins the point when serving. Player A always
        has the first serve."""
def getInputs():
    a=float(input("What is the % prob, Player A wins a serve?: "))
    b=float(input("What is the % prob. player B wins a serve? "))
    n=int(input("How many games to simulate? "))
    
    return (a/100),(b/100),n

class Play:
    def __init__(self,probA,probB,n):

        self.probA=probA
        self.probB=probB
        self.winsA=0
        self.winsB=0
        self.shutoutsA=0
        self.shutoutsB=0
        self.play(n)
    def play(self,n):
        for i in range(n):
            scoreA,scoreB=self.simOneGame(i)
            if scoreA > scoreB:
                self.winsA=self.winsA+1
                if scoreB==0:
                    self.shutoutsA=self.shutoutsA+1
            else:
                self.winsB=self.winsB+1
                if scoreA==0:
                    self.shutoutsB=self.shutoutsB+1
    
    def simOneGame(self,n):
        scoreA=0
        scoreB=0
        if n%2==1:
            serving="A"
        else:
            serving="B"
        while not self.gameOver(scoreA,scoreB):
            if serving=="A":
                if random()<self.probA:
                    scoreA=scoreA+1
                else:
                    serving="B"
            else:
                if random()<self.probB:
                    scoreB=scoreB+1
                else:
                    serving="A"
        return scoreA,scoreB
    
    def gameOver(self,a,b):
        return a==15 or b==15


    def getscores(self):
        return self.winsA,self.winsB
    def getshutouts(self):
        return self.shutoutsA,self.shutoutsB
    def returnSummary(self):
        n=self.winsA+self.winsB
        a="{0:0.2%}".format(self.winsA/n)
        b="{0:0.2%}".format(self.winsB/n)
        c="{0:0.2%}".format(self.shutoutsA/self.winsA)
        d="{0:0.2%}".format(self.shutoutsB/self.winsB)
        return self.winsA,a,self.winsB,b,self.shutoutsA,c,self.shutoutsB,d,n
    def printSummary(self):
        n=self.winsA+self.winsB
        print("\nGames simulated: ",n)
        print("Wins for A: {0} ({1:0.1%})".format(self.winsA,self.winsA/n))
        print("Wins for B: {0} ({1:0.1%})".format(self.winsB,self.winsB/n))
        print("Shutouts for A: {0} ".format(self.shutoutsA))
        print("Shutouts for B: {0} ".format(self.shutoutsB))

class GraphicsRacquetball:
    def __init__(self):
        self.win=win=GraphWin("Racquet Ball",350,400)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground("green")
        #create graphics buttons
        instB=Button(self.win,Point(70,90),30,10,"Instructions")
        quitB=Button(self.win,Point(82,10),15,8,"QUIT")
        retryB=Button(self.win,Point(22,90),30,10,"SIMULATE")
        
        #create texts on the Window
        Text(Point(15,70),"Wins:").draw(self.win)
        Text(Point(40,70),"A").draw(self.win)
        Text(Point (40,60),"B").draw(self.win)
        Text(Point(20,45),"Shutouts").draw(self.win)
        Text(Point(40,45),"A").draw(self.win)
        Text(Point(40,35),"B").draw(self.win)
        Text(Point(19,20),"Games Simulated").draw(self.win)
        Text(Point(81,77),"Percent").draw(self.win)
        #create showStats boxes
        B1=Button(self.win,Point(60,70),15,8,0)
        B2=Button(self.win,Point(85,70),20,8,0)
        B3=Button(self.win,Point(60,60),15,8,0)
        B4=Button(self.win,Point(85,60),20,8,0)
        B5=Button(self.win,Point(60,45),15,8,0)
        B6=Button(self.win,Point(85,45),20,8,0)
        B7=Button(self.win,Point(60,35),15,8,0)
        B8=Button(self.win,Point(85,35),20,8,0)
        B9=Button(self.win,Point(60,20),15,8,0)

        self.stats=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
        self.buttons=[instB,quitB,retryB]

        #Make the first simulation
        self.play()

    def play(self):
        mc=self.win.checkMouse()
        while not self.buttons[1].clicked(mc):   
            a,b,c=self.getInputs()
            gam=Play(a,b,c)
            d,e,f,g,h,i,j,k,l=gam.returnSummary()
            stats=[d,e,f,g,h,i,j,k,l]
            for i in range (len(self.stats)):
                self.stats[i].setLabel(stats[i])
            mc=self.win.getMouse()   
        self.win.close()
    def getInputs(self):
        win=GraphWin("Inputs",300,200)
        win.setCoords(0,0,100,100)

        #Entry for inputs
        Text(Point(20,80),"ProbA Wins").draw(win)
        probA=Entry(Point(70,80),10).draw(win)
        Text(Point(20,60),"ProbB Wins").draw(win)
        probB=Entry(Point(70,60),10).draw(win)
        Text(Point(20,40),"No of Games").draw(win)
        n=Entry(Point(70,40),10).draw(win)
        ok=Button(win,Point(50,10),10,10,"OK")
        mc=win.checkMouse()
        while True:
            if ok.clicked(mc):
                win.close()
                return int(probA.getText())/100,int(probB.getText())/100,int(n.getText())
            mc=win.checkMouse()
            
    def instructions(self):
        pass
        
def main():
    #for text interface
    print(intro())
    probA,probB,n=getInputs()
    play=Play(probA,probB,n)
    play.printSummary()
    print(play.returnSummary())

def main1():
    #for graphical interface
    b=GraphicsRacquetball()
    
if __name__=='__main__':
    main1()
    


