from field2 import *
from field1 import *
from field2 import *
from player import Player
def level_selector(level):
    if level==1:
        field = Field1()
        player = Player(120, 260, 15, 10)
    if level == 2:
        field = Field2()
        player = Player(120, 260, 15, 10)



    return field, player