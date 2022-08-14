import PyQt5.Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys
from Window import Ui_MainWindow as mainUi
from LoginWindow import Ui_MainWindow as loginUi
from TaskInterface import taskInterface
from Chart.ChartInterface import chartInterface


class MainWindow(QMainWindow, mainUi):
    switch2 = QtCore.pyqtSignal()  # to login
    switch3 = QtCore.pyqtSignal()  # to newtask
    initTaskDict = {'name': None,
                    'isDaily': False,
                    'startTime': PyQt5.QtCore.QDateTime(1970, 1, 1, 0, 0),
                    'endTime': PyQt5.QtCore.QDateTime(1970, 1, 1, 0, 0),
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
        taskInterface.switch6.connect(self.goThatDayTask)
        taskInterface.switch8.connect(self.searchInTaskManage)
        taskInterface.switch10.connect(self.searchInEverydayTask)
        chartInterface.switch2.connect(self.updateDataAnalysis)

    def goLogin(self):
        self.switch2.emit()

    def goNewTask(self):
        self.newtask.show()

    def addNewTask(self):
        name = self.newtask.lineEdit.text()
        isDaily = self.newtask.checkBox.isChecked()
        costTime = self.newtask.timeEdit.time()
        endTime = self.newtask.dateEdit_2.dateTime()
        taskType = self.newtask.comboBox.currentText()
        importance = 4 - self.newtask.comboBox_2.currentIndex()  # 从0开始数字越大越重要，最重要为4
        status = self.newtask.comboBox_3.currentIndex()  # 从0开始数字越大完成度越高，最高为4
        detail = self.newtask.textEdit.toPlainText()
        taskDict = {'name': name,  # str
                    'isDaily': isDaily,  # boolean
                    'startTime': QtCore.QDateTime(1970, 1, 1, 0, 0),  # QDateTime
                    'endTime': endTime,  # QDateTime
                    'costTime': costTime,  # QTime(hh, mm)
                    'type': taskType,  # str
                    'importance': importance,  # int 从0开始数字越大越重要，最重要为3
                    'status': status,  # int 从0开始数字越大完成度越高，最高为3
                    'detail': detail}  # str
        # print(taskDict)
        taskInterface.addTask(taskDict)
        newTaskList = taskInterface.searchTask(self.initTaskDict)
        # print(newTaskList)
        self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(newTaskList)  # 添加任务结束，一定回到任务管理页面

        self.newtask.close()

    def deleteTask(self, task_list):
        # print("received" + task_list.__str__())
        self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(task_list)

    def reWriteTask(self, task_list):
        self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(task_list)

    def goThatDayTask(self, task_list, date):
        self.leftTabWidget.everyDayTaskWidget.PageWidget.updateTaskList(task_list)
        self.leftTabWidget.everyDayTaskWidget.updateDate(date)
        self.leftTabWidget.listWidget.setCurrentItem(self.leftTabWidget.listWidget.itemAt(0, 0))

    def searchInTaskManage(self, task_list):
        self.leftTabWidget.taskManageWidget.PageWidget.updateTaskList(task_list)

    def searchInEverydayTask(self, task_list):
        self.leftTabWidget.everyDayTaskWidget.PageWidget.updateTaskList(task_list)

    def updateDataAnalysis(self, chart_dict):
        self.leftTabWidget.dataAnalysisWidget.dataPageWidget.updateDateAnalysis(chart_dict)


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
        self.login.setWindowTitle("Login")

    def login_success(self):
        self.main = MainWindow()
        self.main.setWindowTitle("Task Scheduler")
        self.main.setWindowIcon(QIcon("../src/icons/EverydayTask_calendar.png"))

    def showLogin(self):
        taskInterface.switch14.connect(self.showMain)
        self.login.show()

    def showMain(self):
        self.main.setWindowTitle("Task Scheduler")
        self.main.setWindowIcon("./src/icons/EverydayTask_calendar.png")
        self.login_success()
        self.main.switch2.connect(self.showLogin)
        self.login.close()
        self.main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    myWin = Controller()
    myWin.showLogin()
    sys.exit(app.exec_())  # 在主线程中退出
