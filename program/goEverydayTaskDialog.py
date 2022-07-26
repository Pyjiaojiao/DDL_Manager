# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication


class goEverydayTaskDialog(QtWidgets.QWidget):
    def __init__(self):
        super(goEverydayTaskDialog, self).__init__()
        self.date = QtCore.QDate()
        self.resize(300, 120)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setupUi()
        self.setWindowTitle("Query")

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 300, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label.setStyleSheet(("background-color: rgb(255, 255, 255);\n"
                                  "color: rgb(47, 75, 51);\n"
                                  "border-radius:6px;\n"
                                  "border:2px solid rgb(47, 75, 51)"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)

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
        self.pushButton_2.setObjectName("确定")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setGeometry(10, 150, 100, 30)
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
        self.pushButton.setObjectName("取消")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_2.clicked.connect(self.goInputDayTask)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.close)

        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
        self.pushButton.setText(_translate("MainWindow", "取消"))

    def updateText(self, date):
        dateStr = date.toString("yyyy-MM-dd")
        self.date = date
        self.label.setText("确定查看" + dateStr + "的任务吗？")

    def goInputDayTask(self):
        from TaskInterface import taskInterface
        taskInterface.switch5.emit(self.date)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = goEverydayTaskDialog()
    w.show()
    sys.exit(app.exec_())
