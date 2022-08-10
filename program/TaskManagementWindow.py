import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from program.SearchWidget import mySearchWidget
from PageWidget import PageWidget
from program.TaskManagement.myAddAndDeteleWidget import myAddAndDeleteWidget


class TaskManagementWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(TaskManagementWindow, self).__init__(*args, **kwargs)
        self.resize(1060, 720)
        self.setStyleSheet("background-color:rgb(235, 251, 232)")
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(0, 90, 1060, 570))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("background-image: url(:/TaskManagement_cardBackground.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.baseLayout = QtWidgets.QGridLayout(self, spacing=0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)

        self.deleteMode = False

        self.setupUi()

    def setupUi(self):
        # 左上方搜索栏
        self.SearchWidget = mySearchWidget()

        # 右上方添加删除栏
        self.AddAndDeleteWidget = myAddAndDeleteWidget()

        self.layout1_widget = QtWidgets.QWidget(self)
        self.layout1 = QGridLayout(self.layout1_widget, spacing=0)
        self.layout1.addWidget(self.SearchWidget, 0, 0, 1, 3)
        self.layout1.addWidget(self.AddAndDeleteWidget, 0, 4)
        # self.layout1_widget.raise_()
        self.baseLayout.addWidget(self.layout1_widget, 0, 0)

        # 页面加导航栏
        self.PageWidget = PageWidget()
        self.layout2_widget = QtWidgets.QWidget(self)
        self.layout2_widget.setStyleSheet("background-color:rgb(0,0,0,0)")
        self.layout2 = QGridLayout(self.layout2_widget, spacing=0)
        self.layout2.addWidget(self.PageWidget)
        self.baseLayout.addWidget(self.layout2_widget, 1, 0, 8, 1)

        self.SearchWidget.searchButton.clicked.connect(self.searchTask)
        self.SearchWidget.searchButton.clicked.connect(self.exitDeleteMode)
        self.SearchWidget.searchButton.clicked.connect(self.PageWidget.exitDeleteMode)
        self.AddAndDeleteWidget.pushButton_2.clicked.connect(self.changeDeleteMode)
        self.AddAndDeleteWidget.pushButton_2.clicked.connect(self.PageWidget.changeDeleteMode)

        #self.AddAndDeleteWidget.pushButton.clicked.connect(self.exitDeleteMode)

        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # self.pushButton.setText(_translate("MainWindow", "添加任务"))
        # self.pushButton_2.setText(_translate("MainWindow", "删除任务"))

    def changeDeleteMode(self):
        if self.deleteMode is True:
            for f in self.PageWidget.TaskCardList:
                f.deleteMode = False
                f.pushButton_2.setVisible(False)
            self.deleteMode = False
            self.AddAndDeleteWidget.pushButton_2.setText("退出删除")
        else:
            for f in self.PageWidget.TaskCardList:
                f.deleteMode = True
                f.pushButton_2.setVisible(True)
            self.deleteMode = True
            self.AddAndDeleteWidget.pushButton_2.setText("删除任务")

    def exitDeleteMode(self):
        for f in self.PageWidget.TaskCardList:
            f.deleteMode = False
        self.deleteMode = 0
        self.AddAndDeleteWidget.pushButton_2.setText("删除任务")

    def searchTask(self):
        feature_dict = self.SearchWidget.getFeatureDict()
        from TaskInterface import taskInterface
        taskInterface.switch7.emit(feature_dict)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TaskManagementWindow()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())
