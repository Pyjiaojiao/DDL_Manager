import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class myPageTurnWidget(QWidget):
    def __init__(self):
        super(myPageTurnWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # TODO
        self.resize(1060, 40)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(130, 0, 800, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        control_layout = QHBoxLayout(self.frame)

        self.prePage = QtWidgets.QPushButton("<上一页")
        self.prePage.setFixedSize(90,30)
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


        self.curPage = QtWidgets.QLabel("1")



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
        self.totalPage = QtWidgets.QLabel("共 " + str(10) + " 页")
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
        self.confirmSkip.setStyleSheet("background-image: url(:/PageTurn_next.png);")
        self.confirmSkip.setText(" ")
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

        self.setLayout(control_layout)

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.prePage.clicked.connect(self.button_clicked)  # 上一页点击
        self.nextPage.clicked.connect(self.button_clicked)  # 下一页点击
        self.confirmSkip.clicked.connect(self.button_clicked)  # 确认键




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))

    def button_clicked(self):
        button_text = self.sender().text()
        total_page = int(self.totalPage.text().split()[1]) #总页数
        current_page = int(self.curPage.text())

        if "<上一页" == button_text:
            self.skipPage.setText('')

            current_page = current_page-1
            if current_page <= 1:
                self.curPage.setText("1")

            else:
                self.curPage.setText(str(current_page))

        if "下一页>" == button_text:
            self.skipPage.setText('')
            current_page = current_page+1
            if current_page <= total_page:
                self.curPage.setText(str(current_page))

        if " " == button_text:
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
    app = QApplication(sys.argv)
    w = myPageTurnWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())