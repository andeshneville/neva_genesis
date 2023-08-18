#Three Button Monte

from graphics import*
from buttons import*
from random import randrange

def main():
    #draw a Window
    win=GraphWin("Three Button Monte",320,400)
    win.setCoords(-20,-20,100,100)

    #Print Intro and Instructions
    start=Button(win,Point(40,10),20,10,"Start")
    pt=win.checkMouse()
    statements=classPrint()
    text=Text(Point(40,50),statements.intro())
    text.setFill('green')
    while not start.clicked(pt):
        text.draw(win)
        pt=win.getMouse()
        text.undraw()
    start.undraw()
    #create buttons
    label="click Me"
    winnings=0
    no_of_games=0
    quitb=Button(win,Point(0,-10),20,10,"Quit")
    button1=Button(win,Point(5,50),30,20,label)
    button2=Button(win,Point(40,50),30,20,label)
    button3=Button(win,Point(80,50),30,20, label)
    instruct=Button(win,Point(20,90),40,10,"Instructions")

    Text(Point(40,5),"Total Wins").draw(win)
    wins=Button(win,Point(70,5),20,10,winnings)
    wins.setFill("green")
    Text(Point(40,-10),"Total Games").draw(win)
    gButton=Button(win,Point(70,-10),20,10,no_of_games)
    
    mc=win.getMouse()
    while not quitb.clicked(mc):
        correct=randrange(1,4)
        won=simOneGame(button1,button2,button3,correct,mc)
        if won==True:
            winnings=winnings+1
            no_of_games=no_of_games+1
        elif won==False:
            no_of_games=no_of_games+1
        wins.setLabel(winnings)
        gButton.setLabel(no_of_games)
        if instruct.clicked(mc):
            won=GraphWin("Instructions",350,200)
            t=Text(Point(150,100),statements.instructions())
            t.setFill('blue')
            t.draw(won)
            te=Text(Point(150,180),"Click Anywhere to close this window")
            te.setFill("Red")
            te.draw(won)
            won.getMouse()
            won.close()
            
        mc=win.getMouse()
    win.close()
def simOneGame(button1,button2,button3,a,mc):
    if button1.clicked(mc) and a==1:
        button1.setLabel("Right")
        button1.setFill("Green")
        return True
    elif button2.clicked(mc) and a==2:
        button2.setLabel("Right")
        button2.setFill("Green")
        return True
    elif button3.clicked(mc) and a==3:
        button3.setLabel("Right")
        button3.setFill("Green")
        return True
    elif button1.clicked(mc) and a!=1:
        button1.setLabel("Wrong")
        button1.setFill('red')
        return False
    elif button2.clicked(mc) and a!=2:
        button2.setLabel("Wrong")
        button2.setFill('red')
        return False
    elif button3.clicked(mc) and a!=3:
        button3.setLabel("Wrong")
        button3.setFill('red')
        return False


class classPrint:
    """Prints Any Related Information to the game"""

    def __init__(self):
        """Set the Location for the Text on the Window"""

    def intro(self):
        a=""" Welcome to Three Button Monte
In this game, the player tries to guess
the correct button out of the three buttons.
The correct answer (computer's guess) is then
displayed.
Your scores and the number of games played
are displayed"""
        return a

    def instructions(self):
        a=""" Please guess the correct button out of the
                three buttons and click on it.
                If the button you clicked coincides with the
                button the computer chose, you win, otherwise
                you lose."""
        return a        


if __name__=='__main__':
    main()








