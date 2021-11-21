from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ORM_function import *


class NewAddMac(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_widget_window()

    def setup_widget_window(self):
        self.setFixedSize(QSize(580, 150))
        self.setWindowTitle('Добавить новую машину')
        self.setWindowIcon(QIcon('./statics/AddNew.ico'))
        self.setup_widget_add()

    def setup_widget_add(self):
        # Labels
        #         Main Label
        self.mainLabel = QLabel()
        self.mainLabel.setText("Добавление новой машины.")
        self.mainLabel.setFont(QFont('Arial', 18))
        #         Name Field 1
        self.nameField1 = QLabel()
        self.nameField1.setText('Название машины:')
        self.nameField1.setFont(QFont('Arial', 13))

        #         Name Field 2
        self.nameField2 = QLabel()
        self.nameField2.setText('Коментарий:')
        self.nameField2.setFont(QFont('Arial', 13))


    # Field
    #         Machines
        self.machinesName = QLineEdit()
        self.machinesName.setFixedSize(400,25)
        self.machinesName.setFocus()
        self.machinesName.setMaxLength(200)



    #         Date of repair
        self.machinesComm = QLineEdit()
        self.machinesComm.setFixedSize(450,25)


    #       Buttons

        self.btnOK = QPushButton()
        self.btnOK.setText('Внести')
        self.btnOK.setFixedSize(556,25)
        self.btnOK.clicked.connect(self.GetExistMachines)

    # Layouts

    #         Horizontal
        self.hBox1=QHBoxLayout()
        self.hBox1.addWidget(self.mainLabel)
        self.hBox1.addStretch(6)
        self.hBox2=QHBoxLayout()
        self.hBox2.addWidget(self.nameField1)
        self.hBox2.addWidget(self.machinesName)
        self.hBox2.addStretch(2)
        self.hBox3=QHBoxLayout()
        self.hBox3.addWidget(self.nameField2)
        self.hBox3.addWidget(self.machinesComm)
        self.hBox3.addStretch(2)
        self.hBox4=QHBoxLayout()
        self.hBox4.addWidget(self.btnOK)
        self.hBox4.addStretch(2)

    #        Vertical
        self.vBox=QVBoxLayout()
        self.vBox.addLayout(self.hBox1)
        self.vBox.addLayout(self.hBox2)
        self.vBox.addLayout(self.hBox3)
        self.vBox.addLayout(self.hBox4)
        self.setLayout(self.vBox)


    def GetExistMachines(self):
        try:
            self.name = self.machinesName.text()
            if self.name == '':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('При добавлении записи произошла ошибка! Укажите имя машины')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                return ()
            self.comment = self.machinesComm.text()
            self.nameList=ListAllMachine()
            if len(self.nameList)>0:
                for t in self.nameList:
                    if str(t[1])==self.name:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setInformativeText('Вы попытались ввести существующее наименования машины, попробуйте ввести'
                                               ' другое имя!')
                        msg.setWindowTitle("Ошибка")
                        msg.exec_()
                        return()
            result=AddNewMachine(self.name, self.comment)
            if (result):
                msg = QMessageBox()
                msg.setInformativeText('Машина ' + str(self.name) + ' успешно добавлена!'
                                       ' Не забудьте обновить базы данных (Правка->Обновить)!')
                msg.setWindowTitle("Успешно")
                msg.exec_()
                return ()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('При добавлении записи произошла ошибка! \nКод ошибки: addnewmach/ORMFunc')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                return ()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('При добавлении записи произошла ошибка! \nКод ошибки: addnewmach/ORMFunc')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return ()








