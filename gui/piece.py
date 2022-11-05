from PyQt5 import QtGui


class Piece:
    def __init__(self, player, color):
        self.moveNumber = 0
        self.color = color
        self.player = player

        if color == "white":
            self.image_url = "assets/CBl.png"
        elif color == "green":
            self.image_url = "assets/CV.png"
        elif color == "red":
            self.image_url = "assets/CR.png"
        elif color == "blue":
            self.image_url = "assets/CBlu.png"
        else:
            self.image_url = "assets/CB.png"

    def getImage(self):
        pixmap = QtGui.QPixmap()
        pixmap.load(self.image_url)
        if self.color in ["green", "red", "blue"]:
            pixmap = pixmap.scaledToHeight(33) #
        else :
            pixmap = pixmap.scaledToHeight(30) #
        return pixmap

    def getColor(self):
        return self.color

    def getPlayer(self):
        return self.player

    def getMoveNumber(self):
        return self.moveNumber

    def nextMove(self):
        self.moveNumber += 1
