from OpenGL.GL import *

class Field:
    def __init__(self, x, y, width, height, color=(0, 1, 0)):
        self.x = x
        self.y = y
        self.width = (800)/2
        self.height = (600)/2
        self.color = color

    def draw(self):
    # Calculate the size of each square
        square_width = self.width / 8
        square_height = self.height / 8

        # Loop through rows and columns to draw alternating squares
        for i in range(4):
            for j in range(10):
                # Determine the color of the square based on the row and column indices
                if (i + j) % 2 == 0:
                    glColor3f(1, 1, 1)  # Light color for white squares
                else:
                    glColor3f(0.6, 0.6, 0.8)  # Dark color for black squares
                
                # Calculate the position of the square
                x = self.x + j * square_width
                y = self.y + i * square_height
                
                # Draw the square
                glBegin(GL_QUADS)
                glVertex2f(x, y)
                glVertex2f(x + square_width, y)
                glVertex2f(x + square_width, y + square_height)
                glVertex2f(x, y + square_height)
                glEnd()


        glColor3f(0, 1, 0)  # Green color
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)  # Bottom left corner
        glVertex2f(self.x + 50, self.y)  # Bottom right corner
        glVertex2f(self.x + 50, self.y + 50)  # Top right corner
        glVertex2f(self.x, self.y + 50)  # Top left corner
        glEnd()


# from OpenGL.GL import *

# class Field:
#     def __init__(self, x, y,width,height,color=(0, 1, 0)):
#         self.x = x
#         self.y = y
#         self.width = 400
#         self.height = 300
#         self.color = color

#     # Midpoint Line Drawing Algorithm Implementation
#     def draw_line(self, x1, y1, x2, y2):
        
#         dx, dy = x2 - x1, y2 - y1
#         d = 2 * dy - dx
#         incE, incNE = 2 * dy, 2 * (dy - dx)
#         x, y = x1, y1

#         while x <= x2:
#             self.draw_point(x, y)
#             if d <= 0:
#                 d += incE
#             else:
#                 d += incNE
#                 y += 1
#             x += 1

#     def draw_point(self, x, y):
#         glPointSize(2)
#         glBegin(GL_POINTS)
#         glColor3f(*self.color)
#         glVertex2f(x, y)
#         glEnd()

#     def draw(self):
       
#         square_width = self.width / 8
#         square_height = self.height / 8

#         for i in range(4):
#             for j in range(10):
               
#                 if (i + j) % 2 == 0:
#                     glColor3f(1, 1, 1)  
#                 else:
#                     glColor3f(0.6, 0.6, 0.8)  

            
#                 x = self.x + j * square_width
#                 y = self.y + i * square_height

#                 # Draw the square
#                 glBegin(GL_QUADS)
#                 glVertex2f(x, y)
#                 glVertex2f(x + square_width, y)
#                 glVertex2f(x + square_width, y + square_height)
#                 glVertex2f(x, y + square_height)
#                 glEnd()
           
    
                

        
#         x1, y1 = self.x, self.y
#         x2, y2 = self.x + 50, self.y
#         self.draw_line(x1, y1, x2, y2)
#         self.draw_line(x2, y2, x2, y2 + 50)
#         self.draw_line(x2, y2 + 50, x1, y1 + 50)
#         self.draw_line(x1, y1 + 50, x1, y1)





    