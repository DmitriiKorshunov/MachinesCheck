import sys
from GUI import GUI
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout\
    ,QLabel, QSpinBox, QCheckBox, QComboBox
from PyQt5 import QtGui



if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())