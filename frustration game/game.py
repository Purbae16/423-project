from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from player import Player
from enemy import Enemy
from midpoint import Line
from level_selector import level_selector

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


death=0
level=1
field, player = level_selector(level)



# Keep track of pressed keys
pressed_keys = set()
#field = Field(250, 250, 200, 200)
#player = Player(260, 260, 10, 10)



def animate():
    global level,death, field, player

    if level == 1:
        field.move_enemies(8)

        # for enemy in field.enemy:
        #     if (player.x + player.width >= enemy.x - enemy.radius and player.x <= enemy.x + enemy.radius) and \
        #        (player.y >= enemy.y - enemy.radius and player.y <= enemy.y + enemy.radius):
        #         # Reset player position
        #         player.x = player.startx
        #         player.y = player.starty
        #         death+=1
        #         print(death)
        for enemy in field.enemy:

            distance = ((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2) ** 0.5
        
            sum_of_radii = player.width + enemy.radius

    
            if distance <= sum_of_radii:
                # Reset player position
                player.x = player.startx
                player.y = player.starty
                death += 1
                print(death)


        if player.x>=560 and 250<=player.y<=500:
            level+=1
            field,player=level_selector(level)
   

    if level == 2:
        field.move_enemies(8)

        # for enemy in field.enemy:
        #     if (player.x + player.width >= enemy.x - enemy.radius and player.x <= enemy.x + enemy.radius) and \
        #        (player.y >= enemy.y - enemy.radius and player.y <= enemy.y + enemy.radius):
        #         # Reset player position
        #         player.x = player.startx
        #         player.y = player.starty
        #         death+=1
        #         print(death)
        for enemy in field.enemy:

            distance = ((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2) ** 0.5

            sum_of_radii = player.width + enemy.radius

            if distance <= sum_of_radii:
                # Reset player position
                player.x = player.startx
                player.y = player.starty
                death += 1
                print(death)

        if player.x >= 560 and 230 <= player.y <= 290:
            level += 1
            field, player = level_selector(level)
        






#DEATH COUNT PRINTING
def draw_death_count():
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(SCREEN_WIDTH - 450, SCREEN_HEIGHT - 20)
    death_str = "Deaths: " + str(death)
    for char in death_str:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

button_size = 30
padding = 20
button_colors = (0.28, 0.82, 0.8), (1, 0.76, 0), (1, 0, 0)
button_1x, button_2x = padding, SCREEN_WIDTH - button_size - padding
button_y = SCREEN_HEIGHT - padding - button_size
game_over = False

def draw_restart():
    global button_1x, button_y, button_size
    line_instance = Line()  
    x, y = button_1x, button_y
    point_1 = x, y + button_size // 2
    point_2 = x + button_size // 2, y
    point_3 = x + button_size, y + button_size // 2
    point_4 = x + button_size // 2, y + button_size
    line_instance.drawLine(*point_1, *point_2)
    line_instance.drawLine(*point_1, *point_3)
    line_instance.drawLine(*point_1, *point_4)

def draw_exit():
    global button_2x, button_y, button_size, button_colors
    x, y = button_2x, button_y
    line_instance = Line() 
    point_1 = x, y + button_size
    point_2 = x, y
    point_3 = x + button_size, y
    point_4 = x + button_size, y + button_size
    line_instance.drawLine(*point_1, *point_3)
    line_instance.drawLine(*point_2, *point_4)


def mouseListener(button, state, x, y):
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            global SCREEN_HEIGHT, button_1x, button_2x, button_y, button_size, game_over
            y = SCREEN_HEIGHT - y
            if button_y <= y <= button_y + button_size:
                if button_1x <= x <= button_1x + button_size:    #restart button
                    game_over = False
                    player.x = player.startx
                    player.y = player.starty
                    field.move_enemies(5)
                    print("Starting Over!")
                elif button_2x <= x <= button_2x + button_size:  #exit button
                    print(f'Goodbye!')
                    glutLeaveMainLoop() 
  
                
    glutPostRedisplay()


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
    draw_death_count()
    for enemy in field.enemy:
        enemy.draw()
    player.draw()
    draw_restart()
    draw_exit()

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
glutMouseFunc(mouseListener)
# Start the main loop
glutMainLoop()