from graphics import *
import time
import math
import sys

#set window size (square)
window = 500
#dont mess with these
center = window/2
radius = center * .9
dotSize = 5    
    
def fromPolar(theta, radius):
    x = radius * math.cos(theta)
    y = radius * math.sin(theta) * -1 #fixed it
    return Point(x,y)
    
def scalePoint(point):
    x = (point.getX() * radius) + center
    y = (point.getY() * radius) + center
    return Point(x,y)

def main():
    if len(sys.argv) < 2:
        print("Needs a filename...")
        exit(-1)
    if len(sys.argv) > 2:
        print("Too many arguments...")
        exit(-1)
    #create window
    win = GraphWin("My Circle", window, window)
    #create and draw circle
    c = Circle(Point(window/2, window/2), radius)
    c.draw(win)
    
    inf = open(sys.argv[1], 'r')
    data = inf.read()
    points = data.split('\n')
    
    for i,point in enumerate(points):
        rekt = point.split(' ')
        if len(rekt) != 2:
            print("format issue on line ", i+1)
            continue
        theta = float(rekt[0])
        r = float(rekt[1])
        point = scalePoint(fromPolar(theta, r))
        temp = Circle(point, dotSize)
        temp.setFill("black")
        temp.draw(win) 
        time.sleep(.2)
    try:
        win.getMouse()
    except:
        win.close()# Pause to view result
    win.close()    # Close window when done

main()
