import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QTime, QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication
from DataAnalysis import myAnalysisPage1Widget, myAnalysisPage2Widget, myAnalysisPage3Widget, myAnalysisPage4Widget


class DataPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super(DataPageWidget, self).__init__()
        self.resize(1060, 720)

        # 页面
        self.cardWidget = QtWidgets.QWidget(self)
        self.cardWidget.setGeometry(QtCore.QRect(0, 0, 1040, 570))

        self.baseLayout = QtWidgets.QVBoxLayout(self, spacing=0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QtWidgets.QStackedWidget(self.cardWidget)
        self.baseLayout.addWidget(self.stackedWidget)

        self.PageNum = 4
        self.curPage = QtWidgets.QLabel("1")
        self.curPageNum = 1

        self.setupUi()

    def setupUi(self):
        # 第一页
        self.page1widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QHBoxLayout(self.page1widget, spacing=0)
        self.page1 = myAnalysisPage1Widget.myCardsWidget()
        layout.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page1widget)
        # 第二页
        self.page2widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QHBoxLayout(self.page2widget, spacing=0)
        self.page2 = myAnalysisPage2Widget.myCardsWidget()
        layout.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page2widget)
        # 第三页
        self.page3widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QHBoxLayout(self.page3widget, spacing=0)
        self.page3 = myAnalysisPage3Widget.myCardsWidget()
        layout.addWidget(self.page3)
        self.stackedWidget.addWidget(self.page3widget)
        # 第四页
        self.page4widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QHBoxLayout(self.page4widget, spacing=0)
        self.page4 = myAnalysisPage4Widget.myCardsWidget()
        layout.addWidget(self.page4)
        self.stackedWidget.addWidget(self.page4widget)
        # 底部切页
        self.frame_3 = QtWidgets.QFrame(self)
        self.baseLayout.addWidget(self.frame_3)
        self.frame_3.setGeometry(QtCore.QRect(120, 560, 800, 60))

        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        # self.frame_3.setSizePolicy(sizePolicy)

        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.frame_3.raise_()

        control_layout = QtWidgets.QHBoxLayout(self.frame_3)

        self.prePage = QtWidgets.QPushButton("<上一页")
        self.prePage.setFixedSize(90, 30)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.prePage.setFont(font)
        self.prePage.setStyleSheet("border-width: 1px;\n"
                                   "border-style: solid;\n"
                                   "border-color: rgb(64, 64, 64);\n"
                                   "border-radius:10px")
        self.prePage.setObjectName("prePage")

        self.nextPage = QtWidgets.QPushButton("下一页>")
        self.nextPage.setFixedSize(90, 30)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.nextPage.setFont(font)
        self.nextPage.setStyleSheet("border-width: 1px;\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(64, 64, 64);\n"
                                    "border-radius:10px")
        self.nextPage.setObjectName("prePage")
        self.totalPage = QtWidgets.QLabel("共 " + str(self.PageNum) + " 页")
        self.totalPage.setFont(font)

        skipLabel_0 = QtWidgets.QLabel("跳到")
        skipLabel_0.setFont(font)
        self.skipPage = QtWidgets.QLineEdit()
        self.skipPage.setPlaceholderText("请输入跳转的页码")
        self.skipPage.setFont(font)
        self.skipPage.setValidator(QIntValidator())  # 设置只能输入int类型数据
        self.skipPage.setStyleSheet("background-color:rgb(238, 238, 238)")
        skipLabel_1 = QtWidgets.QLabel("页")
        skipLabel_1.setFont(font)

        self.confirmSkip = QtWidgets.QPushButton("")
        self.confirmSkip.setFixedSize(32, 32)
        self.confirmSkip.setStyleSheet("background-image: url(:/PageTurn_next.png);border-radius: 5px")
        self.confirmSkip.setText("")
        self.confirmSkip.setObjectName("confirmSkip")

        control_layout.addStretch(1)
        control_layout.addWidget(self.prePage)
        control_layout.addWidget(self.curPage)
        control_layout.addWidget(self.nextPage)
        control_layout.addWidget(self.totalPage)
        control_layout.addWidget(skipLabel_0)
        control_layout.addWidget(self.skipPage)
        control_layout.addWidget(skipLabel_1)
        control_layout.addWidget(self.confirmSkip)
        control_layout.addStretch(1)

        self.frame_3.setLayout(control_layout)
        self.frame_3.raise_()
        self.prePage.clicked.connect(self.button_clicked)  # 上一页点击
        self.nextPage.clicked.connect(self.button_clicked)  # 下一页点击
        self.confirmSkip.clicked.connect(self.button_clicked)  # 确认键

        return

    def retranslate(self):
        return

    def updateDateAnalysis(self, chart_dict):
        self.page1.updateThreeCount(chart_dict['curTaskCount'],
                                    chart_dict['curFinishTaskCount'], chart_dict['curTaskFinishRate'])
        self.page1.updateStatusPieChart(chart_dict['taskStatusList'])
        self.page1.updateTypePieChart(chart_dict['taskTypeList'])
        self.page2.updateImportanceBarChart(chart_dict['taskImportanceList'])
        self.page2.updateTimeEstimatedBarChart(chart_dict['timeEstimatedList'])
        self.page3.updateTimeDistributeBarChart(chart_dict['taskTimeDistributeInOneDay'])
        self.page4.updateTimeFinishRateBarChart(chart_dict['taskFinishRateInOneDay'])
        # TODO 重新设置每一个bar图的series，不用重新setupUi

    def button_clicked(self):
        button_text = self.sender().text()
        total_page = int(self.totalPage.text().split()[1])  # 总页数
        current_page = int(self.curPage.text())

        if "<上一页" == button_text:
            self.skipPage.setText('')

            current_page = current_page - 1
            if current_page <= 1:
                self.curPage.setText("1")

            else:
                self.curPage.setText(str(current_page))

        if "下一页>" == button_text:
            self.skipPage.setText('')
            current_page = current_page + 1
            if current_page <= total_page:
                self.curPage.setText(str(current_page))

        if "" == button_text:
            if '' == self.skipPage.text():
                return

            page = int(self.skipPage.text())
            if 1 <= page <= total_page:
                self.curPage.setText(str(page))
            if page > total_page:
                self.curPage.setText(str(total_page))
                self.skipPage.setText(str(total_page))

            if page <= 0:
                self.curPage.setText(str(1))
                self.skipPage.setText(str(1))

        self.stackedWidget.setCurrentIndex(int(self.curPage.text()) - 1)

    @property
    def PAGE(self):
        return int(self.totalPage.text().split()[1])

    @PAGE.setter
    def PAGE(self, page: int):
        if page < 0:
            return
        self.totalPage.setText("共" + str(page) + "页")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataPageWidget()
    w.show()
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
    chart_dict1 = {
        'startDate': QDate(1970, 1, 1),  # QDateTime
        'endDate': QDate(2050, 1, 1),  # QDateTime 指定查询的开始和截止日期（只考虑日期，不计小时分钟）
        # 以下字段均针对“所有时间”
        'totalOriginTaskCount': 0,
        'totalTaskCount': 0,
        'totalTaskFinishRate': 0,
        # 以下字段均针对“指定的startDate和endDate之间”
        'curOriginTaskCount': 20,
        'curTaskCount': 30,
        'curFinishTaskCount': 20,
        'curTaskFinishRate': 0.5,
        'timeEstimatedList': [(2, 1), (4, 7), (6, 4), (8, 4)],
        'taskTypeList': [("学习", 4), ("运动", 5), ("娱乐", 16), ("工作", 3), ("其他", 4)],
        'taskStatusList': [(0, 3), (1, 4), (2, 5), (3, 1)],
        'taskImportanceList': [(0, 6), (1, 3), (2, 4), (3, 1)],
        'taskFinishmentList': [],
        'taskTimeDistributeInOneDay': [(3, 0), (6, 3), (9, 9), (12, 4), (15, 5), (18, 7), (21, 8), (24, 3)]
        ,
        'taskFinishRateInOneDay': [(3, 0.8), (6, .3), (9, .62), (12, .4), (15, .5), (18, .7), (21, .8), (24, .3)]

    }
    w.updateDateAnalysis(chart_dict)
    w.updateDateAnalysis(chart_dict1)
    sys.exit(app.exec_())

import src.images.PageTurn_rc