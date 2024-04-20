import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut


class Enemy:
    def __init__(self, x, y, width, height, vel=5, color=(0,0,255), right = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.right = right

    # def draw(self):
    #     gl.glColor3f(0, 0, 0)
    #     self.draw_circle(self.x, self.y, self.width)

    #     gl.glColor3f(*self.color)
    #     self.draw_circle(self.x, self.y, self.width)

    def draw(self):
        gl.glColor3f(0, 0, 0)
        gl.glBegin(gl.GL_POLYGON)
        gl.glVertex2f(self.x, self.y)
        gl.glVertex2f(self.x + self.width, self.y)
        gl.glVertex2f(self.x + self.width, self.y + self.height)
        gl.glVertex2f(self.x, self.y + self.height)
        gl.glEnd()

        gl.glColor3f(*self.color)
        gl.glBegin(gl.GL_POLYGON)
        gl.glVertex2f(self.x, self.y)
        gl.glVertex2f(self.x + self.width, self.y)
        gl.glVertex2f(self.x + self.width, self.y + self.height)
        gl.glVertex2f(self.x, self.y + self.height)
        gl.glEnd()




    def move(self, bound_x1, bound_x2):
        if self.x < bound_x1 or self.x > bound_x2:
            self.right = not self.right
        if self.right:
            self.x += self.vel
        else:
            self.x -= self.vel