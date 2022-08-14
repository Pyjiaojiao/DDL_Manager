import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QGridLayout
from program.EverydayTask.myDateWidget import myDateWidget
from TaskInterface import taskInterface

from program.SearchWidget import mySearchWidget
from PageWidget import PageWidget


class EveryDayTaskWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(EveryDayTaskWindow, self).__init__(*args, **kwargs)
        self.resize(1060, 720)
        self.setStyleSheet("background-color:rgb(239, 231, 254)")

        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(0, 90, 1060, 570))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("background-image: url(:/EverydayTask_cardBackground.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.baseLayout = QtWidgets.QGridLayout(self, spacing=0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)

        self.date = QtCore.QDate.currentDate()
        self.feature_dict = {}

        self.bootTag = 0
        self.setupUi()

    def setupUi(self):
        # 顶部搜索栏
        self.SearchWidget = mySearchWidget()

        self.DateWidget = myDateWidget()

        self.layout1_widget = QtWidgets.QWidget(self)
        self.layout1 = QGridLayout(self.layout1_widget, spacing=0)
        self.layout1.addWidget(self.SearchWidget, 0, 0, 1, 3)
        self.layout1.addWidget(self.DateWidget, 0, 4)
        # self.layout1_widget.raise_()
        self.baseLayout.addWidget(self.layout1_widget, 0, 0)

        # self.setLayout(self.baseLayout)
        # 中部页面
        self.PageWidget = PageWidget()
        self.layout2_widget = QtWidgets.QWidget(self)
        self.layout2_widget.setStyleSheet("background-color:rgb(0,0,0,0)")
        self.layout2 = QGridLayout(self.layout2_widget, spacing=0)
        self.layout2.addWidget(self.PageWidget)
        for f in self.PageWidget.TaskCardList:
            f.pushButton_2.setVisible(True)
            f.taskDetailWidget.setVisible(False)
            f.pageMode = 1
        self.baseLayout.addWidget(self.layout2_widget, 1, 0, 8, 1)

        self.SearchWidget.searchButton.clicked.connect(self.searchTaskFromDate)

        if self.bootTag == 0:
            self.searchTaskFromDate()
            self.updateDate(self.date)
            self.bootTag = 1

        self.retranslateUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

    def searchTaskFromDate(self):
        self.feature_dict = self.SearchWidget.getFeatureDict()

        taskInterface.switch9.emit(self.date, self.feature_dict)
        print(self.feature_dict)

    def updateDate(self, date):  # date:Qtcore.QDate()
        self.date = date
        self.DateWidget.label.setText(date.toString("yyyy/MM/dd"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EveryDayTaskWindow()
    w.show()
    sys.exit(app.exec_())

import src.images.EverydayTask_rc
