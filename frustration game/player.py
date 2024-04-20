from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint import Line

line = Line()

class Player:
    def __init__(self, x, y, width, vel=5, color=(1.0, 0.0, 0.0)):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.color = color

    def move(self, direction):
        if direction == 'LEFT' and self.x > 0:
            self.x -= self.vel
        if direction == 'RIGHT' and self.x < 800 - self.width:
            self.x += self.vel
        if direction == 'DOWN' and self.y > 0:
            self.y -= self.vel
        if direction == 'UP' and self.y < 600 - self.width:
            self.y += self.vel


    def draw(self):
        glColor3f(*self.color)  # Set the drawing color
        line.drawLine(self.x, self.y, self.x + self.width, self.y)
        line.drawLine(self.x + self.width, self.y, self.x + self.width, self.y + self.width)
        line.drawLine(self.x, self.y + self.width, self.x + self.width, self.y + self.width)
        line.drawLine(self.x, self.y, self.x, self.y + self.width)
    
    