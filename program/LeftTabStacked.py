#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

import PyQt5
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QSize, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, \
    QListWidgetItem, QLabel, QApplication
# from CalendarWidget import CalendarWidget
# from EverydayTaskWindow import EveryDayTaskWindow
# from TaskManagementWindow import TaskManagementWindow
# from TaskManageWindow import TaskManageWindow
# Created on 2018年5月29日
# author: Irony
# site: https://pyqt5.com , https://github.com/892768447
# email: 892768447@qq.com
# file: LeftTabWidget
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0

# from program.TaskCard import TaskCard
from DataAnalysisWindow import DataAnalysisWindow
from TaskManagementWindow import TaskManagementWindow
from EverydayTaskWindow import EveryDayTaskWindow
from AccountManageWindow import AccountManageWindow
from CalendarWidget import CalendarWidget


class LeftTabWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.everyDayTaskWidget = EveryDayTaskWindow()
        self.taskManageWidget = TaskManagementWindow()
        self.dataAnalysisWidget = DataAnalysisWindow()
        self.accountManageWidget = AccountManageWindow()

        self.pageNames = ["每日任务", "任务管理", "日历系统", "数据分析", "账号选项"]
        self.resize(1280, 720)
        # 左右布局(左边一个QListWidget + 右边QStackedWidget)
        # layout = QHBoxLayout(self, spacing=0)
        # layout.setContentsMargins(0, 0, 0, 0)
        # 左侧列表
        # 左侧列表参数设置
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(0, 0, 220, 720)
        #self.listWidget.setFixedSize(220, 720)
        self.listWidget.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"color: rgb(85, 85, 85)")
        # layout.addWidget(self.listWidget)
        # 右侧层叠窗口
        # 右侧列表参数设置
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(220, 0, 1060, 720)
        #self.stackedWidget.setFixedSize(1060, 720)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        # layout.addWidget(self.stackedWidget)
        self.initUi()

    def initUi(self):
        # 初始化界面
        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)
        # 去掉边框
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 这里就用一般的文本配合图标模式了(也可以直接用Icon模式,setViewMode)
        for i in range(5):
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item = QListWidgetItem(str('%s' % self.pageNames[i]), self.listWidget)
            item.setFont(font)

            # 设置item的默认宽高(这里只有高度比较有用)
            item.setSizeHint(QSize(16777215, 60))
            # 文字居中
            item.setTextAlignment(Qt.AlignCenter)
        # 左侧下方的按钮
        '''
        leftBottomItem_1 = QListWidgetItem(QIcon('../src/icon/add.ico'), str(''), self.listWidget)
        leftBottomItem_1.setSizeHint(QSize(30, 30))
        leftBottomItem_1.setBackground(Qt.white)
        '''
        #self.listWidget
        # 右侧的页面
        # Page1：每日任务
        gridLayoutWidget_1 = QtWidgets.QWidget()
        gridLayoutWidget_1.setStyleSheet("background-color:rgb(0,0,0,0)")
        gridLayoutWidget_1.setGeometry(220, 0, 1060, 720)
        gridLayOut_1 = QtWidgets.QGridLayout(gridLayoutWidget_1)
        gridLayOut_1.setContentsMargins(0, 0, 0, 0)
        self.everyDayTaskWidget.setObjectName("everyDayTask")
        self.everyDayTaskWidget.setGeometry(220, 0, 1060, 720)
        gridLayOut_1.addWidget(self.everyDayTaskWidget)
        self.stackedWidget.addWidget(gridLayoutWidget_1)

        # Page2：任务管理
        gridLayoutWidget_2 = QtWidgets.QWidget()
        gridLayoutWidget_2.setGeometry(0, 0, 1060, 720)
        gridLayOut_2 = QtWidgets.QGridLayout(gridLayoutWidget_2)
        gridLayOut_2.setContentsMargins(0, 0, 0, 0)
        self.taskManageWidget.setObjectName("taskManagement")
        self.taskManageWidget.setGeometry(220, 0, 1060, 720)
        # self.TaskManageWidget.setObjectName("taskManagement")
        # self.TaskManageWidget.setGeometry(0, 0, 1060, 620)
        gridLayOut_2.addWidget(self.taskManageWidget)
        gridLayoutWidget_2.raise_()
        gridLayoutWidget_2.setLayout(gridLayOut_2)
        self.stackedWidget.addWidget(gridLayoutWidget_2)



        # Page3：日历系统
        gridLayoutWidget_3 = QtWidgets.QWidget()
        gridLayOut_3 = QtWidgets.QGridLayout(gridLayoutWidget_3)
        gridLayOut_3.setContentsMargins(0, 0, 0, 0)
        calendarWidget = CalendarWidget()
        calendarWidget.setObjectName("calendar")
        gridLayOut_3.addWidget(calendarWidget)
        self.stackedWidget.addWidget(gridLayoutWidget_3)

        # Page4：数据分析
        gridLayoutWidget_4 = QtWidgets.QWidget()
        gridLayoutWidget_4.setGeometry(0, 0, 1060, 720)
        gridLayoutWidget_4.setStyleSheet("background-color: rgb(250, 236, 227)")
        gridLayOut_4 = QtWidgets.QGridLayout(gridLayoutWidget_4)
        gridLayOut_4.setContentsMargins(0, 0, 0, 0)
        self.dataAnalysisWidget.setObjectName("dataAnalysis")
        self.dataAnalysisWidget.test()
        gridLayOut_4.addWidget(self.dataAnalysisWidget)
        self.stackedWidget.addWidget(gridLayoutWidget_4)

        # Page5：账号选项
        gridLayoutWidget_5 = QtWidgets.QWidget()
        gridLayoutWidget_5.setGeometry(220, 0, 1060, 720)
        gridLayoutWidget_5.setStyleSheet("background-color:rgb(0,0,0,0)")
        gridLayOut_5 = QtWidgets.QGridLayout(gridLayoutWidget_5)
        gridLayOut_5.setContentsMargins(0, 0, 0, 0)
        gridLayOut_5.addWidget(self.accountManageWidget)
        self.stackedWidget.addWidget(gridLayoutWidget_5)

        self.setStyleSheet(Stylesheet)


# 样式表
Stylesheet = """
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    min-width: 220px;
    max-width: 220px;
    color: rgb(250,250,250);
    background-color: rgb(250, 250, 250);
}
/*被选中时的背景颜色和左边框颜色*/
QListWidget::item:selected {
    background: rgb(238, 238, 238);
    color: rgb(0, 0, 0);
    border-radius:20px;
    
}
/*鼠标悬停颜色*/
HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

/*右侧的层叠窗口的背景颜色*/
QStackedWidget {
    background: rgb(30, 30, 30);
}
/*模拟的页面*/
QLabel {
}
"""
'''
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())
'''
# import src.icon.leftListIcons_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LeftTabWidget()
    # 你的测试代码，比如可以静态/动态装载一些数据进去
    w.show()
    sys.exit(app.exec_())

