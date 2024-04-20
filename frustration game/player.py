from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Player:
    def __init__(self, x, y, width, height, vel=5, color=(1.0, 0.0, 0.0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color

    def move(self, direction):
        if direction == 'LEFT' and self.x > 0:
            self.x -= self.vel
        if direction == 'RIGHT' and self.x < 800 - self.width:
            self.x += self.vel
        if direction == 'DOWN' and self.y > 0:
            self.y -= self.vel
        if direction == 'UP' and self.y < 600 - self.height:
            self.y += self.vel

    def drawPoint(x, y):
        glPointSize(1.5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()

    def findZone(x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        if abs(dx) >= abs(dy):
            if dx >= 0:
                if dy >= 0:
                    return 0
                else:
                    return 7
            elif dx <= 0:
                if dy >= 0:
                    return 3
                else:
                    return 4
        else:
            if dy >= 0:
                if dx >= 0:
                    return 1
                else:
                    return 6
            elif dy <= 0 :
                if dx >= 0:
                    return 2
                else:
                    return 5

    def convertToZone0(x, y, zone):
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
        
    def plotPoint(x, y, zone):
        if zone == 0:
            Player.drawPoint(x, y)
        elif zone == 1:
            Player.drawPoint(y, x)
        elif zone == 2:
            Player.drawPoint(y, -x)
        elif zone == 3:
            Player.drawPoint(-x, y)
        elif zone == 4:
            Player.drawPoint(-x, -y)
        elif zone == 5:
            Player.drawPoint(-y, -x)
        elif zone == 6:
            Player.drawPoint(-y, x)
        elif zone == 7:
            Player.drawPoint(x, -y)

    def drawLine(x0, y0, x1, y1):
        zone = Player.findZone(x0, y0, x1, y1)
        x0, y0 = Player.convertToZone0(x0, y0, zone)
        x1, y1 = Player.convertToZone0(x1, y1, zone)

        dx = x1 - x0
        dy = y1 - y0
        d = 2 * dy - dx
        deltaE = 2 * dy
        deltaNE = 2 * (dy - dx)
        x = x0
        y = y0
        Player.plotPoint(x, y, zone)

        while x < x1:
            if d <= 0:
                d += deltaE
                x += 1
            else:
                d += deltaNE
                x += 1
                y += 1
            Player.plotPoint(x, y, zone)

    def draw(self):
        glColor3f(*self.color)  # Set the drawing color
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()
    
    