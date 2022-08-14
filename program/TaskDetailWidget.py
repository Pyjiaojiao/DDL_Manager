import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.QtWidgets import QApplication


class myTaskDetailWidget(QtWidgets.QWidget):
    def __init__(self):
        super(myTaskDetailWidget, self).__init__()
        self.taskDict = {'name': None,
                         'isDaily': False,
                         'startTime': QDateTime(1970, 1, 1, 0, 0),
                         'endTime': QDateTime(1970, 1, 1, 0, 0),
                         'costTime': QTime(0, 0),
                         'type': None,
                         'importance': 0,
                         'status': 0,
                         'detail': None}
        self.resize(500, 650)
        self.setupUi()

    def setupUi(self):
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 650))
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                  "border-radius:20px")
        self.widget.setObjectName("widget")

        self.taskNameLabel = QtWidgets.QLabel(self.widget)
        self.taskNameLabel.setGeometry(QtCore.QRect(50, 70, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setObjectName("taskNameLabel")

        self.beginTimeLabel = QtWidgets.QLabel(self.widget)
        self.beginTimeLabel.setGeometry(QtCore.QRect(50, 130, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.beginTimeLabel.setFont(font)
        self.beginTimeLabel.setObjectName("beginTimeLabel")

        self.deadlineLabel = QtWidgets.QLabel(self.widget)
        self.deadlineLabel.setGeometry(QtCore.QRect(50, 190, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deadlineLabel.setFont(font)
        self.deadlineLabel.setObjectName("deadlineLabel")

        self.isDailyLabel = QtWidgets.QLabel(self.widget)
        self.isDailyLabel.setGeometry(QtCore.QRect(50, 250, 160, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.isDailyLabel.setFont(font)
        self.isDailyLabel.setObjectName("isDailyLabel")

        self.taskStateLabel = QtWidgets.QLabel(self.widget)
        self.taskStateLabel.setGeometry(QtCore.QRect(50, 430, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.taskStateLabel.setFont(font)
        self.taskStateLabel.setObjectName("taskStateLabel")

        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(180, 430, 281, 40))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFont(font)

        self.taskTypeLabel = QtWidgets.QLabel(self.widget)
        self.taskTypeLabel.setGeometry(QtCore.QRect(50, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.taskTypeLabel.setFont(font)
        self.taskTypeLabel.setObjectName("taskTypeLabel")

        self.significanceLabel = QtWidgets.QLabel(self.widget)
        self.significanceLabel.setGeometry(QtCore.QRect(50, 370, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.significanceLabel.setFont(font)
        self.significanceLabel.setObjectName("significanceLabel")

        self.detailLabel = QtWidgets.QLabel(self.widget)
        self.detailLabel.setGeometry(QtCore.QRect(50, 490, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.detailLabel.setFont(font)
        self.detailLabel.setObjectName("detailLabel")
        # textBrowser: 详情描述
        self.textBrowser = QtWidgets.QTextEdit(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 500, 300, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                       "border-radius:5px")
        self.textBrowser.setObjectName("textBrowser")

        # label_9:任务名称
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(170, 70, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                   "border-radius:5px\n"
                                   "")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        # label_10 开始时间
        self.label_10 = QtWidgets.QDateTimeEdit(self.widget)
        self.label_10.setGeometry(QtCore.QRect(170, 130, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px")
        self.label_10.setDateTime(QDateTime.currentDateTime())
        self.label_10.setCalendarPopup(True)
        self.label_10.setObjectName("label_10")
        # label_11：截止时间
        self.label_11 = QtWidgets.QDateTimeEdit(self.widget)
        self.label_11.setGeometry(QtCore.QRect(170, 190, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px")
        self.label_11.setDateTime(QDateTime.currentDateTime())
        self.label_11.setCalendarPopup(True)
        self.label_11.setObjectName("label_11")

        # label_12: 任务类型
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(180, 310, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px\n"
                                    "")
        # self.comboBox.setText("")
        self.comboBox.setObjectName("label_12")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # label_13:重要性
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 370, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        sfont = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                      "border-radius:5px")
        # self.comboBox_2.setText("")
        self.comboBox_2.setObjectName("label_13")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        # label_14:是否为日常任务
        self.label_14 = QtWidgets.QCheckBox(self.widget)
        self.label_14.setGeometry(QtCore.QRect(200, 250, 91, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.label_14.setFont(font)
        '''
        self.label_14.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px\n"
                                    "")'''
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")

        # timeEdit: 预期用时
        self.costTimeLabel = QtWidgets.QLabel(self.widget)
        self.costTimeLabel.setGeometry(QtCore.QRect(260, 250, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.costTimeLabel.setFont(font)
        self.costTimeLabel.setObjectName("detailLabel")
        self.timeEdit = QtWidgets.QTimeEdit(self.widget)
        self.timeEdit.setGeometry(QtCore.QRect(370, 250, 100, 30))
        self.timeEdit.setStyleSheet("background-color:rgb(238, 238, 238);\n"
                                    "border-radius:5px\n"
                                    "")
        font.setBold(False)
        self.timeEdit.setFont(font)

        ### 返回键
        self.returnButton = QtWidgets.QPushButton(self.widget)
        self.returnButton.setGeometry(QtCore.QRect(30, 10, 50, 50))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnButton.sizePolicy().hasHeightForWidth())
        self.returnButton.setSizePolicy(sizePolicy)
        self.returnButton.setStyleSheet("background-image: url(:/TaskDetail_back.png);")
        self.returnButton.setText("")
        self.returnButton.setObjectName("returnButton")

        ###修改键
        self.modifyButton = QtWidgets.QPushButton(self.widget)
        self.modifyButton.setGeometry(QtCore.QRect(420, 10, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyButton.sizePolicy().hasHeightForWidth())
        self.modifyButton.setSizePolicy(sizePolicy)
        self.modifyButton.setStyleSheet("background-image: url(:/TaskDetail_modify.png);")
        self.modifyButton.setText("")
        self.modifyButton.setObjectName("modifyButton")

        self.returnButton.clicked.connect(self.close)

        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.taskNameLabel.setText(_translate("MainWindow", "任务名称："))
        self.beginTimeLabel.setText(_translate("MainWindow", "起始时间："))
        self.deadlineLabel.setText(_translate("MainWindow", "截止时间："))
        self.isDailyLabel.setText(_translate("MainWindow", "是否为日常任务："))
        self.taskStateLabel.setText(_translate("MainWindow", "任务状态："))
        self.taskTypeLabel.setText(_translate("MainWindow", "任务类型："))
        self.significanceLabel.setText(_translate("MainWindow", "重要性："))
        self.detailLabel.setText(_translate("MainWindow", "详细描述："))
        self.costTimeLabel.setText(_translate("MainWindow", "预期用时："))
        self.comboBox.setItemText(0, _translate("MainWindow", "学习"))
        self.comboBox.setItemText(1, _translate("MainWindow", "运动"))
        self.comboBox.setItemText(2, _translate("MainWindow", "娱乐"))
        self.comboBox.setItemText(3, _translate("MainWindow", "工作"))
        self.comboBox.setItemText(4, _translate("MainWindow", "其他"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "非常重要"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "重要"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "一般"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "不重要"))

    def updateTask(self, task_dict):
        self.taskDict = task_dict
        self.label_9.setText(self.taskDict['name'])
        self.label_10.setDateTime(self.taskDict['startTime'])
        self.label_11.setDateTime(self.taskDict['endTime'])
        if self.taskDict.__contains__('costTime'):
            costTime = self.taskDict['costTime']
        else:
            costTime = QTime.fromString(self.taskDict['time_estimated'].toString("hh:mm"), "hh:mm")
        self.timeEdit.setTime(costTime)
        if self.taskDict['isDaily'] is True:
            self.label_14.setChecked(True)
        else:
            self.label_14.setChecked(False)
        self.label_14.setEnabled(False)
        typeList = ["学习", "运动", "娱乐", "工作", "其他"]
        self.comboBox.setCurrentIndex(typeList.index(self.taskDict['type']))
        self.comboBox_2.setCurrentIndex(self.taskDict['importance'])
        self.progressBar.setProperty("value", self.calStatusDegree())
        self.textBrowser.setText(self.taskDict['detail'])

    def calStatusDegree(self):
        abd = int(self.taskDict['time_abd'].toString("yyyyMMddhh"))
        est = int(self.taskDict['time_estimated'].toString("yyyyMMddhh"))
        return (abd - 1900010100) / (est - 1900010100) * 100

    def loadImportance(self, i):
        if i == 0:
            return "不重要"
        elif i == 1:
            return "一般"
        elif i == 2:
            return "重要"
        elif i == 3:
            return "非常重要"
        else:
            return "你问我？"

    def loadStatus(self, i):
        if i == 0:
            return "未开始"
        elif i == 1:
            return "正在进行中"
        elif i == 2:
            return "已完成"
        elif i == 3:
            return "已过期"
        else:
            return "你问我？"


import src.images.TaskDetail_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myTaskDetailWidget()
    w.show()
    sys.exit(app.exec_())
