import sys
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QFrame
from PySide2.QtGui import QPainter, QLinearGradient, QPainterPath
from PySide2.QtGui import Qt, QPen, QPolygonF, QBrush, QPolygon
from PySide2.QtCore import QPoint, QRect


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

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))
        points = [QPoint(100, 0),
                  QPoint(0, 50),
                  QPoint(100, 100),
                  QPoint(200, 50)]
        poly = QPolygon(points)
        painter.drawPolygon(poly)
        # painter.drawText(QRect(0,0, 100,50), Qt.AlignCenter, self.text)



app = QApplication(sys.argv)
win_main = btn_frame()
win_main.show()
sys.exit(app.exec_())