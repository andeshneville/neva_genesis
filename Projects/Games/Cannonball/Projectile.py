#Projectile.py

"""Projectile.py
Provides a simple class for modeling the flight
of projectiles."""

from math import*

class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance.
    Tracking is done in two dimensions, heigh(y) and distance (x)"""
    
    def __init__(self,angle,velocity,height):

        """Create a projectile with given launch angle, initial
            velocity and height"""
        
        self.xpos=0.0
        self.ypos=height
        theta=radians(angle)
        self.xvel=velocity * cos(theta)
        self.yvel=velocity * sin(theta)
        self.maxY=height

    def getX(self):
        "Returns the x position(distance) of this projectile."
        return self.xpos

    def getY(self):
        "Returns the Y position (height) of this projectile."
        return self.ypos

    def update(self,time):
        """Update the state of this projectile to move it time seconds
            farther into its flight"""
        self.xpos=self.xpos + time * self.xvel
        yvel1=self.yvel - time * 9.8
        ypos1=time*(self.yvel+yvel1)/2.0
        if ypos1>=0:
            self.maxY=int(self.ypos)

        self.ypos=self.ypos+ypos1
        self.yvel=yvel1

        

    def getMaxY(self):
        return self.maxY        
        
    
        









