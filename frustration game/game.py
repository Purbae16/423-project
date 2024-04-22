from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from player import Player
from field import Field
from enemy import Enemy
from level_selector import level_selector

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



level=2
field, player =level_selector(level)



# Keep track of pressed keys
pressed_keys = set()
#field = Field(250, 250, 200, 200)
#player = Player(260, 260, 10, 10)



def animate():
    global level
    vel=2
    if level == 2:
        for enemy in field.enemy:
            if enemy.direction=="UP":
                enemy.y-=vel
                if enemy.y<=185:
                    enemy.direction="DOWN"
            if enemy.direction == "DOWN":
                enemy.y += vel
                if enemy.y >= 345:
                    enemy.direction = "UP"
                    enemy.y += vel













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
def specialKeyDownListener(key, x, y):
    pressed_keys.add(key)
    handleMovement()

# Function to handle arrow key releases
def specialKeyUpListener(key, x, y):
    pressed_keys.remove(key)
    handleMovement()

# Function to handle player movement
def handleMovement():
    direction_x = 0
    direction_y = 0

    if GLUT_KEY_LEFT in pressed_keys:
        direction_x -= 1
    if GLUT_KEY_RIGHT in pressed_keys:
        direction_x += 1
    if GLUT_KEY_DOWN in pressed_keys:
        direction_y -= 1
    if GLUT_KEY_UP in pressed_keys:
        direction_y += 1

    player.move(direction_x, direction_y,field)
    glutPostRedisplay()

# Function to draw the scene
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    field.draw()
    for enemy in field.enemy:
        enemy.draw()
    player.draw()

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
glutSpecialFunc(specialKeyDownListener)  # Register specialKeyDownListener for key press
glutSpecialUpFunc(specialKeyUpListener)   # Register specialKeyUpListener for key release
glutIdleFunc(animate)
# Start the main loop
glutMainLoop()