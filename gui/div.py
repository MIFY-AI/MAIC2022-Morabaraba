from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class Div(QLabel, QWidget, QtCore.QObject):

    def __init__(self, parent=None):
        super(Div, self).__init__(parent)
        # Dimensions
        self.setMinimumSize(40, 40)
        self.setScaledContents(False)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.trigger = QtCore.pyqtSignal(int, int)

        # In Game
        self.piece = None
        self.active = False
        self.backgroundColor = "white"
