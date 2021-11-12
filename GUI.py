import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

    # Windows size
        self.setFixedSize(QSize(600,200))
        self.setWindowTitle('Machines repair')
        self.setWindowIcon(QIcon('./statics/oiler.ico'))


    # Labels
    #         Main Label
        self.mainLabel=QLabel()
        self.mainLabel.setText("Электронная cистема учета сроков ремонта машин.")
        self.mainLabel.setFont(QFont('Arial',18))

    # Field
    #         Machines
        self.

    # Layouts

    #         Vertical
        self.hBox1 = QHBoxLayout()
        self.hBox1.addWidget(self.mainLabel)
        # self.hBox1.stretch(3)


    #         Horizontal
        self.vBox = QVBoxLayout()
        self.vBox.addLayout(self.hBox1)
    #End
        self.setLayout(self.vBox)
        self.show()

