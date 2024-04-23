from OpenGL.GL import *
from Tiles import Tile, Greentile
from enemy import Enemy


class Field3:
    def __init__(self):
        self.tiles=[]
        self.safe=[]
        self.enemy=[]
        self.temp=1
    
    def draw(self):

        green_x=365
        green_y=250

        x=320
        y=300

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

        glColor3f(0.6,0.6,0.6)
        t = Tile(x+90, y+180)
        self.tiles += [t]

        if self.temp==1:
            add = 0
            for i in range(5):
                e = Enemy(x+4 + add, y+6, 5,"UP",2)
                self.enemy.append(e)
                add = add + 27
            add = 0
            for j in range(4):
                e = Enemy(x + 4 + add, y+120, 5,"DOWN",2)
                self.enemy.append(e)
                add = add + 27
            add = 0
            for j in range(4):
                e = Enemy(x + 4, y+120+add, 5,"DOWN",2)
                self.enemy.append(e)
                add = add + 30
            add = 0
            for j in range(4):
                e = Enemy(x + 90, y+add, 5,"DOWN",2)
                self.enemy.append(e)
                add = add + 30
            self.temp+=1
    

        
    
        g=Greentile(green_x,green_y)
        self.safe+=[g]
            
