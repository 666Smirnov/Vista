# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PycharmProjects\QT_Disigner\Vista_QT\alphabet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ABC(object):

    def setupUi_Abc(self, Ui_ABC):

        Ui_ABC.setObjectName("Abc")
        Ui_ABC.resize(538, 405)

        self.centralwidget = QtWidgets.QWidget(Ui_ABC)
        self.centralwidget.setObjectName("centralwidget")

        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(120, 90, 291, 31))
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(self.btn_clk)

        self.btn10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn10.setGeometry(QtCore.QRect(120, 270, 291, 31))
        self.btn10.setObjectName("btn10")
        self.btn10.clicked.connect(self.btn_clk)

        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(120, 0, 291, 31))
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.btn_clk)

        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(120, 180, 291, 31))
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(self.btn_clk)

        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(120, 240, 291, 31))
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(self.btn_clk)

        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(120, 60, 291, 31))
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(self.btn_clk)

        self.btn12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn12.setGeometry(QtCore.QRect(120, 330, 291, 31))
        self.btn12.setObjectName("btn12")
        self.btn12.clicked.connect(self.btn_clk)

        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(120, 30, 291, 31))
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.btn_clk)

        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(120, 210, 291, 31))
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(self.btn_clk)

        self.btn13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn13.setGeometry(QtCore.QRect(120, 360, 291, 31))
        self.btn13.setObjectName("btn13")
        self.btn13.clicked.connect(self.btn_clk)

        self.btn11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn11.setGeometry(QtCore.QRect(120, 300, 291, 31))
        self.btn11.setObjectName("btn11")
        self.btn11.clicked.connect(self.btn_clk)

        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(120, 150, 291, 31))
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(self.btn_clk)

        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(120, 120, 291, 31))
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(self.btn_clk)

        Ui_ABC.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(Ui_ABC)
        self.statusbar.setObjectName("statusbar")
        Ui_ABC.setStatusBar(self.statusbar)


        '''
        self.retranslateUi(Ui_ABC)
        QtCore.QMetaObject.connectSlotsByName(Ui_ABC)'''

        self.btn4.setText("ЖЗИЙ")
        self.btn10.setText("ФХ")
        self.btn1.setText("АБ")
        self.btn7.setText("ОП")
        self.btn9.setText("ТУ")
        self.btn3.setText("ДЕ")
        self.btn12.setText("ЪЫЬЭ")
        self.btn2.setText("ВГ")
        self.btn8.setText("РС")
        self.btn13.setText("ЮЯ")
        self.btn11.setText("ЦЧШЩ")
        self.btn6.setText("МН")
        self.btn5.setText("КЛ")
    def retranslateUi(self, Ui_ABC):
        _translate = QtCore.QCoreApplication.translate
        Ui_ABC.setWindowTitle(_translate("Abc", "MainWindow"))

    def btn_clk(self):
        import main
        import sql_req
        sender = self.sender()
        req = sql_req.request_Abc(main.conn, sender.text())
        self.setupUi_list(self)