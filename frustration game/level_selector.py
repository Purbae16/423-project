from field2 import *
from field import Field
from field2 import *
from player import Player
def level_selector(level):
    if level==1:
        field = Field2()
        player = Player(260, 260, 20, 10)
    if level == 2:
        field = Field2()
        player = Player(120, 260, 18, 10)



    return field, player