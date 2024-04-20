from OpenGL.GL import *
from midpoint import Line


class Tile:  # x0 is top left, x1 is top right, x2 is bottom left, x3 is bottom right
    def __init__(self, x0,y0):

        self.height=18
        self.width=18
        Line(x0,y0,x0+self.width,y0)
        Line(x0,y0,x0,y0-self.height)
        Line(x0,y0-self.height,x0+self.width,y0-self.height)
        Line(x0+self.width,y0-self.height,x0+self.width,y0)




