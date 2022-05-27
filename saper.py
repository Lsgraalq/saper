"""
Игра "Сапер" на PyQt5
"""

from email.charset import QP
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

IMG_BOMB = QImage('./images/bomb.png')
IMG_CLOCK = QImage('./images/clock.png')
IMG_START = QImage('./images/rocket.png')
IMG_FLAG = QImage('./images/flag.png')

STATUS_READY = 0
STATUS_PLAY = 1
STATUS_FAILED = 2
STATUS_SUCCESS = 3

STATUS_ICONS = {
    STATUS_READY: "./images/plus.png",
    STATUS_PLAY: "./images/smiley.png",
    STATUS_FAILED: "./images/cross.png",
    STATUS_SUCCESS: "./images/smiley-lol.png",
}

class MainWindow(QMainWindow):


    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)

        self.level = 0
        self.board_size, self.n_mines = LEVELS[self.level]

        self.setWindowTitle("saper")
        self.initUI()
        self.init_map()
        self.setFixedSize(self.sizeHint())
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

        
        self.l = QLabel()
        self.l.setPixmap(QPixmap.fromImage(IMG_BOMB))
        self.l.setAlignment(Qt.AlignCenter)



        hb.addWidget(self.l)
        hb.addWidget(self.mines)
        hb.addWidget(self.button)
        hb.addWidget(self.clock)
        self.l = QLabel()
        self.l.setPixmap(QPixmap.fromImage(IMG_CLOCK))
        self.l.setAlignment(Qt.AlignCenter)
        hb.addWidget(self.l)

        vb = QVBoxLayout()
        vb.addLayout(hb)


        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        vb.addLayout(self.grid)
        w.setLayout(vb)
        self.setCentralWidget(w)
    

    def init_map(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                w = Cell(x,y)
                self.grid.addWidget(w,x,y)




class Cell(QWidget):
    """
    Клетка игрового поля
    """
    def __init__(self,x,y, *args, **kwargs):
        """
        Конструктор игрового поля
        """

        super().__init__(*args, **kwargs)
        self.setFixedSize(20,20)

        self.x = x 
        self.y = y

    
    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = event.rect()
        outer, inner = Qt.gray, Qt.lightGray
        p.fillRect(r, QBrush(inner))
        pen = QPen(outer)
        pen.setWidth(1)
        p.setPen(pen)
        p.drawRect(r)






if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()





