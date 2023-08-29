#shortTracker.py

from graphics import*
from Projectile import Projectile
from random import randrange
from time import sleep
from math import*
from buttons import*

class ShortTracker:
    """It trackes the projectile of the cannonball,
        synching a call to both the projectile and
        Circle classes"""

    def __init__(self,win,angle,velocity,height):
        """"win is the GraphWin to display the shot. Angle,
            velocity, and height are initial  projectile
            parameters"""

        self.proj=Projectile(angle,velocity,height)
        self.marker=Circle(Point(0,height),3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self,dt):
        "Move the shot dt seconds farther along its flight"

        #update the projectile
        self.proj.update(dt)

        #move the circle to the new projectile location
        center=self.marker.getCenter()
        dx=self.proj.getX()-center.getX()
        dy=self.proj.getY()-center.getY()
        self.marker.move(dx,dy)

    def getX(self):
        "returns the current x coordinated of the shot's center"
        return self.proj.getX()
    
    def getY(self):
        "return the current y coordinate of the shot's center"
        return self.proj.getY()
    
    def undraw(self):
        "Undraw the shot"
        self.marker.undraw()

    def getMaxY(self):
        return self.proj.getMaxY()
    


class inputDialog:
    """A custom window for getting simulation values
        (angle,velocity and height) from the User."""

    def __init__(self,angle,vel,height):
        """Build and display the input window"""

        self.win=win=GraphWin("Initial Values",200,300)
        win.setCoords(0,4.5,4,.5)

        Text(Point(1,1),"Angle").draw(win)
        self.angle=Entry(Point(3,1),5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1,2),"Velocity").draw(win)
        self.vel=Entry(Point(3,2),5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1,3),"Height").draw(win)
        self.height=Entry(Point(3,3),5).draw(win)
        self.height.setText(str(height))

        self.fire=Buttons(win,Point(1,4),1.25,.5,"Fire!")
        self.fire.activate()

        self.quit=Buttons(win,Point(3,4),1.25,.5,"Quit")
        self.quit.activate()
    def interact(self):
        """Waits for user to click Quit or Fire button
            Returns a string indicating which button was clicked"""
        while True:
            pt=self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        """Return innput values"""

        a=float(self.angle.getText())
        v=float(self.vel.getText())
        h=float(self.height.getText())

        return a,v,h
    def close(self):
        """Close the input window"""
        self.win.close()

class Launcher:
    def __init__(self,win):
        #draw the base shot of the launcher

        base=Circle(Point(0,0),3)
        base.setFill("red")
        base.setOutline("red")
        base.draw(win)
        #save the window and create initial angle and velocity
        self.win=win
        self.angle=radians(45.0)
        self.vel=60.0

        #create initial "dummy" arrow (needed by redraw)
        self.arrow=Line(Point(0,0),Point(0,0).draw(win))
        #replace it with the correct arrow
        self.redraw()

    def adjAngle(self,amt):
        "Change launnch angle by amt degrees"
        self.angle=self.angle+radians(amt)
        self.redraw()
    
    def adjVel(self,amt):
        "Change launch velocity by amt"
        self.vel=self.vel+amt
        self.redraw()

    def redraw(self):
        "Redraw the arrow to show current angle and velocity"
        self.arrow.undraw()
        pt2=Point(0.5*self.vel*cos(self.angle),0.5*
                  self.vel*sin(self.angle))
        self.arrow=Line(Point(0,0),pt2).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)
        
    def fire(self):
        return ShortTracker(self.win,degrees(self.angle),self.vel,0.0)

    
class ProjectileApp:

    def __init__(self):
        #create graphics window with a scale line at the bottom
        self.win=GraphWin("Projectile Animation",640,480)
        self.win.setCoords(-10,-20,210,155)
        self.win.setBackground("cyan3")
        Line(Point(-10,0),Point(210,0)).draw(self.win)
        for x in range(0,210,30):
            Text(Point(x,-7),str(x)).draw(self.win)
            Line(Point(x,0),Point(x,2)).draw(self.win)
        #add the launcher to the window
        self.launcher=Launcher(self.win)
        #start with an empty list of "live" shots
        self.shots=[]
        
        #set the target
        self.target=CButton(self.win,Point(50,100),4,"X")
        self.newtarget()
        #scores button
        self.hits=0
        self.buttons()
    def buttons(self):
        Text(Point(85,-15),"Hits").draw(self.win)
        self.score=Button(self.win,Point(100,-15),15,10,self.hits)
        self.instr=Button(self.win,Point(140,-15),20,10,"Help")
        self.quit=Button(self.win,Point(180,-15),20,10,"Quit")
    def run(self):
        #main event/animation loop
        mc=self.win.checkMouse()
        while not self.quit.clicked(mc):
            
            self.updateShots(1/30)
            key=self.win.checkKey()
            if key in ["q","Q"]:
                break
            if key in ["Up","A"]:
                self.launcher.adjAngle(5)
            elif key in ["Down","a"]:
                self.launcher.adjAngle(-5)
            elif key in ["Right","V"]:
                self.launcher.adjVel(5)
            elif key in ["Left","v"]:
                self.launcher.adjVel(-5)
            elif key in ["f","F","Return"]:
                self.shots.append(self.launcher.fire())
            for a in self.shots:
                x=a.getX()
                y=a.getY()
                if self.target.clicked(Point(x,y)):
                    self.updateScore()
                    self.newtarget()
            if self.instr.clicked(mc):
                text=Text(Point(100,150),"Still Working On It").draw(self.win)
                sleep(5)
                text.undraw()
                #self.instructions()
            mc=self.win.checkMouse()
            update(30)
            
        self.win.close()
    def updateScore(self):
        self.hits=self.hits+1
        self.score.setLabel(self.hits)
    def updateShots(self,dt):
        alive=[]
        for shot in self.shots:
            shot.update(dt)
            if shot.getY()>=0 and -10<shot.getX()<210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots=alive
        
    def newtarget(self):
        self.target.undraw()
        x=randrange(60,200)
        y=randrange(0,150)
        self.target=CButton(self.win,Point(x,y),3," ")
        self.target.setFill("Black")

    def instructions(self):
        win=GraphWin("Instructions",400,200)
        win.setCoords(0,0,100,100)
        button=Button(win,Point(85,10),10,8,"OK")
        text=Text(Point(40,90),"""This is CannonBall game.
                Try as much as possible to hit the target (Black Ball).""")
        text2=Text(Point(40,60),"""
                Use: "F/f" to fire a ball
                     V/Right Key      to increase velocity of the ball
                     v/Left Key       to decrease velocity of the ball
                     A/Upp key  to increase the angle
                     a/Down key     to decrease the angle.""")
        text3=Text(Point(44,20),"""A new target emerges if you hit the current \n target and your Hits scores is increased.""")
        mc=win.checkMouse()
        text.draw(win)
        text2.draw(win)
        text2.setFill("Green")
        text3.draw(win)
        while not button.clicked(mc):
            mc=win.checkMouse()
        win.close()
        
if __name__=="__main__":
    ProjectileApp().run()


    
