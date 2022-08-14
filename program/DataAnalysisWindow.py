import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QGridLayout
from program.EverydayTask.myDateWidget import myDateWidget
from DataAnalysis import myAnalysisPage1Widget, myAnalysisPage2Widget, myAnalysisPage3Widget, myAnalysisPage4Widget, \
    myAnalysisBackgroundWidget
from DataAnalysis import DataPageWidget


class DataAnalysisWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(DataAnalysisWindow, self).__init__(*args, **kwargs)
        self.resize(1060, 720)
        # self.widget = QtWidgets.QWidget(self)
        self.setStyleSheet("background-color: rgb(250, 236, 227)")
        # self.widget.setGeometry(0,0,1060,570)

        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(0, 70, 1060, 570))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("background-image: url(:/DataAnalysis_background.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.raise_()
        self.baseLayout = QtWidgets.QGridLayout(self,spacing=0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)

        self.setupUi()

    def setupUi(self):
        layout_widget = QtWidgets.QWidget(self)
        layout_widget.setStyleSheet("background-color:rgba(0,0,0,0)")
        layout = QGridLayout(layout_widget,spacing=0)
        self.dataPageWidget = DataPageWidget.DataPageWidget()
        layout.addWidget(self.dataPageWidget)
        self.baseLayout.addWidget(layout_widget)
        QtCore.QMetaObject.connectSlotsByName(self)
        return

    def test(self):
        chart_dict = {
            'startDate': QDate(1970, 1, 1),  # QDateTime
            'endDate': QDate(2050, 1, 1),  # QDateTime 指定查询的开始和截止日期（只考虑日期，不计小时分钟）
            # 以下字段均针对“所有时间”
            'totalOriginTaskCount': 0,
            'totalTaskCount': 0,
            'totalTaskFinishRate': 0,
            # 以下字段均针对“指定的startDate和endDate之间”
            'curOriginTaskCount': 20,
            'curTaskCount': 40,
            'curFinishTaskCount': 20,
            'curTaskFinishRate': 0.5,
            'timeEstimatedList': [(2, 1), (4, 7), (6, 3), (8, 4)],
            'taskTypeList': [("学习", 4), ("运动", 5), ("娱乐", 6), ("工作", 3), ("其他", 4)],
            'taskStatusList': [(0, 3), (1, 4), (2, 5), (3, 1)],
            'taskImportanceList': [(0, 6), (1, 3), (2, 4), (3, 1)],
            'taskFinishmentList': [],
            'taskTimeDistributeInOneDay': [(3, 0), (6, 3), (9, 12), (12, 4), (15, 5), (18, 7), (21, 8), (24, 3)]
            ,
            'taskFinishRateInOneDay': [(3, 0.8), (6, .3), (9, .62), (12, .4), (15, .5), (18, .7), (21, .8), (24, .3)]

        }
        self.dataPageWidget.updateDateAnalysis(chart_dict)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataAnalysisWindow()
    w.show()
    w.test()
    sys.exit(app.exec_())

import src.images.DataAnalysis_rc
