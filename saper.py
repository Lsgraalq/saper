"""
Игра "Сапер" на PyQt5
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random
import time

LEVELS = (
    (8, 10),
    (16, 40),
    (24, 99)
)

IMG_BOMB = QImage('C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/bomb.png')
IMG_CLOCK = QImage('C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/clock.png')
IMG_START = QImage('C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/rocket.png')
IMG_FLAG = QImage('C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/flag.png')

STATUS_READY = 0
STATUS_PLAY = 1
STATUS_FAILED = 2
STATUS_SUCCESS = 3

STATUS_ICONS = {
    STATUS_READY: "C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/plus.png",
    STATUS_PLAY: "C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/smiley.png",
    STATUS_FAILED: "C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/cross.png",
    STATUS_SUCCESS: "C:/Users/Ilya/Desktop/PyQt5/Test/pyqt-saper-2022-main/images/smiley-lol.png",
}

class MainWindow(QMainWindow):


    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)

        self.level = 0
        self.board_size, self.n_mines = LEVELS[self.level]

        self.setWindowTitle("saper")
        self.setFixedSize(300,300)
        self.initUI()
        self.show()

    
    def initUI(self):
        """Настройка интерфейса"""

        w = QWidget()
        hb = QHBoxLayout()


        self.mines = QLabel(str(self.n_mines))
        self.mines.setAlignment(Qt.AlignCenter)   
        self.clock = QLabel("000")
        self.clock.setAlignment(Qt.AlignCenter)
        
        f = self.mines.font()
        f.setPointSize(24)
        f.setWeight(75)
        self.mines.setFont(f)
        self.clock.setFont(f)

        self.button = QPushButton()
        self.button.setFixedSize(32, 32)
        self.button.setIconSize(QSize(32,32))
        self.button.setIcon(QIcon('./images/smiley.png'))
        self.button.setFlat(True)

        hb.addWidget(self.mines)
        hb.addWidget(self.button)
        hb.addWidget(self.clock)

        vb = QVBoxLayout()
        vb.addLayout(hb)

        w.setLayout(vb)
        self.setCentralWidget(w)





if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()





