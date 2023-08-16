
from graphics import*


class Button:
    """A button is labeled rectangle in a window.
        It is activated or deactivated with activate()
        and deactivate() methods respectively.
        The clicked(p) method returns True if the
        button is active and p is inside it."""
    
    def __init__(self,win,center,width,height,label):
        """Creates a Rectangular button e.g
            bg=Button(myWin,centerPoint,Width,height,'Quit'"""
        self.center=center
        x,y=center.getX(),center.getY()
        w,h=width/2,height/2
        self.xmax,self.xmin= x+w,x-w
        self.ymax,self.ymin=y+h,y-h
        
        self.rect=Rectangle(Point(self.xmin,self.ymin),Point(self.xmax,self.ymax))
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label=Text(center,label)
        self.label.draw(win)        
        self.activate()
        
    def activate(self):
        "sets this button to 'active'"
        self.label.setTextColor('black')
        self.rect.setWidth(2)
        self.active=True
        
    def deactivate(self):
        "sets this button to 'inactve'"
        self.label.setTextColor('darkgray')
        self.rect.setWidth(1)
        self.active=False

    def clicked(self,p):
        "returns true if the button is clicked and p is inside"
        if p==None:
            return False
        return (self.active and  self.xmin<=p.getX()<=self.xmax and
                self.ymin<=p.getY()<=self.ymax)
    def setLabel(self,label):
        self.label.setText(label)

    def setFill(self,color):
        self.rect.setFill(color)
    def undraw(self):
        self.rect.undraw()
        self.label.setText("")
        
    def getLabel(self):
        return self.label.getText()
    
def main():
    win=GraphWin("Try",300,300)
    b=Button(win,Point(100,100),50,20,"Try")
    b.setLabel("Quit")
    b.setFill("white")
    print(b.getLabel())
    m=win.getMouse()
    while True:
        if b.clicked(m):
            print("It is working")
        m=win.checkMouse()
if __name__=='__main__':
    main()
