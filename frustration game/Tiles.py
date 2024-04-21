from OpenGL.GL import *
import random


class Tile:  # x0 is top left, x1 is top right, x2 is bottom left, x3 is bottom right
    def __init__(self, x0,y0):

        self.height=30
        self.width=30
        self.startx=x0
        self.starty=y0

        glColor3f(1, 1, 1)
        Line(x0,y0,x0+self.width,y0)
        Line(x0,y0,x0,y0-self.height)
        Line(x0,y0-self.height,x0+self.width,y0-self.height)
        Line(x0+self.width,y0-self.height,x0+self.width,y0)

        fillSquare(x0, y0, self.width, (1,1,1))

class Greentile:
    def __init__(self, x0,y0):

        self.height=30
        self.width=30
        self.startx=x0
        self.starty=y0

        glColor3f(0.0, 0.8, 0.1)
        Line(x0,y0,x0+self.width,y0)
        Line(x0,y0,x0,y0-self.height)
        Line(x0,y0-self.height,x0+self.width,y0-self.height)
        Line(x0+self.width,y0-self.height,x0+self.width,y0)

        fillSquare(x0, y0, self.width, (0.0,0.8,0.1))


def WritePixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()



def findZone(x, y):
    zone = 0
    dx = abs(x[1] - x[0])
    dy = abs(y[1] - y[0])

    if dx >= dy:
        if x[0] <= x[1]:
            if y[0] <= y[1]:
                zone = 0
            else:
                zone = 7
        else:
            if y[0] <= y[1]:
                zone = 3
            else:
                zone = 4
    else:
        if y[0] <= y[1]:
            if x[0] <= x[1]:
                zone = 1
            else:
                zone = 2
        else:
            if x[0] <= x[1]:
                zone = 6
            else:
                zone = 5
    return zone


def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def convertFromZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def Line(x1, y1, x2, y2):
    zone = findZone((x1, x2), (y1, y2))
    x1, y1 = convertToZone0(x1, y1, zone)
    x2, y2 = convertToZone0(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1

    x1,x2=int(x1),int(x2)
    for x in range(x1, x2 + 1):
        x_orig, y_orig = convertFromZone0(x, y, zone)
        WritePixel(x_orig, y_orig)
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE


def fillSquare(x,y, width, color=(0.0,0.0,0.0) ):
        glColor3f(*color)
        
        x0 = x
        y0 = y - width

        for i in range(y0, y + 1):
            Line(x0, i, x + width, i)
