import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, QTime
from PyQt5.QtWidgets import QWidget, QApplication
from Tools import base_op


class TaskInterface(QWidget):
    switch1 = QtCore.pyqtSignal(dict)  # for edit: taskCard->taskInterface
    switch2 = QtCore.pyqtSignal(list)  # for edit: taskInterface->MainWindow
    switch3 = QtCore.pyqtSignal(str)  # for delete: taskCard->taskInterface
    switch4 = QtCore.pyqtSignal(list)  # for delete: taskInterface->MainWindow
    switch5 = QtCore.pyqtSignal(QtCore.QDateTime)  # 用于日历系统：跳转到某天的任务列表: goEverydayTaskDialog->taskInterface
    switch6 = QtCore.pyqtSignal(list, QtCore.QDateTime)  # 用于日历系统:taskInterface->
    switch7 = QtCore.pyqtSignal(dict)  # for search: taskManage->taskInterface
    switch8 = QtCore.pyqtSignal(list)  # for search: taskInterface->MainWindow
    switch9 = QtCore.pyqtSignal(QtCore.QDateTime, dict)  # for search:everydayTask->taskInterface
    switch10 = QtCore.pyqtSignal(list)  # for search:everydayTask->taskInterface

    def __init__(self, user_id):
        super(TaskInterface, self).__init__()
        self.user_id = user_id
        self.back_end = None
        self.origin_task_dict = {'name': None,
                                 'isDaily': False,
                                 'startTime': QDateTime(1970, 1, 1, 0, 0),
                                 'endTime': QDateTime(2050, 1, 1, 0, 0),
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

    def addTask(self, task_dict):
        base_op.add_task(task_dict=task_dict)
        return

    def deleteTask(self, task_name):
        '''cur_task = {}
        for i in self.task_list_test:
            if i['name'] == task_name:
                cur_task = i
            break
        self.task_list_test.remove(cur_task)  # 前端测试用，和后端连接后请删除
        '''
        # 后端处理
        base_op.del_task(task_name=task_name)
        newTaskList = self.searchTask({})  # 这个搜索根据后端实现改
        # 以下勿删
        self.switch4.emit(self.searchTask(newTaskList))

    def editTask(self, task_dict):  # 传入的是switch1.emit(arg)的参数arg，即shortTaskDict
        '''task_name = task_dict['name']
        i = 0
        while i < len(self.task_list_test):
            if self.task_list_test[i]['name'] == task_name:
                self.task_list_test[i] = task_dict
                break  # 前端测试用，和后端连接后请删除'''
        base_op.mod_task(task_name=task_dict['name'], task_mod_dict=task_dict)
        # 后端处理
        newTaskList = self.searchTask({})  # 这个搜索根据后端实现改
        # 以下勿删
        self.switch2.emit(newTaskList)

    # 用于任务管理
    def searchTask(self, feature_dict):
        # cur_task_list = self.task_list_test  # 前端测试用，和后端连接后请删除
        # 后端处理
        cur_task_list = base_op.load_specified_subtasks(specify=feature_dict)
        return cur_task_list

    # 用于每日任务
    def searchTaskFromDate(self, date, feature_dict):  # date:QDateTime()
        feature_dict.update({'date':date})
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


app = QApplication(sys.argv)
taskInterface = TaskInterface(None)
