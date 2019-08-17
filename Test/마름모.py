import sys
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QFrame
from PySide2.QtGui import QPainter, QLinearGradient, QPainterPath
from PySide2.QtGui import Qt, QPen, QPolygonF

class btn_frame(QPushButton):
    def __init__(self):
        super().__init__()
        self.title = "LaLaLa"
        self.x = 0
        self.y = 0
        self.w = 500
        self.h = 500
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.show()

    def paintEngine(self):
        myGradient = QLinearGradient()
        myPen = QPen()
        myPolygon = QPolygonF()

        myPath = QPainterPath()
        myPath.addPolygon(myPolygon)

        painter = QPainter()
        painter.setBrush(myGradient)
        painter.setPen(myPen)
        painter.drawPath(myPath)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = btn_frame()
    win_main.show()
    sys.exit(app.exec_())