from field2 import *
from field import Field
from field2 import *
from player import Player
def level_selector(level):
    if level==1:
        field = Field(250,250,800,600)
        player = Player(260, 260, 10, 10,field)
    if level == 2:
        field = Field2()
        player = Player(260, 260, 10, 10)



    return field, player