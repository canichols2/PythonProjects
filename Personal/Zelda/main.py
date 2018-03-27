# import time
import go


class game:
    # gameObjects = set()
    gameObjects = [None]*0

    def __init__(self):
        player = go.Player()
        self.gameObjects.append(player)

    def update(self):
        x = 1 + 1

    def uInput(self):
        option = input(">")
        if option == "c":
            name = input("Creature>")
            # name = "Cody"
            # print("going to add ",name)
            self.gameObjects.append(go.Creature(name))
        elif option == "e":
            name = input("enemy>")
            # name = "Cody"
            # print("going to add ",name)
            self.gameObjects.append(go.Enemy(name))
        elif option == "kill":
            print("STUB: killed creature")

    def render(self):
        for obj in self.gameObjects:
            print("--", obj.type, ":", obj.name)

    def gameLoop(self):
        cont = True
        # frameSkip = 1
        while(cont):
            # startTime = time.time()
            self.uInput()
            self.update()
            self.render()
            go.GameObject.updateObjects()
            # Dont' need these until I make it realtime
            # holdTime = startTime + frameSkip - time.time()
            # print("hold time prev: ",holdTime)
            # holdTime = holdTime if holdTime < 0 else 0
            # print("hold time after: ",holdTime)
            # time.sleep(holdTime)


zelda = game()
zelda.gameLoop()
