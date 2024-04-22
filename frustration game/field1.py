from OpenGL.GL import *
from Tiles import Tile, Greentile
from enemy import Enemy


class Field1:
    def __init__(self):
        self.tiles=[]
        self.safe=[]
        self.enemy=[]
        self.temp=1


    def draw(self):

        green_x=90
        green_y=380

        x=230
        y=350
        g_x=580
        g_y=380

        l_x=200
        l_y=260

        r_x=550
        r_y=350

        for i in range(5):
            for j in range(3):
                g=Greentile(green_x,green_y)
                self.safe+=[g]
                green_x+=g.width
            green_x=90
            green_y-=g.width

        for i in range(5):
            for j in range(3):
                g=Greentile(g_x,g_y)
                self.safe+=[g]
                g_x+=g.width
            g_x=580
            g_y=g_y-g.height
        
        for i in range(1):
            for j in range(1):
                g=Greentile(l_x,l_y)
                self.safe+=[g]
                l_x+=g.width
            l_x=200
            l_y=260

        for i in range(1):
            for j in range(1):
                g=Greentile(r_x,r_y)
                self.safe+=[g]
                r_x+=g.width
            r_x=200
            r_y=350



        for i in range(4):
            for j in range(10):
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

            x=230
            y=y-t.width



        if self.temp==1:
            add = 0
            for i in range(2):
                e = Enemy(525, 275 + add, 4,"RIGHT",2)
                self.enemy.append(e)
                add = add + 60
            add = 0
            for j in range(2):
                e = Enemy(252, 245 + add, 4,"LEFT",2)
                self.enemy.append(e)
                add = add + 60
            self.temp+=1

    # def move_enemies(self,vel):

    #     for enemy in self.enemy:
    #         if enemy.direction=="UP":
    #             enemy.y-=vel
    #             if enemy.y<=170:
    #                 enemy.direction="DOWN"
    #         if enemy.direction == "DOWN":
    #             enemy.y += vel
    #             if enemy.y >= 345:
    #                 enemy.direction = "UP"
    #                 enemy.y += vel
            
    def move_enemies(self, vel):
        for enemy in self.enemy:
            if enemy.direction == "LEFT":
                enemy.x -= vel
                if enemy.x <= 230:
                    enemy.direction = "RIGHT"
            if enemy.direction == "RIGHT":
                enemy.x += vel
                if enemy.x >= 520:
                    enemy.direction = "LEFT"
                    enemy.x += vel

     

     

    



        

        



        








