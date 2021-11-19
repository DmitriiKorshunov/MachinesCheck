from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI_widget_main import GUI
from GUI_widget_add_new_mac import NewAddMac


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(QSize(600, 250))
        self.setWindowTitle('График ремонта')
        self.setWindowIcon(QIcon('./statics/oiler.ico'))
        self.exitAct = QAction(QIcon('./statics/Exit.ico'), '&Выход', self)
        self.addAct = QAction(QIcon('./statics/AddNew.ico'),'&Добавить новую машину', self)
        self.addAct.setShortcut('Ctrl+A')
        self.addAct.setStatusTip('Добавить новую машину в базу данных.')
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Выход из приложения')
        self.exitAct.triggered.connect(qApp.quit)
        self.updateAct=QAction(QIcon(),'&Обновить',self)
        self.updateAct.setStatusTip('Загрузить\обновить информацию из баз данных.')
        self.updateAct.triggered.connect(self.UpdateCentralWidget)
        self.addActWidget = NewAddMac()
        self.addAct.triggered.connect(self.addActWidget.show)
        self.statusBar()
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&Файл')
        self.fileMenu.addAction(self.addAct)
        self.fileMenu.addAction(self.exitAct)
        self.editMenu = self.menubar.addMenu('&Правка')
        self.editMenu.addAction(self.updateAct)
        self.show()
        self.setCentralWidget(GUI())


    def UpdateCentralWidget(self):
        self.setCentralWidget(GUI())




