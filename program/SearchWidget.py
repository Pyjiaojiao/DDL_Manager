import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent


class mySearchWidget(QWidget):
    def __init__(self):
        super(mySearchWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        # TODO
        # 背景
        self.resize(780, 60)
        self.setStyleSheet("background-color:rgb(235, 251, 232);\n"
                           "border-radius:8px")
        # 设置搜索按钮
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setGeometry(QtCore.QRect(740, 15, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)

        self.searchButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "image: url(:/TaskManagement_search.png);\n"
                                        "")
        self.searchButton.setText("")
        self.searchButton.setObjectName("selfButton")
        self.searchButton.raise_()

        # 设置全部按钮
        self.allButton = QtWidgets.QPushButton(self)
        self.allButton.setGeometry(QtCore.QRect(10, 15, 112, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton.sizePolicy().hasHeightForWidth())
        self.allButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.allButton.setFont(font)
        self.allButton.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                     "border-radius:5px")
        self.allButton.setObjectName("allButton")
        # 设置三个选择按钮
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(140, 15, 140, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius:5px")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 15, 140, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius:5px\n"
                                      "")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self)
        self.comboBox_3.setGeometry(QtCore.QRect(460, 15, 130, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius:5px\n"
                                      "")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        # 是否日常
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setTristate(True)
        self.checkBox.setCheckState(QtCore.Qt.PartiallyChecked)
        self.checkBox.setGeometry(QtCore.QRect(620, 15, 105, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setStyleSheet("background-color:rgb(0,0,0,0)")
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.allButton.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.checkBox.raise_()
        self.searchButton.raise_()

        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.searchButton.setText(_translate("Form", ""))
        self.allButton.setText(_translate("Form", "全部"))
        self.comboBox.setItemText(0, _translate("Form", "选择任务状态"))
        self.comboBox.setItemText(1, _translate("Form", "未开始"))
        self.comboBox.setItemText(2, _translate("Form", "正在进行中"))
        self.comboBox.setItemText(3, _translate("Form", "已完成"))
        self.comboBox.setItemText(4, _translate("Form", "已过期"))
        self.comboBox_2.setItemText(0, _translate("Form", "选择任务类型"))
        self.comboBox_2.setItemText(1, _translate("Form", "学习"))
        self.comboBox_2.setItemText(2, _translate("Form", "工作"))
        self.comboBox_2.setItemText(3, _translate("Form", "运动"))
        self.comboBox_2.setItemText(4, _translate("Form", "娱乐"))
        self.comboBox_2.setItemText(5, _translate("Form", "其他"))
        self.comboBox_3.setItemText(0, _translate("Form", "选择重要性"))
        self.comboBox_3.setItemText(4, _translate("Form", "非常重要"))
        self.comboBox_3.setItemText(3, _translate("Form", "重要"))
        self.comboBox_3.setItemText(2, _translate("Form", "一般"))
        self.comboBox_3.setItemText(1, _translate("Form", "不重要"))
        self.checkBox.setText(_translate("Form", "日常任务"))

    def getFeatureDict(self):
        feature_dict = {}
        if self.checkBox.checkState() == QtCore.Qt.Checked: # 选中是日常任务，不选中非日常任务，半选中均有
            feature_dict.update({'isDaily': True})
        elif self.checkBox.checkState() == QtCore.Qt.Unchecked:
            feature_dict.update({'isDaily': False})
        if self.comboBox_2.currentIndex() != 0:
            # print("now type is " + self.comboBox_2.currentIndex().__str__())
            typeList = ["学习", "工作", "运动", "娱乐", "其他"]
            feature_dict.update({'type': typeList[int(self.comboBox_2.currentIndex() - 1)]})
        if self.comboBox_3.currentIndex() != 0:
            feature_dict.update({'importance': self.comboBox_3.currentIndex() - 1})
        if self.comboBox.currentIndex() != 0:
            feature_dict.update({'status': self.comboBox.currentIndex() - 1})
        '''feature_dict = {
            'isDaily': self.checkBox.isChecked(),
            'type': self.comboBox_2.currentText(),
            'importance': self.comboBox_3.currentIndex(),
            'status': self.comboBox.currentIndex()
        }'''
        # print(feature_dict)
        return feature_dict


import src.images.TaskManagementWindow_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = mySearchWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())
