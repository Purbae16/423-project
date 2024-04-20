from field import Field
def level_selector(level):
    if level==1:
        field = Field(250, 250, 200, 200)
    if level==2:
        field = Field(250, 500, 200, 200)


    return field