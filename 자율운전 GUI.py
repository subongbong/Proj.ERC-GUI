# Trial And Error!!

from Ver5 import *      # 2019-08-14

from make_flowchart import make_flowchart as mf

import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QStackedWidget
from PySide2.QtCore import QTimer, QRect, QLine, Qt
from PySide2.QtGui import QPainter, QPen, QColor
from Button import btn_frame

class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = Ui_MainForm()
        self.main_ui.setupUi(self)

        self.pen_color = Qt.black

        self.main_ui.subf1_btn.clicked.connect(lambda: self.load_stackWidget(0, 'STRATEGY SELECTION'))
        self.main_ui.subf2_btn.clicked.connect(lambda: self.load_stackWidget(1, 'DIAGNOSIS'))
        self.main_ui.subf3_btn.clicked.connect(lambda: self.load_stackWidget(2, 'CONTROL'))

        self.load_stackContents()

    def load_stackWidget(self, load_nub, title):
        self.main_ui.stackedWidget.setCurrentIndex(load_nub)
        self.main_ui.TopLabel.setText(title)

    def load_stackContents(self):
        for load_nub in range(0, 3):
            self.scrollArea_widget = self.main_ui.stackedWidget.widget(load_nub).children()[0].widget()
            if load_nub == 0:
                mf(self.scrollArea_widget)                              # mf(self.main_ui.scrollAreaWidgetContents)
            # if load_nub == 1:                                         # 추후, 각 기능의 인터페이스 구현
            #     self.test_push = QPushButton(self.scrollArea_widget)

    def mousePressEvent(self, e):
        print(e.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    app.exec_()
