import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from TaskDetailWidget import myTaskDetailWidget
from TaskInterface import taskInterface


class myTaskCard(QtWidgets.QWidget):


    def __init__(self):
        super(myTaskCard, self).__init__()
        self.resize(346, 280)
        self.taskDict = {'name': None,
                         'isDaily': False,
                         'startTime': QDateTime(1970, 1, 1, 0, 0),
                         'endTime': QDateTime(1970, 1, 1, 0, 0),
                         'type': None,
                         'importance': 0,
                         'status': 0,
                         'detail': None}
        self.taskDetailWidget = myTaskDetailWidget()

        self.setupUi()

    def setupUi(self):
        self.baseLayout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.baseLayout)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(23, 5, 300, 270))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 300, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                  "border-radius:20px\n"
                                  "")
        self.widget.setObjectName("widget")

        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(170, 230, 105, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 50, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 50, 130, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:5px\n"
                                   "")
        self.label_4.setObjectName("label_4")

        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(30, 170, 250, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("selection-color: rgb(166, 200, 255);")
        self.progressBar.setProperty("value", 35)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(150, 110, 130, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                   "border-radius:5px\n"
                                   "")
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("background-image: url(:/TaskCard_more.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(:/TaskCard_delete.png);\n"
                                        "border-radius:10px;\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "font: 11pt \"Consolas\";\n"
                                        "\n"
                                        "")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self)

        self.pushButton.clicked.connect(self.taskDetailWidget.show)
        self.pushButton_2.clicked.connect(self.deleteTask)
        self.taskDetailWidget.modifyButton.clicked.connect(self.rewriteTask)
        self.taskDetailWidget.modifyButton.clicked.connect(self.taskDetailWidget.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "是否完成"))
        self.label.setText(_translate("MainWindow", "任务名称："))
        self.label_2.setText(_translate("MainWindow", "截止日期："))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))

    '''       taskDict = {'name': name,  # str
                    'isDaily': isDaily,  # boolean
                    'startTime': startTime,  # QDateTime
                    'endTime': endTime,  # QDateTime
                    'type': taskType,  # str
                    'importance': importance,  # int 从0开始数字越大越重要，最重要为3
                    'status': status,  # int 从0开始数字越大完成度越高，最高为3
                    'detail': detail}  # str
    '''

    def updateTask(self, task_dict):
        if task_dict is None:
            self.frame.setVisible(False)
            self.taskDict = {}
        else:
            self.frame.setVisible(True)
            self.taskDict = task_dict
            self.label_4.setText(self.taskDict['name'])
            self.label_6.setText(self.taskDict['endTime'].toString(QtCore.Qt.DefaultLocaleShortDate))
            self.checkBox.setChecked(self.taskDict['status'] > 1)
            self.progressBar.setProperty("value", self.taskDict['status'] * 25)
            self.taskDetailWidget.updateTask(task_dict)
            self.frame.setVisible(True)

    def changeDeleteMode(self, bool):
        self.pushButton_2.setVisible(bool)

    def deleteTask(self):
        taskInterface.switch3.emit(str(self.taskDict['name']))
        return

    def rewriteTask(self):
        name = self.taskDetailWidget.label_9.text()
        isDaily = self.taskDetailWidget.label_14.isChecked()
        startTime = QtCore.QDateTime.fromString(self.taskDetailWidget.label_10.text(), "yyyy-MM-dd hh:mm")
        costTime = self.taskDetailWidget.timeEdit.time()
        endTime = QtCore.QDateTime.fromString(self.taskDetailWidget.label_11.text(), "yyyy-MM-dd hh:mm")
        taskType = self.taskDetailWidget.label_12.text()
        importance = self.taskDetailWidget.label_13.text()
        status = int(self.progressBar.property("value")) / 33
        detail = self.taskDetailWidget.textBrowser.toPlainText()
        taskDict = {'name': name,  # str
                    'isDaily': isDaily,  # boolean
                    'startTime': startTime,  # QDateTime
                    'costTime': costTime,
                    'endTime': endTime,  # QDateTime
                    'type': taskType,  # str
                    'importance': importance,  # int 从0开始数字越大越重要，最重要为3
                    'status': status,  # int 从0开始数字越大完成度越高，最高为3
                    'detail': detail}  # str

        shortTaskDict = self.checkEdit(taskDict)
        # taskInterface.switch1.emit(shortTaskDict) # 实际使用的
        taskInterface.switch1.emit(taskDict)  # 用于测试的，将shortTaskDict转为完整的taskDict、再并入taskList传入页面重新加载，由后端完成
        return

    def checkEdit(self, task_dict):
        shortDict = {}
        for key in self.taskDict:
            if key in task_dict and self.taskDict[key] != task_dict[key]:
                shortDict.update({key: task_dict[key]})
        return shortDict


import src.images.TaskCard_rc

if __name__ == "__main__":
    task2 = {'name': "task2",
             'isDaily': False,
             'startTime': QDateTime(1980, 1, 1, 0, 0),
             'endTime': QDateTime(1980, 1, 1, 0, 0),
             'type': None,
             'importance': 0,
             'status': 3,
             'detail': None}
    app = QApplication(sys.argv)
    w = myTaskCard()
    w.updateTask(task2)
    w.show()
    sys.exit(app.exec_())
