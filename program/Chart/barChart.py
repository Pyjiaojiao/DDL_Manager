from random import randint
import sys

from PyQt5 import QtGui
from PyQt5.QtChart import QChartView, QChart, QBarSeries, QBarSet, QBarCategoryAxis
from PyQt5.QtCore import Qt, QPointF, QRectF, QPoint
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QApplication, QGraphicsLineItem, QWidget, \
    QHBoxLayout, QLabel, QVBoxLayout, QGraphicsProxyWidget, QStyle


class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))

        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        self.titleLabel.setFont(QFont("微软雅黑", 8))
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, bars):
        self.titleLabel.setText(title)
        for bar, value in bars:
            if bar not in self.Cache:
                item = ToolTipItem(
                    bar.color(),
                    (bar.label() or "-") + ":" + str(value), self)
                item.setFont(QFont("微软雅黑", 8))
                self.layout().addWidget(item)
                self.Cache[bar] = item
            else:
                self.Cache[bar].setText(
                    (bar.label() or "-") + ":" + str(value))
                self.Cache[bar].setFont(QFont("微软雅黑", 8))
            brush = bar.brush()
            color = brush.color()
            self.Cache[bar].setVisible(color.alphaF() == 1.0)  # 隐藏那些不可用的项
        self.adjustSize()  # 调整大小


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        self.setWidget(self.tipWidget)
        self.hide()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def show(self, title, bars, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, bars)
        super(GraphicsProxyWidget, self).show()


class ChartView(QChartView):
    titleDict = {
        'timeEstimatedList': "任务预期时长分布柱状图",
        'taskFinishmentList': "任务完成数量分布柱状图",
        'taskImportanceList': "任务优先级分布柱状图",
        'taskTimeDistributeInOneDay': "任务数量随时段分布柱状图",
        'taskFinishRateInOneDay': "任务完成率随时段分布柱状图"
    }

    nameDict = {
        'timeEstimatedList': "任务数量",
        'taskFinishmentList': "任务完成数量",
        'taskImportanceList': "任务数量",
        'taskTimeDistributeInOneDay': "任务数量",
        'taskFinishRateInOneDay': "任务完成率"
    }

    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self._chart = QChart()
        self._chart.setBackgroundVisible(False)
        # self.initChart()

    def mouseMoveEvent(self, event):
        super(ChartView, self).mouseMoveEvent(event)
        pos = event.pos()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round(x)
        # 得到在坐标系中的所有bar的类型和点
        series = self._chart.series()[0]
        bars = [(bar, bar.at(index))
                for bar in series.barSets() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        #         print(bars)
        if bars:
            right_top = self._chart.mapToPosition(
                QPointF(self.max_x, self.max_y))
            # 等分距离比例
            step_x = round(
                (right_top.x() - self.point_top.x()) / self.category_len)
            posx = self._chart.mapToPosition(QPointF(x, self.min_y))
            self.lineItem.setLine(posx.x(), self.point_top.y(),
                                  posx.x(), posx.y())
            self.lineItem.show()
            try:
                title = self.categories[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            x = int(x)
            y = int(y)
            self.toolTipWidget.show(
                title, bars, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        # bar透明度
        brush = bar.brush()
        color = brush.color()
        alpha = 0.0 if color.alphaF() == 1.0 else 1.0
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar.setBrush(brush)
        # marker
        brush = marker.labelBrush()
        color = brush.color()
        alpha = 0.4 if color.alphaF() == 1.0 else 1.0
        # 设置label的透明度
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker的透明度
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

    def handleMarkerHovered(self, status):
        # 设置bar的画笔宽度
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def handleBarHoverd(self, status, index):
        # 设置bar的画笔宽度
        bar = self.sender()  # 信号发送者
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def initChart(self, dict_keyname, chart_list):
        self._chart.setTitle(self.titleDict[dict_keyname])
        self._chart.setAcceptHoverEvents(True)
        self._chart.removeAllSeries()
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = self.createCategories(dict_keyname, chart_list)
        names = [self.nameDict[dict_keyname]]
        series = QBarSeries(self._chart)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        #self._chart.setLabelFont(font)
        self._chart.setTitleFont(font)
        for name in names:
            bar = QBarSet(name)
            # 填充数据
            for item in chart_list:
                bar.append(item[1])
            series.append(bar)
            bar.hovered.connect(self.handleBarHoverd)  # 鼠标悬停
        self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        # x轴
        axis_x = QBarCategoryAxis(self._chart)
        axis_x.append(self.categories)
        axis_x.setLabelsFont(QFont("微软雅黑",8))
        self._chart.setAxisX(axis_x, series)

        # chart的图例
        legend = self._chart.legend()
        legend.setFont(QFont("微软雅黑",8))
        legend.setVisible(True)
        # 遍历图例上的标记并绑定信号
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.handleMarkerClicked)
            # 鼠标悬停事件
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)

        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # line 宽度需要调整
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()

        self.category_len = len(axisX.categories())
        self.min_x, self.max_x = -1, self.category_len - 1
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))

    def createCategories(self, dict_keyname, chart_list):
        new_list = []
        if dict_keyname == 'taskTimeDistributeInOneDay' \
                or dict_keyname == 'taskFinishRateInOneDay' \
                or dict_keyname == 'timeEstimatedList':
            cur_x = "0-" + str(chart_list[0][0]) + "h"
            new_list.append(cur_x)
            for i in range(1, len(chart_list)):
                cur_x = str(chart_list[i - 1][0]) + "-" + str(chart_list[i][0]) + "h"
                new_list.append(cur_x)
            return new_list
        elif dict_keyname == 'taskImportanceList':
            new_list = ["不重要", "一般", "重要", "非常重要"]
            return new_list

    def setTheme(self, theme):
        self._chart.setTheme(theme)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = ChartView()
    view.initChart('taskTimeDistributeInOneDay', [(3, 1), (6, 7), (9, 3)])
    view.show()
    sys.exit(app.exec_())
