from graphics import*
import math

#draw a table with rows as wind speed and columns as temperatures
#Speed range is 0 to 50 in 5mph increments
#Temperature range is from -20 to 60 in 10 degree increment
#calculate the values for winndchill


def table(win):
    x1=-20
    y1=0

    #draw the first horizontal and the last horizontal lines
    line1=Line(Point(-20,55),Point(70,55)).draw(win)
    line2=Line(Point(70,0),Point(70,55)).draw(win)
    while y1<=50:
        line=Line(Point(x1,y1),Point(70,y1))
        line.draw(win)
        label=Text(Point(-30,y1+2.5),y1)
        label.draw(win)
        y1=y1+5
    while x1<=60:
        line=Line(Point(x1,0),Point(x1,55))
        line.draw(win)
        label=Text(Point(x1+5,-5),x1)
        label.draw(win)
        x1=x1+10
    

def main():
    #create a Window
    win=GraphWin("Table for WindChill",320,240)
    win.setCoords(-40,-20,80,65)
    #draw table
    table(win)
    #iniitialize speed
    speed=0
    while speed<=50:
        temperature=-20
        while temperature<=60:
            windchill=35.74+(0.6215*temperature)-(35.75*(speed**0.16))+(0.4275*temperature*(speed**0.16))
            #table(win,temperature,speed,windchill)
            label=Text(Point(temperature+5,speed+2.5),int(windchill))
            label.draw(win)
            temperature=temperature+10
        speed=speed+5

main()

    
