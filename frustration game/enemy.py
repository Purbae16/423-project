from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rand

def drawCircle(x, y, cir_x, cir_y):
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(x + cir_x, y + cir_y)
    glVertex2f(y + cir_x, x + cir_y)

    glVertex2f(y + cir_x, -x + cir_y)
    glVertex2f(x + cir_x, -y + cir_y)

    glVertex2f(-x + cir_x, -y + cir_y)
    glVertex2f(-y + cir_x, -x + cir_y)

    glVertex2f(-y + cir_x, x + cir_y)
    glVertex2f(-x + cir_x, y + cir_y)

    glEnd()
    glFlush()


def midpoint(cir_x, cir_y, radius):
    d = 1 - radius
    x = 0
    y = radius

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        drawCircle(x, y, cir_x, cir_y)


class Enemy:
    def __init__(self, x, y, radius,direction, vel=0, color=(0.0,0.0,1.0),right=True ):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = vel
        self.color = color
        self.direction=direction
        self.right = right
        
        midpoint(self.x, self.y, self.radius )




    def draw(self):
        glColor3f(*self.color)
        midpoint(self.x, self.y, self.radius )
        




    def move(self, bound_x1, bound_x2):
        if self.x < bound_x1 or self.x > bound_x2:
            self.right = not self.right
        if self.right:
            self.x += self.vel
        else:
            self.x -= self.vel