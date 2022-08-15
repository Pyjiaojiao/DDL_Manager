import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QDateTime, QDate, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from TaskDetailWidget import myTaskDetailWidget
from TaskInterface import taskInterface


class myTaskCard(QtWidgets.QWidget):
    switch1 = QtCore.pyqtSignal()  # finish task:taskCard->taskManage
    switch2 = QtCore.pyqtSignal()  # finish date task:taskCard->everydayTask

    def __init__(self):
        super(myTaskCard, self).__init__()
        self.resize(346, 280)
        self.taskDict = {'name': None,
                         'isDaily': False,
                         'startTime': QDate(1970, 1, 1),
                         'endTime': QDate(1970, 1, 1),
                         'type': None,
                         'importance': 0,
                         'status': 0,
                         'detail': None}
        self.taskDetailWidget = myTaskDetailWidget()
        self.pageMode = 1  # 1: 每日任务 2:任务管理
        self.finishMode = 1  # 1: 未完成 2: 已完成
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

        self.checkBox = QtWidgets.QPushButton(self.widget)
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
        if self.finishMode == 1:
            self.checkBox.setText("是否完成")
            self.checkBox.setStyleSheet("QPushButton:hover{background-color: rgb(84, 55, 173)}"
                                        "QPushButton:hover{color: rgb(255, 255, 255)}"
                                        "QPushButton:hover{border-radius:10px}"
                                        "QPushButton:pressed{background-color: rgb(84, 55, 173)}"
                                        "QPushButton:pressed{color: rgb(255, 255, 255)}"
                                        "QPushButton:pressed{border-radius:10px}"
                                        "QPushButton{background-color: rgb(255, 255, 255)}"
                                        "QPushButton{color: rgb(84, 55, 173)}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{border:2px solid rgb(84, 55, 173)}")
        else:
            self.checkBox.setText("已完成")
            self.checkBox.setStyleSheet("QPushButton{color: rgb(47, 75, 51)}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{border:2px solid rgba(47, 75, 51)}")

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
        self.pushButton_2.setStyleSheet('''QPushButton {
                                        background-image: url(:/TaskCard_delete.png);
                                        border-radius:10px;
                                        color:rgb(255, 255, 255);
                                        font: 11pt \"Consolas\";}
                            
                                        ''')
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self)

        self.pushButton.clicked.connect(self.taskDetailWidget.show)
        self.pushButton_2.clicked.connect(self.deleteTask)
        self.taskDetailWidget.modifyButton.clicked.connect(self.rewriteTask)
        self.taskDetailWidget.modifyButton.clicked.connect(self.taskDetailWidget.close)
        self.checkBox.clicked.connect(self.finishTask)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "任务名称："))
        self.label_2.setText(_translate("MainWindow", "截止日期："))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))

    def updateTask(self, task_dict):
        if task_dict is None:
            self.frame.setVisible(False)
            self.taskDict = {}
        else:
            print(task_dict)
            self.frame.setVisible(True)
            self.taskDict = task_dict
            self.label_4.setText(self.taskDict['name'])
            self.label_6.setText(self.taskDict['endDate'].toString(QtCore.Qt.DefaultLocaleShortDate))
            print('status is ')
            print(self.taskDict['status'])
            if self.taskDict['status'] > 1:
                self.checkBox.setEnabled(False)
                self.checkBox.setText("已完成")
                self.checkBox.setStyleSheet("QPushButton{color: rgb(47, 75, 51)}"
                                            "QPushButton{border-radius:10px}"
                                            "QPushButton{border:2px solid rgba(47, 75, 51)}")
            self.progressBar.setProperty("value", self.calStatusDegree())
            # if self.pageMode == 1:
            self.taskDetailWidget.updateTask(task_dict)
            self.frame.setVisible(True)

    def calStatusDegree(self):
        abd = int(self.taskDict['time_abd'].toString("yyyyMMddhh"))
        est = int(self.taskDict['time_estimated'].toString("yyyyMMddhh"))
        return (abd - 1900010100) / (est - 1900010100) * 100

    def changeDeleteMode(self, bool):
        self.pushButton_2.setVisible(bool)

    def deleteTask(self):
        print("self.pageMode is " + str(self.pageMode))
        if self.pageMode == 1:
            print(self.taskDict)
            taskInterface.switch3_.emit(str(self.taskDict['name']), self.taskDict['startTime'])

        elif self.pageMode == 2:
            print("pre delete" + str(self.taskDict['name']))
            taskInterface.switch3.emit(str(self.taskDict['name']))
        return

    def rewriteTask(self):
        name = self.taskDetailWidget.label_9.text()
        isDaily = self.taskDetailWidget.label_14.isChecked()
        startTime = self.taskDetailWidget.label_10.dateTime()
        costTime = self.taskDetailWidget.timeEdit.time()
        endTime = self.taskDetailWidget.label_11.dateTime()
        taskType = self.taskDetailWidget.comboBox.currentText()
        importance = self.taskDetailWidget.comboBox_2.currentIndex()
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
        taskInterface.switch1.emit(shortTaskDict)  # 实际使用的
        # taskInterface.switch1.emit(taskDict)  # 用于测试的，将shortTaskDict转为完整的taskDict、再并入taskList传入页面重新加载，由后端完成
        return

    def checkEdit(self, task_dict):
        shortDict = {'name': task_dict['name']}
        for key in self.taskDict:
            if key in task_dict and self.taskDict[key] != task_dict[key]:
                # and key != 'endTime' and key != 'startTime':
                shortDict.update({key: task_dict[key]})
        return shortDict

    def finishTask(self):
        if self.finishMode == 1:
            self.taskDict['status'] = 2
            if self.pageMode == 1:
                date = QtCore.QDate.fromString(self.taskDict['startTime'].toString("yyyy/MM/dd"), "yyyy/MM/dd")
                self.checkBox.setEnabled(False)
                self.finishMode = 2
                self.checkBox.setText("已完成")
                self.checkBox.setStyleSheet("QPushButton{color: rgb(47, 75, 51)}"
                                            "QPushButton{border-radius:10px}"
                                            "QPushButton{border:2px solid rgba(47, 75, 51)}")
                taskInterface.switch17.emit(date, self.taskDict)  # everyDayTask
            elif self.pageMode == 2:
                self.checkBox.setEnabled(False)
                taskInterface.switch15.emit(self.taskDict)  # taskManage


import src.images.TaskCard_rc

if __name__ == "__main__":
    task2 = {'name': "task2",
             'isDaily': False,
             'startTime': QDateTime(1980, 1, 1, 0, 0),
             'endTime': QDateTime(1980, 1, 1, 0, 0),
             'costTime': QTime(0, 0),
             'type': None,
             'importance': 0,
             'status': 3,
             'detail': None}
    app = QApplication(sys.argv)
    w = myTaskCard()
    w.updateTask(task2)
    w.show()
    sys.exit(app.exec_())
