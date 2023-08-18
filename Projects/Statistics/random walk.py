

from graphics import*
from random import random, randrange
from math import*
from buttons import Button
from time import*

class RandomWalkDot:
    """Creates a dot that moves randomly"""
    def __init__(self):
        self.startPoint=Point(50,50)
        self.center=self.startPoint
        self.dot=Circle(self.center,1)
        self.xdisp=0
        self.ydisp=0
        
    def step(self):
        angle=random() * 2 * pi
        x= 5*cos(angle)
        y= 5*sin(angle)
        self.dot.move(x,y)
        
    def update(self):
        self.dot.undraw()
        self.step()
        return self.dot
    def getX(self):
        return self.dot.getCenter().getX()
    def getY(self):
        return self.dot.getCenter().getY()

class RandomWalkLine:
    "Creates a line that progresses randomly"
    def __init__(self):
        self.p1=Point(50,50)
        self.p2=Point(50,50)
        self.line=Line(self.p1,self.p2)
            
    def step(self):
        angle=random() * 2 * pi
        x=self.getX()+5*(cos(angle))
        y=self.getY()+5*(sin(angle))
        self.p2=Point(x,y)
        
    def getX(self):
        return self.p2.getX()
    def getY(self):
        return self.p2.getY()
    def update(self):
        self.p1=self.p2
        self.step()
        return Line(self.p1,self.p2)

class GraphicsInterface:
    """Uses the RandomWalkDot and RandomWalkLine classes to
        draw several lines and Dots. This class then monitors
        each and every line and dot drawn"""
    
    def __init__(self):
        "Set's up the Graphic Window"
        self.win=GraphWin("Random Walk",400,400)
        self.win.setCoords(-20,-20,100,100)
        self.stop=Button(self.win,Point(40,-10),20,8,"STOP")
        self.stop.setFill("RED")
        self.adddot=Button(self.win,Point(0,90),25,8,"ADD DOT")
        self.addline=Button(self.win,Point(50,90),25,8,"ADD LINE")
        self.currentWalks=[]
        
    def simulate(self):
        """Keeps Every Drawn line or Dot in motion until the stop
         Button is pressed"""
        self.addDot()
        mc=self.win.checkMouse()
        while not self.stop.clicked(mc):
            for i in self.currentWalks:        
                b=i.update()
                b.draw(self.win)
                b.setFill("Green")
            sleep(0.1)
            if self.adddot.clicked(mc):
                self.addDot()
            if self.addline.clicked(mc):
                self.addLine()                
            mc=self.win.checkMouse()
        self.win.close()
        
    def addDot(self):
        "Starts a new dot"
        dot=RandomWalkDot()
        self.currentWalks.append(dot)
    def addLine(self):
        "Draws a new line"
        line=RandomWalkLine()
        self.currentWalks.append(line)

def main():
    a=GraphicsInterface()
    a.simulate()


if __name__=='__main__':
    main()






