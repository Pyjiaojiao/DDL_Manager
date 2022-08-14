import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class BasicInformationWidget(QWidget):
    def __init__(self):
        super(BasicInformationWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # TODO
        self.resize(450, 580)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 450, 580))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "border-radius:25px")

        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(80, 20, 100, 100))
        self.graphicsView.setStyleSheet("background-image: url(:/AccountManagement_head.png);")
        self.graphicsView.setObjectName("graphicsView")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 140, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 420, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 430, 250, 120))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                       "border-radius:10px")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 210, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(160, 350, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(50, 280, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(160, 280, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:2px solid rgb(0, 0, 0);\n"
                                      "border-radius:20px;\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "昵称"))
        self.label_3.setText(_translate("Form", "地区"))
        self.label_4.setText(_translate("Form", "个性签名"))
        self.label_6.setText(_translate("Form", "性别"))
        self.pushButton.setText(_translate("Form", "编辑资料"))

import src.images.AccountManagement_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BasicInformationWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())