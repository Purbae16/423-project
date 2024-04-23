from OpenGL.GL import *
from Tiles import Tile, Greentile
from enemy import Enemy


class Field3:
    def __init__(self):
        self.tiles=[]
        self.extra=[]
        self.safe=[]
        self.enemy=[]
        self.ball=None
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

            glColor3f(0.6, 0.6, 0.6)
            t = Tile(320 + 90, y+90)
            self.extra += [t]


        if self.temp==1:
            add = 0
            for i in range(5):
                e = Enemy(x+4 + add, y+6, 5,"LEFT",2)
                self.enemy.append(e)
                add = add + 27
            add = 0
            for j in range(3):
                e = Enemy(x + 4 + add, y+120, 5,"RIGHT",2)
                self.enemy.append(e)
                add = add + 27
            add = 0
            for k in range(3):
                e = Enemy(x + 4, y+33+add, 5,"UP",2)
                self.enemy.append(e)
                add = add + 27
            add = 0
            for l in range(3):
                e = Enemy(x + 112, y+33+add, 5,"DOWN",2)
                self.enemy.append(e)
                add = add + 27
            add = 0
            ball = Enemy(x+102, y+180, 2,"DOWN",0,(0.9,0.7,0.0))
            self.ball = ball
            self.temp+=1


        
    
        g=Greentile(green_x,green_y)
        self.safe+=[g]

    def move_enemies(self,vel):

        for enemy in self.enemy:
            if enemy.direction=="LEFT":
                enemy.x-=vel
                if enemy.x<=324:
                    enemy.direction="UP"
            if enemy.direction == "UP":
                enemy.y += vel
                if enemy.y >= 295:
                    enemy.direction = "RIGHT"
            if enemy.direction == "RIGHT":
                enemy.x += vel
                if enemy.x >= 432:
                    enemy.direction = "DOWN"
            if enemy.direction == "DOWN":
                enemy.y -= vel
                if enemy.y <= 190:
                    enemy.direction = "LEFT"
            
            
            
            
