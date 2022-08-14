import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout
from program.AccountManage.myOutWidget import OutWidget
from program.AccountManage.myWechatEdit import WechatWidget
from program.AccountManage.myPhoneWidget import PhoneWidget
from program.AccountManage.myPassportWidget import PassportWidget
from program.AccountManage.myBasicInformationWidget import BasicInformationWidget
from program.AccountManage.myEmailWidget import EmailWidget

class AccountManageWindow(QWidget) :
    def __init__(self, *args, **kwargs):
        super(AccountManageWindow, self).__init__(*args, **kwargs)
        self.resize(1060, 720)
        self.setStyleSheet("background-color:rgb(226, 232, 254)")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1060, 720))
        self.widget.setStyleSheet("background-color:rgb(226, 232, 254)")

        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 90, 1060, 570))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("background-image: url(:/AccountManagement_background.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.baseLayout = QtWidgets.QGridLayout(self, spacing=0)
        self.baseLayout.setContentsMargins(50, 50, 50, 50)

        self.setupUi()

    def setupUi(self):

        self.BasicInformationWidget = BasicInformationWidget()

        self.layout1_widget = QtWidgets.QWidget(self.widget)
        self.layout1 = QGridLayout(self.layout1_widget,spacing=0)
        self.layout1_widget.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.layout1.addWidget(self.BasicInformationWidget)


        self.baseLayout.addWidget(self.layout1_widget,0,0)

        self.PassportWidget = PassportWidget()
        self.PhoneWidget = PhoneWidget()
        self.WechatWidget = WechatWidget()
        self.EmailWidget = EmailWidget()
        self.OutWidget = OutWidget()



        self.layout2_widget = QtWidgets.QWidget(self.widget)
        self.layout2_widget.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.layout2 = QGridLayout(self.layout2_widget, spacing=0)
        self.layout2.setContentsMargins(100,50,50,50)

        self.layout2.addWidget(self.PassportWidget, 0, 0)
        self.layout2.addWidget(self.PhoneWidget, 1, 0)
        self.layout2.addWidget(self.EmailWidget, 2, 0)
        self.layout2.addWidget(self.WechatWidget, 3, 0)
        self.layout2.addWidget(self.OutWidget, 4, 0)

        self.baseLayout.addWidget(self.layout2_widget, 0, 1)

        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # self.pushButton.setText(_translate("MainWindow", "添加任务"))
        # self.pushButton_2.setText(_translate("MainWindow", "删除任务"))

import src.images.AccountManagement_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AccountManageWindow()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())


