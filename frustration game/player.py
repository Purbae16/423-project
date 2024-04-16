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
        if direction == 'RIGHT' and self.x < 800 - self.height:
            self.x += self.vel
        if direction == 'DOWN' and self.y < 600 - self.height:
            self.y += self.vel
        if direction == 'UP' and self.y > 0:
            self.y -= self.vel

    def draw(self):
        glColor3f(*self.color)  # Set the drawing color
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()
