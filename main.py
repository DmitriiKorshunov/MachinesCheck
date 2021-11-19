#!/venv/lib/python3.9
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from GUI_widgets_window import MainWindow



if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())