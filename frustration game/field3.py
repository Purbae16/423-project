from OpenGL.GL import *
from Tiles import Tile, Greentile
from enemy import Enemy


class Field3:
    def __init__(self):
        self.tiles=[]
        self.extra=[]
        self.safe=[]
        self.enemy=[]
        self.temp=1
    
    def draw(self):

        green_x=365
        green_y=250

        x=320
        y=300
        g_x=560
        g_y=290



        for i in range(4):
            for j in range(4):
                if len(self.tiles) % 2 == 0:
                    glColor3f(0.8,0.8,0.8)
                    t = Tile(x, y)
                    self.tiles += [t]
                    x += t.width
                else:
                    glColor3f(0.6,0.6,0.6)
                    t = Tile(x, y)
                    self.tiles += [t]
                    x += t.width

            x=320
            y=y-t.width

            glColor3f(0.6, 0.6, 0.6)
            t = Tile(320 + 90, y+90)
            self.extra += [t]



        
    
        g=Greentile(green_x,green_y)
        self.safe+=[g]
            
