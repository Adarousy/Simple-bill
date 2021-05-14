# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DELL\Desktop\project\vatinterface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3, sys
from sqlite3 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from callfullvat import MyForm
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 273)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lname = QtWidgets.QLabel(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(40, 40, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lname.setFont(font)
        self.lname.setAlignment(QtCore.Qt.AlignCenter)
        self.lname.setObjectName("lname")
        self.ponse = QtWidgets.QLabel(self.centralwidget)
        self.ponse.setGeometry(QtCore.QRect(70, 200, 341, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(11)
        self.ponse.setFont(font)
        self.ponse.setText("")
        self.ponse.setAlignment(QtCore.Qt.AlignCenter)
        self.ponse.setObjectName("ponse")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.cr = QtWidgets.QPushButton(self.centralwidget)
        self.cr.setGeometry(QtCore.QRect(100, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.cr.setFont(font)
        self.cr.setStyleSheet("background-color: rgb(209, 155, 255);")
        self.cr.setObjectName("cr")
        self.det = QtWidgets.QPushButton(self.centralwidget)
        self.det.setGeometry(QtCore.QRect(250, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.det.setFont(font)
        self.det.setStyleSheet("background-color: rgb(146, 158, 86);")
        self.det.setObjectName("det")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.det.clicked.connect(self.DET)
        self.cr.clicked.connect(self.createdatabase)
    def DET(self):
        Dialog = QtWidgets.QDialog()
        ui = MyForm()
        ui.show()
        MainWindow.destroy()
        ui.exec_()
    def createdatabase(self):
        try:
            conn = sqlite3.connect(self.lineEdit.text()+".db")
            c = conn.cursor()
            c.execute('CREATE TABLE Details(Date str, name bulding char(30),NetAmount int, Property amount int, Vat int, Total int)')
            self.ponse.setText("Database is Created and Table is created")
        except Error as ee:
            self.ponse.setText("Some error has ocuured")
        finally:
            conn.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lname.setText(_translate("MainWindow", "Enter database Name"))
        self.cr.setText(_translate("MainWindow", "Create database"))
        self.det.setText(_translate("MainWindow", "Go Details"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


