import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class myAddAndDeleteWidget(QWidget):
    def __init__(self):
        super(myAddAndDeleteWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # TODO
        self.resize(250, 60)
        self.setStyleSheet("background-color:rgb(236, 249, 232);\n"
                           "border-radius:8px")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 15, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover{background-color: rgb(47, 75, 51)}"
                                      "QPushButton:hover{color: rgb(255, 255, 255)}"
                                      "QPushButton:hover{border-radius:10px}"
                                      "QPushButton:pressed{background-color: rgb(47, 75, 51)}"
                                      "QPushButton:pressed{color: rgb(255, 255, 255)}"
                                      "QPushButton:pressed{border-radius:10px}"
                                      "QPushButton{background-color: rgb(255, 255, 255)}"
                                      "QPushButton{color: rgb(47, 75, 51)}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{border:2px solid rgba(47, 75, 51)}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(135, 15, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton:hover{background-color: rgb(47, 75, 51)}"
                                        "QPushButton:hover{color: rgb(255, 255, 255)}"
                                        "QPushButton:hover{border-radius:10px}"
                                        "QPushButton:pressed{background-color: rgb(47, 75, 51)}"
                                        "QPushButton:pressed{color: rgb(255, 255, 255)}"
                                        "QPushButton:pressed{border-radius:10px}"
                                        "QPushButton{background-color: rgb(255, 255, 255)}"
                                        "QPushButton{color: rgb(47, 75, 51)}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{border:2px solid rgba(47, 75, 51)}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "添加任务"))
        self.pushButton_2.setText(_translate("Form", "删除任务"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myAddAndDeleteWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())
