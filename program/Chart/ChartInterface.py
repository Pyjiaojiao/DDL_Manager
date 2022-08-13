import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication, QWidget


class ChartInterface(QWidget):
    switch1 = QtCore.pyqtSignal(dict)  # 数据分析检索：数据分析页面（检索按钮）->ChartInterface
    switch2 = QtCore.pyqtSignal(dict)  # 数据分析检索：ChartInterface->MainWindow

    def __init__(self):
        super(ChartInterface, self).__init__()
        self.chart_dict = {'startDate': QDateTime(1970, 1, 1, 0, 0),  # QDateTime
                           'endDate': QDateTime(2050, 1, 1, 0, 0),  # QDateTime 指定查询的开始和截止日期（只考虑日期，不计小时分钟）
                           # 以下字段均针对“所有时间”
                           'totalOriginTaskCount': 0,  # int
                           'totalTaskCount': 0,  # int 拆分任务总数+日常任务总数，其中日常任务每天均计数
                           'totalTaskFinishRate': 0,  # float:[0,1] 总任务完成率, 针对已到截止时间的拆分任务+日常任务
                           # 以下字段均针对“指定的startDate和endDate之间”
                           'curOriginTaskCount': 0,
                           'curTaskCount': 0,
                           'curFinishTaskCount':0,
                           'curTaskFinishRate': 0,
                           'timeEstimatedList': list,  # tuple(hour:int, count:int),其中hour是时间范围的上限。
                           # 例如：[(3,5),(6,10)]的含义是：预期时长为0-3时的任务有5个，3-6h的任务有10个，hour步长为3。hour的步长是均匀的，具体数值应由后端确定，保证len(list)<10即可。
                           # 这里的“预期时长”针对原始任务，日常任务只记一次。
                           'taskTypeList': list,  # tuple(type:str, count:int)，针对原始任务，日常任务只记一次。
                           'taskStatusList': list,  # tuple(status:int, count:int) status的值与TaskDict相同，针对原始任务
                           'taskImportanceList': list,
                           # tuple(importance:int, count:int) importance的值与TaskDict相同，针对原始任务
                           'taskFinishmentList': list,
                           # [(True, count:int),(False, count:int)]针对**当前时间**已截止的任务进行统计，list第一项记录已完成任务的数量，list第二项记录未完成任务（状态为已过期，index=3）的数量。
                           # 针对拆分任务和日常任务。
                           'taskTimeDistributeInOneDay': list,
                           # [(3, count:int),(6, count:int),(9, count:int),...,(24, count:int)], list结构类似timeEstimatedList, 其中hour步长固定为3.
                           # 含义是：在指定的startDate和endDate内，一天的0-3点、3-6点、...21-24点**有覆盖**的任务数量
                           # 针对拆分任务和日常任务
                           'taskFinishRateInOneDay': list  # 和上一条类似，count替换为FinishRate。
                           # 针对已到截止时间的拆分任务+日常任务
                           }
        self.switch1.connect(self.searchChartData)
        return


    # date_dict={startDate:QDate, endDate:QDate}
    def searchChartData(self, date_dict):
        chart_dict = {}
        self.switch2.emit(chart_dict)
        return


app = QApplication(sys.argv)
chartInterface = ChartInterface()
