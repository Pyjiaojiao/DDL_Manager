import sys
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
        self.widget.setStyleSheet("background-color: rgb(250, 236, 227,0);")
        self.widget.setObjectName("widget")

        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(10, 20, 1000, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("\n"
                                    "border-radius:20px;\n"
                                    "background-color: rgb(255, 255, 255, 170);")
        self.widget_6.setObjectName("widget_6")
        self.taskTimeDistributeBarChart = barChart.ChartView()
        layout = QtWidgets.QHBoxLayout(self.widget_6, spacing=0)
        layout.addWidget(self.taskTimeDistributeBarChart)

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))

    def updateTimeDistributeBarChart(self, chart_list):
        self.taskTimeDistributeBarChart.initChart('taskTimeDistributeInOneDay',
                                                  chart_list)


import DataAnalysis_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myCardsWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    w.updateTimeDistributeBarChart([(3, 0), (6, 3), (9, 12), (12, 4), (15, 5), (18, 7), (21, 8), (24, 3)])
    sys.exit(app.exec_())
