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


    def move(self, direction_x, direction_y, field):
        # Calculate the next position
        next_x = self.x + direction_x * self.vel
        next_y = self.y + direction_y * self.vel

        # Check if the next position is within the game region
        for tile in field.tiles + field.safe:
            if (next_x >= tile.startx and next_x <= tile.startx + tile.width) and \
               (next_y >= tile.starty - tile.height and next_y <= tile.starty):
                # The next position is within a tile, so update the player's position
                self.x = next_x
                self.y = next_y
                break

    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()

    
    