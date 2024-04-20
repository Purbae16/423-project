from OpenGL.GL import *
from Tiles import Tile


class Field2:
    def __init__(self):
        self.tiles=[]


    def draw(self):

        x=30
        y=350
        if len(self.tiles)%2==0:
            glColor3f(8.0, 8.0, 8.0)
        else:
            glColor3f(6.0, 6.0, 6.0)
        for i in range(6):
            for j in range(12):
                t=Tile(x,y)
                self.tiles+=[t]
                x+=t.width
            x=30
            y=350-t.height








