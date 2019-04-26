__name__ = "Entity"
__version__ = "0.1"

class Entity():
    def __init__(self, size = 16):
        self.x = 0
        self.y = 0
        self.size = size

    def info(self):
        print("I have x= " + self.x + " and y= " + self.y + ";")
        print("size= " + self.size)

class Hero(Entity):
    def __init__(self):
        self.y = 0

class Enemy(Entity):
    def __init__(self, y):
        self.y = y