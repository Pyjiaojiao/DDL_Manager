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
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(160, 430, 250, 120))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                    "border-radius:10px")
        self.textEdit.setObjectName("textEdit")
        # 账号
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_5.setText("5")
        self.label_5.setObjectName("label_5")
        # 昵称
        self.label_7 = QtWidgets.QLineEdit(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 210, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_7.setText("7")
        self.label_7.setObjectName("label_7")
        # 地区
        self.label_8 = QtWidgets.QLineEdit(self.widget)
        self.label_8.setGeometry(QtCore.QRect(160, 350, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_8.setText("8")
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
        # 性别
        self.label_9 = QtWidgets.QLineEdit(self.widget)
        self.label_9.setGeometry(QtCore.QRect(160, 280, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:10px\n"
                                   "")
        self.label_9.setText("9")
        self.label_9.setObjectName("label_9")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover{background-color: rgb(0, 0, 0)}"
                                      "QPushButton:hover{color: rgb(255, 255, 255)}"
                                      "QPushButton:hover{border-radius:10px}"
                                      "QPushButton:pressed{background-color: rgb(0, 0, 0)}"
                                      "QPushButton:pressed{color: rgb(255, 255, 255)}"
                                      "QPushButton:pressed{border-radius:10px}"
                                      "QPushButton{background-color: rgb(255, 255, 255)}"
                                      "QPushButton{color: rgb(0, 0, 0)}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{border:2px solid rgb(0, 0, 0)}")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.editInformation)

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

    def updateInformation(self, usr_id, usr_dict):
        self.label_5.setText(usr_id)
        self.label_7.setText(usr_dict['nickname'])
        self.label_9.setText(usr_dict['gender'])
        self.label_8.setText(usr_dict['region'])
        self.textEdit.setText(usr_dict['signature'])
        return

    def editInformation(self):
        nickname = self.label_7.text()
        gender = self.label_9.text()
        region = self.label_8.text()
        signature = self.textEdit.toPlainText()
        usr_dict = {'nickname': nickname,
                    'gender': gender,
                    'region': region,
                    'signature': signature}
        from TaskInterface import taskInterface
        taskInterface.switch21.emit(usr_dict)


import src.images.AccountManagement_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BasicInformationWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())
