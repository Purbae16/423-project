from OpenGL.GL import *
from Tiles import Tile, Greentile
from enemy import Enemy


class Field2:
    def __init__(self):
        self.tiles=[]
        self.safe=[]
        self.enemy=[]
        self.temp=1


    def draw(self):

        green_x=110
        green_y=290

        x=200
        y=350
        g_x=560
        g_y=290

        for i in range(2):
            for j in range(3):
                g=Greentile(green_x,green_y)
                self.safe+=[g]
                green_x+=g.width
            green_x=110
            green_y-=g.width

        for i in range(2):
            for j in range(3):
                g=Greentile(g_x,g_y)
                self.safe+=[g]
                g_x+=g.width
            g_x=560
            g_y=g_y-g.height



        for i in range(6):
            for j in range(12):
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

            x=200
            y=y-t.width


        if self.temp==1:
            add = 0
            for i in range(6):
                e = Enemy(245 + add, 345, 5,"UP",2)
                self.enemy.append(e)
                add = add + 60
            add = 0
            for j in range(6):
                e = Enemy(212 + add, 185, 5,"DOWN",2)
                self.enemy.append(e)
                add = add + 60
            self.temp+=1

    def move_enemies(self,vel):

        for enemy in self.enemy:
            if enemy.direction=="UP":
                enemy.y-=vel
                if enemy.y<=170:
                    enemy.direction="DOWN"
            if enemy.direction == "DOWN":
                enemy.y += vel
                if enemy.y >= 345:
                    enemy.direction = "UP"
                    enemy.y += vel
            
 

    



        

        



        








