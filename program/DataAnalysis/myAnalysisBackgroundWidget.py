import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class myCardsWidget(QWidget):
    def __init__(self):
        super(myCardsWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # TODO
        self.setObjectName("Form")
        self.resize(1060, 720)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1060, 720))
        self.widget.setStyleSheet("background-color: rgb(250, 236, 227);")
        self.widget.setObjectName("widget")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 70, 1060, 570))
        self.graphicsView.setStyleSheet("background-image: url(:/DataAnalysis_background.png);")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")


        # self.setStyleSheet("background-image: url(:/cardbackground.jpg);")
        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))

import DataAnalysis_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myCardsWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())