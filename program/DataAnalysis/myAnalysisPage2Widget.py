import sys

from PyQt5.QtChart import QChart
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Chart import barChart


class myCardsWidget(QWidget):
    def __init__(self):
        super(myCardsWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1060, 720)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1060, 720))
        self.widget.setStyleSheet("background-color: rgba(250, 236, 227,0);")
        self.widget.setObjectName("widget")
        # 任务预期时长分布图
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(0, 20, 490, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("\n"
                                    "border-radius:20px;\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.widget_6.setObjectName("widget_6")
        self.taskTimeEstimatedBarChart = barChart.ChartView()
        layout = QtWidgets.QHBoxLayout(self.widget_6, spacing=0)
        layout.addWidget(self.taskTimeEstimatedBarChart)
        # 任务重要性分布图
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(515, 20, 490, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet("\n"
                                    "border-radius:20px;\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.widget_7.setObjectName("widget_7")
        self.taskImportanceBarChart = barChart.ChartView()
        self.taskImportanceBarChart.setTheme(QChart.ChartThemeQt)
        layout = QtWidgets.QHBoxLayout(self.widget_7, spacing=0)
        layout.addWidget(self.taskImportanceBarChart)

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))

    def updateTimeEstimatedBarChart(self, chart_list):
        self.taskTimeEstimatedBarChart.initChart('timeEstimatedList', chart_list)

    def updateImportanceBarChart(self, chart_list):
        self.taskImportanceBarChart.initChart('taskImportanceList', chart_list)


import DataAnalysis_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myCardsWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    w.updateTimeEstimatedBarChart([(2, 1), (4, 7), (6, 3), (8, 4)])
    w.updateImportanceBarChart([(0, 6), (1, 3), (2, 4), (3, 1)])
    sys.exit(app.exec_())
