from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint import Line



class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

    def move(self, direction_x, direction_y,field):
        if direction_x < 0 and self.x > 0:
            self.x -= self.vel
        if direction_x > 0 and self.x < 800 - self.width:
            self.x += self.vel
        if direction_y < 0 and self.y > 0:
            self.y -= self.vel
        if direction_y > 0 and self.y < 600 - self.height:
            self.y += self.vel

    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()

    
    