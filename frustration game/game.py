from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from player import Player
from field import Field
from enemy import Enemy

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

field = Field(250, 250, 200, 200) 
player = Player(260, 260, 10, 10)
enemy = Enemy(50, 100, 5, 5, 15)
enemy2 = Enemy(50, 150, 5, 5, 15)
enemy3 = Enemy(250, 150, 5, 5, 15)
enemy4 = Enemy(250, 200, 5, 5, 15)




# def collide(self, enemy):
#     # Calculate the distance between the player and the enemy
#     dx = self.x - enemy.x
#     dy = self.y - enemy.y
#     distance = math.sqrt(dx**2 + dy**2)

    
#     if distance < self.width + enemy.width:
#         return True
#     else:
#         return False

# def update():
    
#     if player.collide(enemy) or player.collide(enemy2) or player.collide(enemy3) or player.collide(enemy4):
#         player.reset()
#         player.deaths += 1

   
#     glutPostRedisplay()


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
    enemy.draw()
    enemy2.draw()
    enemy3.draw()
    enemy4.draw()
    
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

