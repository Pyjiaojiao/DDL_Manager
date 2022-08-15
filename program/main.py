import PyQt5.Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys

from ChartInterface import chartInterface
from Window import Ui_MainWindow as mainUi
from LoginWindow import Ui_MainWindow as loginUi
from TaskInterface import taskInterface


class MainWindow(QMainWindow, mainUi):
    switch2 = QtCore.pyqtSignal()  # to login
    switch3 = QtCore.pyqtSignal()  # to newtask
    initTaskDict = {'name': None,
                    'isDaily': False,
                    'startTime': PyQt5.QtCore.QDate(1970, 1, 1),
                    'endTime': PyQt5.QtCore.QDate(2050, 1, 1),
                    'costTime': PyQt5.QtCore.QTime(0, 0),
                    'type': None,
                    'importance': 0,
                    'status': 0,
                    'detail': None}

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.leftTabWidget.accountManageWidget.OutWidget.pushButton.clicked.connect(self.goLogin)
        # self.leftTabWidget.pushButton_5_1.clicked.connect(self.goLogin)
        self.leftTabWidget.taskManageWidget.AddAndDeleteWidget.pushButton.clicked.connect(self.goNewTask)  # 添加任务页面

        self.newtask.pushButton.clicked.connect(self.addNewTask)
        taskInterface.switch2.connect(self.reWriteTask)
        taskInterface.switch4.connect(self.deleteTask)
        taskInterface.switch4_.connect(self.deleteTaskFromDate)
        taskInterface.switch6.connect(self.goThatDayTask)
        taskInterface.switch8.connect(self.searchInTaskManage)
        taskInterface.switch10.connect(self.searchInEverydayTask)
        taskInterface.switch18.connect(self.finishTaskFromDate)
        taskInterface.switch20.connect(self.updateDataAnalysis)
        taskInterface.switch22.connect(self.updateUsrInfo)

    def goLogin(self):
        self.switch2.emit()

    def goNewTask(self):
        self.newtask.show()

    def addNewTask(self):
        name = self.newtask.lineEdit.text()
        isDaily = self.newtask.checkBox.isChecked()
        costTime = self.newtask.timeEdit.time()
        startDate = self.newtask.dateEdit.date()
        endDate = self.newtask.dateEdit_2.date()
        taskType = self.newtask.comboBox.currentText()
        importance = self.newtask.comboBox_2.currentIndex()  # 从0开始数字越大越重要，最重要为3
        status = self.newtask.comboBox_3.currentIndex()  # 从0开始数字越大完成度越高，最高为3
        detail = self.newtask.textEdit.toPlainText()
        taskDict = {'name': name,  # str
                    'isDaily': isDaily,  # boolean
                    'startDate': startDate,  # QDate
                    'endDate': endDate,  # QDate
                    'costTime': costTime,  # QTime(hh, mm)
                    'type': taskType,  # str
                    'importance': importance,  # int 从0开始数字越大越重要，最重要为3
                    'status': status,  # int 从0开始数字越大完成度越高，最高为3
                    'detail': detail}  # str
        print("inputTaskDict:" + taskDict.__str__())
        taskInterface.addTask(taskDict)
        self.leftTabWidget.taskManageWidget.searchTask()
        self.leftTabWidget.taskManageWidget.PageWidget.setPageMode(2)
        self.leftTabWidget.everyDayTaskWidget.searchTaskFromDate()
        # self.leftTabWidget.everyDayTaskWidget.searchTaskFromDate(self.leftTabWidget.everyDayTaskWidget.date)
        # self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(newTaskList)  # 添加任务结束，一定回到任务管理页面
        '''
        # 修好每日任务后解除注释吧！
        newTaskList = self.leftTabWidget.everyDayTaskWidget.searchTaskFromDate()
        # print(newTaskList)
        self.leftTabWidget.everyDayTaskWidget.PageWidget.updateTaskList(newTaskList)  # 同时更新每日任务界面'''

        self.newtask.close()

    def deleteTask(self):
        # newTaskList = taskInterface.searchTask({})
        # self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(newTaskList)
        self.leftTabWidget.taskManageWidget.searchTask()
        self.leftTabWidget.taskManageWidget.PageWidget.setPageMode(2)

    def deleteTaskFromDate(self, date):
        # newTaskList = taskInterface.searchTaskFromDate(date, {})
        # self.leftTabWidget.everyDayTaskWidget.PageWidget.updateTaskList(newTaskList)
        self.leftTabWidget.everyDayTaskWidget.updateDate(date)
        self.leftTabWidget.everyDayTaskWidget.searchTaskFromDate()

    def reWriteTask(self):
        self.leftTabWidget.taskManageWidget.searchTask()
        # self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(task_list)
        self.leftTabWidget.taskManageWidget.PageWidget.setPageMode(2)

    def goThatDayTask(self, task_list, date):
        self.leftTabWidget.everyDayTaskWidget.PageWidget.updateTaskList(task_list)
        self.leftTabWidget.everyDayTaskWidget.updateDate(date)
        self.leftTabWidget.listWidget.setCurrentItem(self.leftTabWidget.listWidget.itemAt(0, 0))

    def searchInTaskManage(self, task_list):
        self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(task_list)
        self.leftTabWidget.taskManageWidget.PageWidget.setPageMode(2)

    def searchInEverydayTask(self, task_list):
        self.leftTabWidget.everyDayTaskWidget.PageWidget.updateTaskList(task_list)

    def finishTask(self):
        self.leftTabWidget.taskManageWidget.searchTask()

    def finishTaskFromDate(self, date):
        self.leftTabWidget.everyDayTaskWidget.updateDate(date)
        # self.leftTabWidget.everyDayTaskWidget.searchTaskFromDate()

    def updateDataAnalysis(self, chart_dict):
        print("main")
        # print(chart_dict)
        self.leftTabWidget.dataAnalysisWidget.dataPageWidget.updateDateAnalysis(chart_dict)

    def updateUsrInfo(self):
        self.leftTabWidget.accountManageWidget.\
            BasicInformationWidget.updateInformation(taskInterface.getUsrInfo())


class Login(QMainWindow, loginUi):
    switch1 = QtCore.pyqtSignal()  # to main

    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.goMain)

    def goMain(self):
        self.switch1.emit()

    def clearTextInput(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")


class Controller:
    def __init__(self):
        self.login = Login()
        self.main = None
        self.login.setWindowTitle("Login")
        self.login.setWindowIcon(QIcon(":/LoginSign.png"))

    def login_success(self):
        self.main = MainWindow()
        self.main.setWindowTitle("DDL Manager")
        self.main.setWindowIcon(QIcon(":/MainPage.png"))

    def showLogin(self):
        taskInterface.switch14.connect(self.showMain)
        self.login.show()
        if self.main is not None:
            self.main.close()

    def showMain(self):
        self.login_success()
        self.main.switch2.connect(self.showLogin)
        self.login.close()
        self.main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    myWin = Controller()
    myWin.showLogin()
    sys.exit(app.exec_())  # 在主线程中退出

import src.icons.WindowIcons_rc
import src.images.DataAnalysis_rc
