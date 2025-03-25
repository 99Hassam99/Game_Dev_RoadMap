from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0, 0, 0)  # Black background

game = MyGame()
game.run()