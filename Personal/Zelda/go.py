class Position:
    def __init__(self, x=0, y=0, xVel=0, yVel=0):
        self.xPos = x
        self.yPos = y
        self.xVel = xVel
        self.yVel = yVel

    def update(self):
        self.xPos = self.xPos + self.xVel
        self.yPos = self.yPos + self.yVel


class GameObject:
    gameobjects = set()
    name = "GenericObject"

    def __init__(self, name="None", position=Position()):
        self.name = name
        self.type = "generic"
        self.pos = position
        GameObject.gameobjects.add(self)

    def update(self, message=""):
        self.pos.update()
        print('{} updated{}'
              .format(self.name,
                      message if message is ""
                      else ": " + message))

    def updateObjects():
        for sub in GameObject.gameobjects:
            sub.update()


class Creature(GameObject):
    def __init__(self, name="Creature", position=Position()):
        super().__init__(name, position)
        self.health = 10
        self.type = "creature"


class Enemy(Creature):
    count = 0

    def __init__(self, name="enemy"):
        Enemy.count = Enemy.count + 1
        super().__init__("[" + str(Enemy.count) + "] "+name)
        self.type = "enemy"


class Player(Creature):
    def __init__(self, name="Link"):
        super().__init__(name)
        self.type = "Player"
        self.health = 5
        self.healthMax = 10
        self.regenTime = 0
        self.regenTimeMax = 5
        self.regenAmmount = 1

    def update(self):
        super().update()
        if self.health < self.healthMax and \
           self.regenTime < self.regenTimeMax:
            self.health = self.health + self.regenAmmount
