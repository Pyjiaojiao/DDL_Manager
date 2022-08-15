import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTime, QDate
from PyQt5.QtWidgets import QWidget, QApplication
from Tools import base_op
from ChartInterface import chartInterface

class TaskInterface(QWidget):
    switch1 = QtCore.pyqtSignal(dict)  # for edit: taskCard->taskInterface
    switch2 = QtCore.pyqtSignal()  # for edit: taskInterface->MainWindow
    switch3 = QtCore.pyqtSignal(str)  # for delete: taskCard->taskInterface
    switch4 = QtCore.pyqtSignal()  # for delete: taskInterface->MainWindow
    switch3_ = QtCore.pyqtSignal(str, QtCore.QDateTime)  # for delete: taskCard->taskInterface
    switch4_ = QtCore.pyqtSignal(QtCore.QDate)  # for delete: taskInterface->MainWindow
    switch5 = QtCore.pyqtSignal(QtCore.QDate)  # 用于日历系统：跳转到某天的任务列表: goEverydayTaskDialog->taskInterface
    switch6 = QtCore.pyqtSignal(list, QtCore.QDate)  # 用于日历系统:taskInterface->MainWindow
    switch7 = QtCore.pyqtSignal(dict)  # for search: taskManage->taskInterface
    switch8 = QtCore.pyqtSignal(list)  # for search: taskInterface->MainWindow
    switch9 = QtCore.pyqtSignal(QtCore.QDate, dict)  # for search:everydayTask->taskInterface
    switch10 = QtCore.pyqtSignal(list)  # for search:everydayTask->taskInterface
    switch11 = QtCore.pyqtSignal(dict)  # for register:loginWindow->taskInterface
    switch12 = QtCore.pyqtSignal()  # for register:taskInterface->loginWindow
    switch13 = QtCore.pyqtSignal(dict)  # for login:loginWindow->taskInterface
    switch14 = QtCore.pyqtSignal()  # for login:taskInterface->MainWindow
    switch15 = QtCore.pyqtSignal(dict)  # finish task:taskManage->taskInterface
    switch16 = QtCore.pyqtSignal()  # finish task:taskInterface->MainWindow
    switch17 = QtCore.pyqtSignal(QtCore.QDate, dict)  # finish date task:everydayTask->taskInterface
    switch18 = QtCore.pyqtSignal(QtCore.QDate)  # finish date task:taskInterface->MainWindow
    switch19 = QtCore.pyqtSignal(dict)
    switch20 = QtCore.pyqtSignal(dict)
    def __init__(self, user_id):
        super(TaskInterface, self).__init__()
        self.user_id = user_id
        self.back_end = None
        self.origin_task_dict = {'name': None,
                                 'isDaily': False,
                                 'startTime': QDate(1970, 1, 1),
                                 'endTime': QDate(2050, 1, 1),
                                 'costTime': QTime(0, 0),
                                 'type': None,
                                 'importance': 0,
                                 'status': 0,
                                 'detail': None}  # 用于模拟搜索所有task，后端自行修改
        self.blank_dict = {}
        self.task_list_test = []

        self.switch1.connect(self.editTask)
        self.switch3.connect(self.deleteTask)
        self.switch5.connect(self.goThatDayTask)
        self.switch7.connect(self.searchInTaskManage)
        self.switch9.connect(self.searchInEverydayTask)
        self.switch11.connect(self.registerAccount)
        self.switch13.connect(self.loginAccount)
        self.switch15.connect(self.finishTask)
        self.switch17.connect(self.finishTaskFromDate)
        self.switch19.connect(self.updateDataAnalysis)

    def addTask(self, task_dict):
        base_op.add_task(task_dict=task_dict)
        base_op.re_arrange()
        return

    def deleteTask(self, task_name):
        # 后端处理
        print("now delete:" + task_name)
        base_op.del_task(task_name=task_name)
        base_op.re_arrange()
        # 以下勿删
        self.switch4.emit()

    def deleteTaskFromDate(self, task_name, task_start_time):
        date = QtCore.QDate.fromString(task_start_time.toString("yyyy/MM/dd"), "yyyy/MM/dd")
        # 后端处理
        base_op.delete_subtask(task_name=task_name, task_start_time=task_start_time)
        # 以下勿删
        self.switch4_.emit(date)

    def editTask(self, task_dict):  # 传入的是switch1.emit(arg)的参数arg，即shortTaskDict
        base_op.mod_task(task_name=task_dict['name'], task_mod_dict=task_dict)
        # 后端处理
        base_op.re_arrange()
        # newTaskList = self.searchTask({})  # 这个搜索根据后端实现改
        #self.switch2.emit(newTaskList)
        self.switch2.emit()

    # 任务管理界面：完成任务
    def finishTask(self, task_dict):
        # 后端处理，无需搜索;搜索在main.py:finishTask()处理
        self.switch16.emit()

    # 每日任务界面：完成任务
    def finishTaskFromDate(self, date, task_dict):
        # 后端处理，无需搜索
        print("startTime is ")
        print(task_dict['startTime'])
        base_op.finish_subtask(task_name=task_dict['name'], task_start_time=task_dict['startTime'])
        self.switch18.emit(date)

    # 用于任务管理
    def searchTask(self, feature_dict):
        # cur_task_list = self.task_list_test  # 前端测试用，和后端连接后请删除
        # 后端处理
        print("input feature_dict")
        print(feature_dict)
        cur_task_list = base_op.load_specified_subtasks(specify=feature_dict)
        return cur_task_list

    # 用于每日任务
    def searchTaskFromDate(self, date, feature_dict):  # date:QDate()
        feature_dict.update({'date': date})
        cur_task_list = base_op.load_specified_subtasks(specify=feature_dict)
        # 后端函数f(date, feature_dict)
        return cur_task_list

    # 日历系统：查看某天的任务
    def goThatDayTask(self, date):
        newTaskList = self.searchTaskFromDate(date, {})
        self.switch6.emit(newTaskList, date)

    # 任务管理界面：多关键字搜索
    def searchInTaskManage(self, feature_dict):
        newTaskList = self.searchTask(feature_dict)
        self.switch8.emit(newTaskList)

    # 每日任务界面
    def searchInEverydayTask(self, date, feature_dict):
        newTaskList = self.searchTaskFromDate(date, feature_dict)
        self.switch10.emit(newTaskList)

    def registerAccount(self, usrDict):
        print(usrDict['usr_id'])
        print(usrDict['pwd'])
        r = base_op.register(usr_id=usrDict['usr_id'], password=usrDict['pwd'])
        if r < 0:
            print("register fail")

    def loginAccount(self, usrDict):
        print(usrDict)
        r = base_op.login(usr_id=usrDict['usr_id'], password_in=usrDict['pwd'])
        if r < 0:
            print("login fail")
        else:
            self.switch14.emit()

    def updateDataAnalysis(self, chart_dict):
        print(chart_dict)
        self.switch20.emit(chart_dict)



app = QApplication(sys.argv)
taskInterface = TaskInterface(None)
