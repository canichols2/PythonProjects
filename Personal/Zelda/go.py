class gameObject:
   xPos = 0
   yPos = 0
   xVel = 0
   yVel = 0
   name = "GenericObject"
   def __init__(self):
      self.type = "generic"
   def __init__(self,name):
      self.name = name
      self.type = "generic"
   

   def update(self):
      xPos = xPos + xVel
      yPos = yPos + yVel

class creature(gameObject):
   health = 10
   name = "Creature"
   def __init__(self):
      self.type = "creature"
      self.name = "Creature"
   def __init__(self,name):
      super().__init__(name)
      self.type = "creature"

class enemy(creature):
   count=0
   def __init__(self,name="enemy"):
      enemy.count = enemy.count +1
      super().__init__("[" + str(enemy.count) + "] "+name)
      self.type = "enemy"

class player(creature):
   health = 5
   name = "link"
   def __init__(self):
      super().__init__()
      self.type = "Player"
   def __init__(self,name="Link"):
      super().__init__(name)
      self.type = "Player"
   