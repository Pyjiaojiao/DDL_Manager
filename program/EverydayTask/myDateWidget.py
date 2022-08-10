import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class myDateWidget(QWidget):
    def __init__(self):
        super(myDateWidget, self).__init__()
        self.setupUi()

    def setupUi(self):

        self.resize(250, 60)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px")

        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(30, 15, 32, 32))
        self.graphicsView.setStyleSheet("background-image: url(:/EverydayTask_calendar.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 15, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "0000/00/00"))

import src.images.EverydayTask_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myDateWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())