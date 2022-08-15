import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QColor, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice


class ChartView(QMainWindow):
    titleDict = {
        'taskTypeList': "任务类型占比饼图",
        'taskStatusList': "任务状态占比饼图",
        'taskImportanceList': "任务重要性占比饼图",
        'taskFinishmentList': "任务完成情况占比饼图"
    }
    nameDict = {
        'taskStatusList': ["未开始", "进行中", "已完成", "已过期"],
        'taskImportanceList': ["不重要", "一般", "重要", "非常重要"],
        'taskFinishmentList': ["已完成", "已过期"]
    }

    def __init__(self, parent=None):
        super(ChartView, self).__init__(parent)
        # 设置窗口大小
        self.resize(480, 360)
        # self.initChart()

    def initChart(self, dict_keyname, chart_list):
        # 设置饼图数据
        pieSeries = self.createSeries(dict_keyname, chart_list)
        # 图表视图
        chartView = QChartView()
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.chart().setBackgroundVisible(False)
        chartView.chart().setTitle(self.titleDict[dict_keyname])
        chartView.chart().setTitleFont(QFont('微软雅黑', 8))
        chartView.chart().addSeries(pieSeries)
        chartView.chart().legend().setAlignment(Qt.AlignBottom)
        chartView.chart().setTheme(QChart.ChartThemeLight)
        chartView.chart().legend().setFont(QFont('微软雅黑', 8))  # 图例字体

        self.setCentralWidget(chartView)

    def createSeries(self, dict_keyname, chart_list):
        pieSeries = QPieSeries()
        pieSeries.setHoleSize(0.35)
        font = QFont('微软雅黑', 8)
        if dict_keyname == 'taskTypeList':
            count = 0
            if count == 0:
                count = 1
            for i in chart_list:
                count += i[1]
            for i in chart_list:
                pieSlice = pieSeries.append(i[0], i[1])
                pieSlice.setLabelVisible(True)
                pieSlice.setLabelFont(font)
        elif dict_keyname == 'taskStatusList':
            count = chart_list[0][1] + chart_list[1][1] + chart_list[2][1] + chart_list[3][1]
            if count == 0:
                count = 1
            pieSeries.append(self.nameDict[dict_keyname][0] + "%d%%" % (chart_list[0][1] / count * 100),
                             chart_list[0][1])
            pieSeries.append(self.nameDict[dict_keyname][1] + "%d%%" % (chart_list[1][1] / count * 100),
                             chart_list[1][1])
            pieSlice = pieSeries.append(self.nameDict[dict_keyname][2] + "%d%%" % (chart_list[2][1] / count * 100),
                                        chart_list[2][1])
            pieSlice.setExploded()
            pieSlice.setLabelVisible()  # 设置标签可见,缺省不可见
            pieSlice.setLabelFont(font)
            pieSlice.setColor(QColor(255, 80, 80))
            pieSeries.append(self.nameDict[dict_keyname][3] + "%d%%" % (chart_list[3][1] / count * 100),
                             chart_list[3][1])
        elif dict_keyname == 'taskImportanceList':
            count = chart_list[0][1] + chart_list[1][1] + chart_list[2][1] + chart_list[3][1]
            if count == 0:
                count = 1
            pieSeries.append(self.nameDict[dict_keyname][0] + "%d%%" % (chart_list[0][1] / count * 100),
                             chart_list[0][1])
            pieSeries.append(self.nameDict[dict_keyname][1] + "%d%%" % (chart_list[1][1] / count * 100),
                             chart_list[1][1])
            pieSeries.append(self.nameDict[dict_keyname][2] + "%d%%" % (chart_list[2][1] / count * 100),
                             chart_list[2][1])
            pieSlice = pieSeries.append(self.nameDict[dict_keyname][3] + "%d%%" % (chart_list[3][1] / count * 100),
                                        chart_list[3][1])
            pieSlice.setExploded()
            pieSlice.setLabelVisible()  # 设置标签可见,缺省不可见
            pieSlice.setColor(QColor(255, 80, 80))
        elif dict_keyname == 'taskFinishmentList':
            count = chart_list[0][1] + chart_list[1][1]
            if count == 0:
                count = 1
            pieSlice = pieSeries.append(self.nameDict[dict_keyname][0] + "%d%%" % (chart_list[0][1] / count * 100),
                             chart_list[0][1])
            pieSlice.setLabelVisible(True)
            pieSlice = pieSeries.append(self.nameDict[dict_keyname][1] + "%d%%" % (chart_list[1][1] / count * 100),
                                        chart_list[1][1])
            pieSlice.setLabelVisible()  # 设置标签可见,缺省不可见
            pieSlice.setColor(QColor(255, 80, 80))

        return pieSeries


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChartView()
    # window.initChart('taskImportanceList', [(0, 4), (1, 5), (2, 6), (3, 3)])
    # window.initChart('taskTypeList', [("学习", 4), ("运动", 5), ("娱乐", 6), ("工作", 3), ("其他", 4)])
    #window.initChart('taskStatusList', [(0, 4), (1, 5), (2, 6), (3, 3)])
    window.initChart('taskStatusList', [(0, 0), (1, 0), (2, 0), (3, 0)])
    # window.initChart('taskFinishmentList', [(0, 4), (1, 5)])


    window.show()
    sys.exit(app.exec())
