from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


player = Player(50, 50, 10, 10)



def update(value):
    keys = glutGetModifiers()
    if keys & GLUT_ACTIVE_SHIFT:
        player.move_special(GLUT_ACTIVE_SHIFT)
    else:
        player.move_normal()
    enemy.move(50, 250)
    glutTimerFunc(50, update, 0)  # Call update function again after 50 milliseconds

# Function to draw the scene
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    player.draw()
    enemy.draw()
    glutSwapBuffers()

# Function to handle window resizing
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Initialize OpenGL and create window
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow(b"OpenGL Player and Enemy")
glClearColor(0.0, 0.0, 0.0, 1.0)
gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

# Register callbacks
glutDisplayFunc(draw)
glutReshapeFunc(reshape)
glutTimerFunc(0, update, 0)

# Start the main loop
glutMainLoop()
