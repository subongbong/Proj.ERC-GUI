# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\PycharmProjects\자율운전 GUI\Ver1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1264, 803)
        MainForm.setStyleSheet("background-color: rgb(225, 224, 224);")
        self.frame1 = QtWidgets.QFrame(MainForm)
        self.frame1.setGeometry(QtCore.QRect(9, 59, 221, 611))
        self.frame1.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.subf1 = QtWidgets.QFrame(self.frame1)
        self.subf1.setGeometry(QtCore.QRect(10, 10, 201, 191))
        self.subf1.setStyleSheet("border-style: outset;\n"
"background-color: rgb(145, 20, 255);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.subf1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subf1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subf1.setObjectName("subf1")
        self.subf1_btn = QtWidgets.QPushButton(self.subf1)
        self.subf1_btn.setGeometry(QtCore.QRect(10, 20, 180, 90))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.subf1_btn.setFont(font)
        self.subf1_btn.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.subf1_btn.setObjectName("subf1_btn")
        self.subf1_label = QtWidgets.QLabel(self.subf1)
        self.subf1_label.setGeometry(QtCore.QRect(10, 130, 180, 40))
        self.subf1_label.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.subf1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subf1_label.setObjectName("subf1_label")
        self.subf2 = QtWidgets.QFrame(self.frame1)
        self.subf2.setGeometry(QtCore.QRect(10, 210, 201, 191))
        self.subf2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.subf2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subf2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subf2.setObjectName("subf2")
        self.subf2_btn = QtWidgets.QPushButton(self.subf2)
        self.subf2_btn.setGeometry(QtCore.QRect(10, 20, 180, 90))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.subf2_btn.setFont(font)
        self.subf2_btn.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.subf2_btn.setObjectName("subf2_btn")
        self.subf2_label = QtWidgets.QLabel(self.subf2)
        self.subf2_label.setGeometry(QtCore.QRect(10, 130, 180, 40))
        self.subf2_label.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.subf2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subf2_label.setObjectName("subf2_label")
        self.subf3 = QtWidgets.QFrame(self.frame1)
        self.subf3.setGeometry(QtCore.QRect(10, 410, 201, 191))
        self.subf3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"")
        self.subf3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subf3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subf3.setObjectName("subf3")
        self.subf3_btn = QtWidgets.QPushButton(self.subf3)
        self.subf3_btn.setGeometry(QtCore.QRect(10, 20, 180, 90))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.subf3_btn.setFont(font)
        self.subf3_btn.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.subf3_btn.setObjectName("subf3_btn")
        self.subf3_label = QtWidgets.QLabel(self.subf3)
        self.subf3_label.setGeometry(QtCore.QRect(10, 130, 180, 40))
        self.subf3_label.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);")
        self.subf3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subf3_label.setObjectName("subf3_label")
        self.frame2 = QtWidgets.QFrame(MainForm)
        self.frame2.setGeometry(QtCore.QRect(10, 10, 220, 40))
        self.frame2.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.TopLabel = QtWidgets.QLabel(MainForm)
        self.TopLabel.setGeometry(QtCore.QRect(240, 10, 961, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TopLabel.setFont(font)
        self.TopLabel.setStyleSheet("background-color: rgb(225, 224, 224);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);")
        self.TopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TopLabel.setObjectName("TopLabel")
        self.stackedWidget = QtWidgets.QStackedWidget(MainForm)
        self.stackedWidget.setGeometry(QtCore.QRect(240, 60, 961, 610))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 961, 610))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 959, 608))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 961, 610))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 959, 608))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setGeometry(QtCore.QRect(340, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 0, 960, 610))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 958, 608))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.dial = QtWidgets.QDial(self.scrollAreaWidgetContents_3)
        self.dial.setGeometry(QtCore.QRect(300, 190, 311, 211))
        self.dial.setObjectName("dial")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.subf1_btn.setText(_translate("MainForm", "STRATEGY SELECTION"))
        self.subf1_label.setText(_translate("MainForm", "TextLabel"))
        self.subf2_btn.setText(_translate("MainForm", "DIAGNOSIS"))
        self.subf2_label.setText(_translate("MainForm", "TextLabel"))
        self.subf3_btn.setText(_translate("MainForm", "CONTROL"))
        self.subf3_label.setText(_translate("MainForm", "TextLabel"))
        self.TopLabel.setText(_translate("MainForm", "TextLabel"))
        self.pushButton.setText(_translate("MainForm", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

