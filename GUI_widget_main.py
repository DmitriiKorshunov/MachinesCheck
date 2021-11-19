#!/venv/lib/python3.9
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ORM_function import *
import datetime


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.set_window_layout()

    def set_window_layout(self):

        # Labels
        #         Main Label
        self.mainLabel = QLabel()
        self.mainLabel.setText("Электронная cистема учета сроков ремонта машин.")
        self.mainLabel.setFont(QFont('Arial', 18))

        #         Name Field 1
        self.nameField1 = QLabel()
        self.nameField1.setText('Машина:')
        self.nameField1.setFont(QFont('Arial', 13))

        #         Name Field 2
        self.nameField2 = QLabel()
        self.nameField2.setText('Срок ремонта:')
        self.nameField2.setFont(QFont('Arial', 13))

        #          Name Field 3
        self.nameField3 = QLabel()
        self.nameField3.setText('Коментарий:')
        self.nameField3.setFont(QFont('Arial', 13))


        #        DateEdit
        self.dateEditFrom = QLabel()
        self.dateEditFrom.setText(' с ')
        self.dateEditTo = QLabel()
        self.dateEditTo.setText(' по ')
        self.dateEditFrom.setFont(QFont('Arial', 13))
        self.dateEditTo.setFont(QFont('Arial', 13))

        # Field
        #         Machines
        self.MachinesCB = QComboBox()
        self.MachinesCB.setFixedSize(170, 25)
        self.ItemsForCB()

        #         Date of repair
        self.nowDate = datetime.datetime.now()
        self.repairFrom = QDateEdit(self.nowDate)
        self.repairTo = QDateEdit(self.nowDate)

        #         Comments
        self.comm = QLineEdit()
        self.comm.setFixedSize(475, 25)
        self.comm.setMaxLength(5000)
        self.comm.setStatusTip('Максимум - 5000 знаков')

        # Buttons
        #       Input data
        self.btnInputData = QPushButton()
        self.btnInputData.setText('Внести')
        self.btnInputData.setStatusTip('Внести изменения в график ремонта')
        self.btnInputData.clicked.connect(self.AddNewDateRepair)

        # Layouts

        #         Vertical
        self.hBox1 = QHBoxLayout()
        self.hBox1.addWidget(self.mainLabel)
        self.hBox2 = QHBoxLayout()
        self.hBox2.addWidget(self.nameField1)
        self.hBox2.addWidget(self.MachinesCB)
        self.hBox2.addStretch(5)
        self.hBox3 = QHBoxLayout()
        self.hBox3.addWidget(self.nameField2)
        self.hBox3.addWidget(self.dateEditFrom)
        self.hBox3.addWidget(self.repairFrom)
        self.hBox3.addWidget(self.dateEditTo)
        self.hBox3.addWidget(self.repairTo)
        self.hBox3.addStretch(5)
        self.hBox4 = QHBoxLayout()
        self.hBox4.addWidget(self.btnInputData)
        self.hBox5 = QHBoxLayout()
        self.hBox5.addWidget(self.nameField3)
        self.hBox5.addWidget(self.comm)
        self.hBox5.addStretch(5)

        #         Horizontal
        self.vBox = QVBoxLayout()
        self.vBox.addLayout(self.hBox1)
        self.vBox.addLayout(self.hBox2)
        self.vBox.addLayout(self.hBox3)
        self.vBox.addLayout(self.hBox5)
        self.vBox.addLayout(self.hBox4)
        # End
        self.setLayout(self.vBox)

    def ItemsForCB(self):
        self.items = list()
        self.nameList = ListAllMachine()
        if not (len(self.nameList) == 0):
            for t in self.nameList:
                self.items.append(str(t[1]))
            self.MachinesCB.addItems(self.items)
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText('В базе данных не обнаружены записей о существующих машиных!'
                                   'Добавьте новые машины (Ctrl+A).')
            msg.setWindowTitle("Внимание!")
            msg.exec_()
            return

    def AddNewDateRepair(self):
        self.name=self.MachinesCB.currentText()
        self.dateFrom=self.repairFrom.dateTime()
        self.dateFromText = self.dateFrom.toString('dd-MM-yyyy')
        self.dateTo=self.repairTo.dateTime()
        self.dateToText = self.dateTo.toString('dd-MM-yyyy')
        self.comment = self.comm.text()
        self.dateFromTextDay = self.dateFromText.split('-')[0]
        self.dateFromTextMonth = self.dateFromText.split('-')[1]
        self.dateFromTextYear = self.dateFromText.split('-')[2]
        self.dateToTextDay = self.dateToText.split('-')[0]
        self.dateToTextMonth = self.dateToText.split('-')[1]
        self.dateToTextYear = self.dateToText.split('-')[2]
        self.periodFrom = datetime.datetime(int(self.dateFromTextYear),
                                            int(self.dateFromTextMonth),
                                            int(self.dateFromTextDay))
        self.periodTo = datetime.datetime(int(self.dateToTextYear),
                                          int(self.dateToTextMonth),
                                          int(self.dateToTextDay))
        self.period = self.periodTo - self.periodFrom
        print(type(self.period.days))
        if self.period.days<0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Дата окончания ремонта наступает перед датой его начала! '
                                   'Проверьте данные ввода!')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return ()
        else:
            try:
                AddNewRepair(self.name,self.dateFromText,self.dateToText,self.comment)
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('Ошибка при записи в базу данных. Попробуйте снова! Ошибка может быть связана с'
                                       'некоректно выбранным именем.')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                return ()