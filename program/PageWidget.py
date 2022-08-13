import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QTime, QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication

from TaskCard import myTaskCard
from PageTurnWidget import myPageTurnWidget


class PageWidget(QtWidgets.QWidget):
    def __init__(self):
        super(PageWidget, self).__init__()
        self.resize(1040, 620)
        self.setStyleSheet("background-color:rgb(0,0,0,0)")
        # 当前任务列表
        task2 = {'name': "task2",
                 'isDaily': False,
                 'startTime': QDateTime(1980, 1, 1, 1, 1),
                 'endTime': QDateTime(1980, 1, 1, 1, 1),
                 'type': None,
                 'costTime': QTime(0, 0),
                 'importance': 0,
                 'status': 3,
                 'detail': None}
        self.TaskList = [task2, task2, task2, task2, task2, task2, task2, task2, task2, task2, task2, task2, task2,
                         task2, task2, task2, task2, task2, task2, task2]
        self.TaskList = []
        self.TaskCardList = []
        self.PageNum = (len(self.TaskList) - 1) // 6 + 1
        # 页面
        # self.resize(1280, 720)
        self.cardWidget = QtWidgets.QWidget(self)
        self.cardWidget.setGeometry(QtCore.QRect(0, 0, 1040, 570))

        self.baseLayout = QtWidgets.QVBoxLayout(self, spacing=0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QtWidgets.QStackedWidget(self.cardWidget)
        self.baseLayout.addWidget(self.stackedWidget)
        self.frame_3 = QtWidgets.QFrame(self)

        self.curPage = QtWidgets.QLabel("1")
        self.curPageNum = 1

        self.deleteMode = False
        self.setupUi()

    def setupUi(self):

        for i in range(self.PageNum):
            layoutWidget = QtWidgets.QWidget()
            layoutWidget.setFixedSize(1040, 560)
            layout = QtWidgets.QGridLayout(layoutWidget)
            layout.setContentsMargins(0, 0, 0, 0)
            start_index = i * 6
            end_index = start_index + 6

            if end_index > len(self.TaskList):
                end_index = len(self.TaskList)
            curTasks = self.TaskList[start_index:end_index]
            # print(curTasks)
            for j in range(len(curTasks)):
                f = myTaskCard()
                f.updateTask(curTasks[j])
                self.TaskCardList.append(f)
                f.changeDeleteMode(self.deleteMode)
                layout.addWidget(f, j // 3, j % 3)
            if len(curTasks) == 2:
                f = myTaskCard()
                f.setEnabled(False)
                op = QtWidgets.QGraphicsOpacityEffect()
                op.setOpacity(0)
                f.setGraphicsEffect(op)
                self.TaskCardList.append(f)
                layout.addWidget(f, 0, 2)
            # layoutWidget.raise_()
            self.stackedWidget.addWidget(layoutWidget)

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
        # self.prePage.clicked.connect(self.display)

    def retranslate(self):
        return

    def changeDeleteMode(self):
        if self.deleteMode is True:
            for f in self.TaskCardList:
                f.deleteMode = False
                f.pushButton_2.setVisible(False)
            self.deleteMode = False
        else:
            for f in self.TaskCardList:
                f.deleteMode = True
                f.pushButton_2.setVisible(True)
            self.deleteMode = True

    def exitDeleteMode(self):
        for f in self.TaskCardList:
            f.deleteMode = False
        self.deleteMode = False

    def updateTaskList(self, task_list):
        self.TaskList = task_list
        self.PageNum = (len(task_list) - 1) // 6 + 1
        self.curPage = QtWidgets.QLabel("1")
        self.baseLayout.removeWidget(self.frame_3)
        self.TaskCardList = []
        # 清空原页面
        count = self.stackedWidget.count()
        for i in range(count):
            widget = self.stackedWidget.currentWidget()
            self.stackedWidget.removeWidget(widget)
        # 即时渲染
        self.setupUi()

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


import src.images.PageTurn_rc

if __name__ == "__main__":
    task2 = {'name': "task2",
             'isDaily': False,
             'startTime': QDateTime(1980, 1, 1, 1, 1),
             'endTime': QDateTime(1980, 1, 1, 2, 1),
             'costTime': QTime(0, 0),
             'type': None,
             'importance': 0,
             'status': 3,
             'detail': None}
    app = QApplication(sys.argv)
    w = PageWidget()
    # w.updateTaskList([task2, task2, task2, task2, task2])
    # w.updateTaskList([])
    w.show()
    sys.exit(app.exec_())
