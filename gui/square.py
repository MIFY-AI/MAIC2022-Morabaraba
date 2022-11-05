from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class Square(QLabel, QWidget, QtCore.QObject):

    def __init__(self, col, row, parent=None):
        super(Square, self).__init__(parent)
        # Dimensions
        self.setMinimumSize(70, 70)
        self.setScaledContents(False)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.trigger = QtCore.pyqtSignal(int, int)
        self.col = col
        self.row = row

        # In Game
        self.piece = None
        self.active = False
        self.setStatusTip(self.toNotation())
        self.backgroundColor = "white"

    def enable(self, active):
        self.active = active
        self.setStyleSheet('QLabel { background-color : ' + self.backgroundColor + '; }')

    def set_active(self, color):
        if type(color) == str:
            self.active = True
            self.setStyleSheet('QLabel { background-color : ' + color + '; }')
        elif type(color) == bool:
            self.active = color
            self.setStyleSheet('QLabel { background-color : ' + self.backgroundColor + '; }')

    def is_piece(self):
        if self.piece is None:
            return False
        return True

    def is_active(self):
        return self.active

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece
        self.setPixmap(piece.getImage())
        self.setStatusTip(self.toNotation() + " - " + self.piece.color)

    def remove_piece(self):
        self.piece = None
        empty = QtGui.QPixmap(0, 0)
        self.setPixmap(empty)
        self.setStatusTip(self.toNotation())

    def __set_color(self, color):

        if color == 0:
            self.setStyleSheet("""QLabel { background-color : white; } """)
        elif color == 1:
            self.setStyleSheet("""QLabel { background-color : grey; } """)
        else:
            raise Exception("Incorrect chess square color")
        self.color = color

    def set_background_color(self, color):
        self.backgroundColor = color
        self.setStyleSheet('QLabel { background-color : ' + color + '; }')

    def toNotation(self): # TODO : Tu vas disparaitre
        coordinates = str()
        x = self.col + 49
        y = self.row + 65
        if self.col >= 0 and self.col < self.col and self.row >= 0 and self.row < self.row:
            coordinates += str(str(x) + " ")
            coordinates += str(str(y) + " ")
        return coordinates
