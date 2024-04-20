from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from player import Player
from field import Field

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

field = Field(250, 250, 200, 200) 
player = Player(260, 260, 10)
#def update(value):
    # No need to check for modifiers here
    #player.move_normal()
    #glutTimerFunc(50, update, 0)  # Call update function again after 50 milliseconds

# Function to handle arrow key presses
def specialKeyListener(key, x, y):
    if key == GLUT_KEY_LEFT:
        player.move('LEFT')
    elif key == GLUT_KEY_RIGHT:
        player.move('RIGHT')
    elif key == GLUT_KEY_DOWN:
        player.move('DOWN')
    elif key == GLUT_KEY_UP:
        player.move('UP')
    glutPostRedisplay()

# Function to draw the scene
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    field.draw()
    player.draw()
      # Draw the field
    glutSwapBuffers()
    glutPostRedisplay()

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
glutSpecialFunc(specialKeyListener)  # Register specialKeyListener for arrow key presses
#glutTimerFunc(0, update, 0)

# Start the main loop
glutMainLoop()

