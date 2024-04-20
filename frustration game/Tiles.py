from OpenGL.GL import *
from midpoint import Line


class Tile:  # x0 is top left, x1 is top right, x2 is bottom left, x3 is bottom right
    def __init__(self, x0,y0,x1,y1,x2,y2,x3,y3):
        Line(x0,y0,x1,y1)
        Line(x0,y0,x2,y2)
        Line(x2,y2,x3,y3)
        Line(x3,y3,x1,y1)




