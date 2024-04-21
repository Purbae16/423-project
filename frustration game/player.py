from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#from midpoint import Line

def WritePixel(x, y):
    glPointSize(2)
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



#line = Line()

class Player:
    def __init__(self, x, y, width, vel=5, color=(1.0, 0.0, 0.0)):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.color = color

    def move(self, direction_x, direction_y):
        if direction_x < 0 and self.x > 0:
            self.x -= self.vel
        if direction_x > 0 and self.x < 800 - self.width:
            self.x += self.vel
        if direction_y < 0 and self.y > 0:
            self.y -= self.vel
        if direction_y > 0 and self.y < 600 - self.width:
            self.y += self.vel

    def draw(self):
        # Set the outline color
        glColor3f(*self.color)
        # Draw the outline of the square
        Line(self.x, self.y, self.x + self.width, self.y)  # Top edge
        Line(self.x + self.width, self.y, self.x + self.width, self.y - self.width)  # Right edge
        Line(self.x, self.y - self.width, self.x + self.width, self.y - self.width)  # Bottom edge
        Line(self.x, self.y, self.x, self.y - self.width)  # Left edge

        # Fill the square
        self.fillSquare()

    def fillSquare(self):
        glColor3f(*self.color)
        
        x0 = self.x
        y0 = self.y - self.width

        for y in range(y0, self.y + 1):
            Line(x0, y, self.x + self.width, y)
