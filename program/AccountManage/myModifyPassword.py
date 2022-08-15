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
        self.resize(500, 300)
        self.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "border-radius:15px\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 40, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 250, 40))
        self.lineEdit.setStyleSheet("\n"
                                    "background-color: rgb(238, 238, 238);\n"
                                    "border-radius:5px\n"
                                    "")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 250, 40))
        self.lineEdit_2.setStyleSheet("\n"
                                      "background-color: rgb(238, 238, 238);\n"
                                      "border-radius:5px\n"
                                      "")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 160, 250, 40))
        self.lineEdit_3.setStyleSheet("\n"
                                      "background-color: rgb(238, 238, 238);\n"
                                      "border-radius:5px\n"
                                      "")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 230, 115, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{background-color:rgb(56, 56, 56)}"
            "QPushButton{color: rgb(255, 255, 255)}"
            "QPushButton:hover{background-color:rgb(75, 75, 75)}"
            "QPushButton:pressed{background-color:rgb(75, 75, 75)}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 230, 115, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{background-color:rgb(56, 56, 56)}"
            "QPushButton{color: rgb(255, 255, 255)}"
            "QPushButton:hover{background-color:rgb(75, 75, 75)}"
            "QPushButton:pressed{background-color:rgb(75, 75, 75)}")
        self.pushButton_5.setObjectName("pushButton_5")



        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.pushButton_5.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "原密码："))
        self.label_2.setText(_translate("Form", "新密码："))
        self.label_3.setText(_translate("Form", "确认新密码："))
        self.pushButton_4.setText(_translate("Form", "登录"))
        self.pushButton_5.setText(_translate("Form", "取消"))


import src.images.AccountManagement_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myCardsWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())