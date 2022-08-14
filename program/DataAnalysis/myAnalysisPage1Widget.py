import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate
from Chart import pieChart


class myCardsWidget(QWidget):
    def __init__(self):
        super(myCardsWidget, self).__init__()
        self.startDate = QDate(1970, 1, 1)
        self.endDate = QDate(2050, 1, 1)
        self.allDateMode = True
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1060, 720)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1060, 720))
        self.widget.setStyleSheet("background-color: rgb(250, 236, 227, 0);")
        self.widget.setObjectName("widget")

        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 10, 1010, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("\n"
                                    "border-radius:20px;\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 112, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius:5px;\n"
                                      "border:2px solid rgb(236, 179, 153)")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(190, 10, 130, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setMidLineWidth(5)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 130, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setMidLineWidth(5)
        self.label_2.setObjectName("label_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(660, 10, 170, 30))
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("border-radius:5px;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit_3.setGeometry(QtCore.QRect(340, 10, 170, 30))
        self.dateEdit_3.setDate(QtCore.QDate.currentDate())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_3.sizePolicy().hasHeightForWidth())
        self.dateEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setStyleSheet("border-radius:5px;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 10, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("background-image: url(:/DataAnalysis_search.png);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        # 任务总数
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 70, 321, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "border:2px solid rgb(250, 236, 227);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 120, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255)\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(110, 50, 141, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255)\n"
                                   "")
        self.label_6.setObjectName("label_6")
        # 任务完成数量
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(350, 69, 331, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "border:2px solid rgb(250, 236, 227);")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255)\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(140, 50, 141, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255)\n"
                                   "")
        self.label_7.setObjectName("label_7")
        # 任务完成率
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setGeometry(QtCore.QRect(700, 69, 301, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "border:2px solid rgb(250, 236, 227);")
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255)\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setGeometry(QtCore.QRect(150, 50, 141, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255)\n"
                                   "")
        self.label_8.setObjectName("label_8")
        # 任务状态分布
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(0, 230, 490, 380))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("\n"
                                    "border-radius:20px;\n"
                                    "background-color: rgba(255, 255, 255, 140);")
        self.widget_6.setObjectName("widget_6")
        self.statusPieChart = pieChart.ChartView()
        layout = QtWidgets.QHBoxLayout(self.widget_6, spacing=0)
        layout.addWidget(self.statusPieChart)
        # 任务类型分布
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(520, 230, 490, 380))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet("\n"
                                    "border-radius:20px;\n"
                                    "background-color: rgba(255, 255, 255, 140);")
        self.widget_7.setObjectName("widget_7")
        self.typePieChart = pieChart.ChartView()
        layout = QtWidgets.QHBoxLayout(self.widget_7, spacing=0)
        layout.addWidget(self.typePieChart)

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pushButton.clicked.connect(self.changeAllTimeMode)
        self.pushButton_2.clicked.connect(self.searchDataFromDate)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "全部"))
        self.label.setText(_translate("Form", "选择开始时间："))
        self.label_2.setText(_translate("Form", "选择结束时间："))
        self.label_3.setText(_translate("Form", "任务总数："))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "任务完成数量："))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "任务完成率："))
        self.label_8.setText(_translate("Form", "TextLabel"))

    def updateThreeCount(self, task_count, finish_count, finish_rate):
        self.label_6.setText(str(task_count))
        self.label_7.setText(str(finish_count))
        self.label_8.setText("%.1f%%" % (finish_rate * 100))

    def updateStatusPieChart(self, chart_list):
        self.statusPieChart.initChart('taskStatusList', chart_list)

    def updateTypePieChart(self, chart_list):
        self.typePieChart.initChart('taskTypeList', chart_list)

    def changeAllTimeMode(self):
        if self.allDateMode:
            self.pushButton.setStyleSheet("background-color: rgb(236, 179, 153);\n"
                                          "border-radius:5px;\n"
                                          "border:2px solid rgb(236, 179, 153)")
            self.allDateMode = False
        else:
            self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius:5px;\n"
                                          "border:2px solid rgb(236, 179, 153)")
            self.allDateMode = True

    def searchDataFromDate(self):
        from Chart.ChartInterface import chartInterface
        # TODO：信号- Date -> interface -> main -> dataAnalysisWindow -> 更新
        if self.allDateMode:
            self.startDate = QDate(1970, 1, 1)
            self.endDate = QDate(2050, 1, 1)
        else:
            self.startDate = self.dateEdit_2.date()
            self.endDate = self.dateEdit_3.date()
        chartInterface.switch1.emit({'startDate': self.startDate,
                                     'endDate': self.endDate})


import DataAnalysis_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myCardsWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    w.updateThreeCount(80, 40, 0.8)
    w.updateStatusPieChart([(0, 3), (1, 4), (2, 5), (3, 1)])
    w.updateTypePieChart([("学习", 4), ("运动", 5), ("娱乐", 6), ("工作", 3), ("其他", 4)])
    sys.exit(app.exec_())
