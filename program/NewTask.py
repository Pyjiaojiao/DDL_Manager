import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication


class NewTaskDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super(NewTaskDialog, self).__init__(*args, **kwargs)
        self.resize(500, 720)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 30, 500, 650))
        self.widget = QtWidgets.QWidget(self.frame)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label = QtWidgets.QLabel(self.widget)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.timeEdit = QtWidgets.QTimeEdit(self.widget)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.initUi()

    def initUi(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 650))
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                  "border-radius:20px")
        self.widget.setObjectName("widget")





        self.pushButton.setGeometry(QtCore.QRect(80, 580, 115, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        #         self.pushButton.setStyleSheet("background-color:rgb(56, 56, 56);\n"
        # "color: rgb(255, 255, 255);\n"
        # "border-radius:5px")

        self.pushButton.setStyleSheet(
            "QPushButton{background-color:rgb(56, 56, 56)}"
            "QPushButton{color: rgb(255, 255, 255)}"
            "QPushButton:hover{background-color:rgb(75, 75, 75)}"
            "QPushButton:pressed{background-color:rgb(75, 75, 75)}"
        )

        self.pushButton.setObjectName("pushButton")

        self.pushButton_2.setGeometry(QtCore.QRect(310, 580, 115, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        #         self.pushButton_2.setStyleSheet("background-color: rgb(56, 56, 56);\n"
        # "color: rgb(255, 255, 255);\n"
        # "border-radius:5px")

        self.pushButton_2.setStyleSheet(
            "QPushButton{background-color:rgb(56, 56, 56)}"
            "QPushButton{color: rgb(255, 255, 255)}"
            "QPushButton:hover{background-color:rgb(75, 75, 75)}"
            "QPushButton:pressed{background-color:rgb(75, 75, 75)}"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        # lineEdit：任务名称
        self.lineEdit.setGeometry(QtCore.QRect(160, 75, 300, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px;\n"
                                    "color:rgba(255, 255, 255，200)")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.checkBox.setGeometry(QtCore.QRect(70, 130, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        # timeEdit:预期用时(Hour)
        self.label_9.setGeometry(QtCore.QRect(230, 130, 100, 40))
        self.label_9.setFont(font)
        self.timeEdit.setGeometry(QtCore.QRect(330, 130, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(False)
        font.setWeight(50)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px;\n"
                                    "color:rgba(255, 255, 255，200)")
        self.timeEdit.setTime(QtCore.QTime(0, 0))
        self.timeEdit.setObjectName("lineEdit_2")
        # dateEdit:开始时间(startTime)
        self.dateEdit.setGeometry(QtCore.QRect(230, 190, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setWeight(75)
        font.setBold(False)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                        "border-radius:5px\n"
                                        "")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())


        self.label.setGeometry(QtCore.QRect(70, 190, 150, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2.setGeometry(QtCore.QRect(70, 250, 150, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.dateEdit_2.setGeometry(QtCore.QRect(230, 250, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                          "border-radius:5px")
        self.dateEdit_2.setCalendarPopup(True)
        font.setBold(False)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())

        self.comboBox.setGeometry(QtCore.QRect(230, 310, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_3.setGeometry(QtCore.QRect(70, 310, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(190, 10, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5.setGeometry(QtCore.QRect(70, 370, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox_2.setGeometry(QtCore.QRect(230, 370, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                      "border-radius:5px")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label_6.setGeometry(QtCore.QRect(70, 430, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.comboBox_3.setGeometry(QtCore.QRect(230, 430, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                      "border-radius:5px")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.textEdit.setGeometry(QtCore.QRect(160, 490, 300, 75))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px;\n"
                                    "color:rgba(255, 255, 255，200)")
        self.textEdit.setLineWidth(1)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setObjectName("textEdit")

        self.label_7.setGeometry(QtCore.QRect(70, 500, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8.setGeometry(QtCore.QRect(70, 80, 81, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")



        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.checkBox.setText(_translate("MainWindow", "是否为日常任务"))
        self.label.setText(_translate("MainWindow", "选择开始时间"))
        self.label_2.setText(_translate("MainWindow", "选择结束时间"))
        self.label_9.setText(_translate("MainWindow", "预期用时"))
        self.comboBox.setCurrentText(_translate("MainWindow", "学习"))
        self.comboBox.setItemText(0, _translate("MainWindow", "学习"))
        self.comboBox.setItemText(1, _translate("MainWindow", "运动"))
        self.comboBox.setItemText(2, _translate("MainWindow", "娱乐"))
        self.comboBox.setItemText(3, _translate("MainWindow", "工作"))
        self.comboBox.setItemText(4, _translate("MainWindow", "其他"))
        self.label_3.setText(_translate("MainWindow", "选择任务类型"))
        self.label_4.setText(_translate("MainWindow", "New Task"))
        self.label_5.setText(_translate("MainWindow", "重要性"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "非常重要"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "重要"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "一般"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "不重要"))
        self.label_6.setText(_translate("MainWindow", "选择任务状态"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "未开始"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "正在进行中"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "已完成"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "已过期"))
        self.label_7.setText(_translate("MainWindow", "详细描述"))
        self.label_8.setText(_translate("MainWindow", "任务名称"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NewTaskDialog()
    w.show()
    sys.exit(app.exec_())
