import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout \
    , QLabel, QSpinBox, QCheckBox, QComboBox
from PyQt5 import QtGui


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

    # Windows size
        self.resize(800, 800)
        self.move(300, 300)
        self.setWindowTitle('Machines repair')
        self.setWindowIcon(QtGui.QIcon('./statics/oiler.ico'))


    # Labels
    #         Main Label
        self.mainLabel=QLabel()
        self.mainLabel.setText("Электронная истема учета сроков ремонта машин")
        self.mainLabel.move(100,100)
    #End
        self.show()

