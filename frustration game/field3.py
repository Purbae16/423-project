from OpenGL.GL import *
from Tiles import Tile, Greentile
from enemy import Enemy


class Field1:
    def __init__(self):
        self.tiles=[]
        self.safe=[]
        self.enemy=[]
        self.temp=1