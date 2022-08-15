import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class OutWidget(QWidget):
    def __init__(self):
        super(OutWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # TODO
        self.resize(200, 50)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(53, 55, 100)}"
                                      "QPushButton{color: rgb(255, 255, 255)}"
                                      "QPushButton{border-radius:15px}"
                                      "QPushButton:hover{background-color:rgb(79, 82, 149)}"
                                      "QPushButton:pressed{background-color:rgb(79, 82, 149)}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "退出登录"))


import src.images.AccountManagement_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OutWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())
