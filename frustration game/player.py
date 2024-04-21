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
        line.drawLine(self.x, self.y, self.x + self.width, self.y)  # Top edge
        line.drawLine(self.x + self.width, self.y, self.x + self.width, self.y - self.width)  # Right edge
        line.drawLine(self.x, self.y - self.width, self.x + self.width, self.y - self.width)  # Bottom edge
        line.drawLine(self.x, self.y, self.x, self.y - self.width)  # Left edge

        # Fill the square
        self.fillSquare()

    def fillSquare(self):
        glColor3f(*self.color)
        
        x0 = self.x
        y0 = self.y - self.width

        for y in range(y0, self.y + 1):
            line.drawLine(x0, y, self.x + self.width, y)
