# 예제 내용
# * QLabel 과 QPushButton 사용하여 윈도우 생성
# 참조: 파이썬으로 배우는 알고리즘 트레이딩 (https://wikidocs.net/5231)

# QLabel 위젯: 텍스트나 이미지를 출력하는데 사용함.

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):                                  # setUI 메서드라고 불리움.
        self.setGeometry(800, 400, 300, 150)            # 윈도우 사이즈 지정

        textLabel = QLabel("Message: ", self)           # QLabel 객체 사용/ textLabel 변수로 바인딩
        textLabel.move(20, 20)

        self.label = QLabel("", self)                   # QLabel 객체 사용/ self.label 변수로 바인딩
        self.label.move(80, 20)                         # move 메서드 사용/ QLabel 객체가 생성되는 위치 조정
        self.label.resize(150, 30)                      # resize 메서드 사용/ 크기 조정

        btn1 = QPushButton("Click", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)         # clicked 시그널 사용/ self.btn1_clicked 메서드와 연결

        btn2 = QPushButton("Clear", self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)         # clicked 시그널 사용/ self.btn2_clicked 메서드와 연결

    def btn1_clicked(self):
        self.label.setText("버튼이 클릭되었습니다.")

    def btn2_clicked(self):
        self.label.clear()                              # clear 메서드 사용/ 문자 지움


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()