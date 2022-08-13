"""
Created on 2018年1月30日
@author: Irony."[讽刺]
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: CalendarQssStyle
@description: 日历美化样式
"""
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QFont
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from goEverydayTaskDialog import goEverydayTaskDialog
StyleSheet = '''
/*顶部导航区域*/
#qt_calendar_navigationbar {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #00BCD4,stop:1 #C0FFD7);
    min-height: 80px;
}

/*上一个月按钮和下一个月按钮*/
#qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none; /*去掉边框*/
    margin-top: 64px;
    color: white;
    min-width: 36px;
    max-width: 36px;
    min-height: 36px;
    max-height: 36px;
    border-radius: 18px; /*看来近似椭圆*/
    font-weight: bold; /*字体加粗*/
    qproperty-icon: none; /*去掉默认的方向键图片*/
    background-color: transparent;/*背景颜色透明*/
}
#qt_calendar_prevmonth {
    qproperty-text: "<"; /*修改按钮的文字*/
}
#qt_calendar_nextmonth {
    qproperty-text: ">";
}
#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}


/*年,月控件*/
#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: white;
    margin: 18px;
    min-width: 60px;
    border-radius: 30px;
    background-color: rgba(240,240,240,100)
}
#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}


/*年份输入框*/
#qt_calendar_yearedit {
    min-width: 50px;
    color: white;
    background: transparent;/*让输入框背景透明*/
}
#qt_calendar_yearedit::up-button { /*往上的按钮*/
    width: 20px;
    subcontrol-position: right;/*移动到右边*/
}
#qt_calendar_yearedit::down-button { /*往下的按钮*/
    width: 20px;
    subcontrol-position: left; /*移动到左边去*/
}


/*月份选择菜单*/
CalendarWidget QToolButton QMenu {
     background-color: white;
}
CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}
CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}
CalendarWidget QToolButton::menu-indicator {
    /*image: none;去掉月份选择下面的小箭头*/
    subcontrol-position: right center;/*右边居中*/
}


/*下方的日历表格*/
#qt_calendar_calendarview {
    outline: 0px;/*去掉选中后的虚线框*/
    selection-background-color: #00D49F; /*选中背景颜色*/
    border-radius: 18px;
}
'''


class CalendarWidget(QCalendarWidget):
    switch1 = QtCore.pyqtSignal(QtCore.QDate)  # 双击触发

    def __init__(self, *args, **kwargs):
        super(CalendarWidget, self).__init__(*args, **kwargs)
        self.resize(1280, 720)
        self.goEverydayTaskDialog = goEverydayTaskDialog()
        # 隐藏左边的序号
        self.setVerticalHeaderFormat(self.NoVerticalHeader)

        # 顶部导航栏文字样式
        fmtTop = QTextCharFormat()
        fmtTop.setFont(QFont("SimHei", 30))
        self.setHeaderTextFormat(fmtTop)

        # 修改周六周日颜色

        fmtGreen = QTextCharFormat()
        fmtGreen.setFont(QFont("Microsoft YaHei", 17))
        fmtGreen.setForeground(QBrush(Qt.green))
        self.setWeekdayTextFormat(Qt.Saturday, fmtGreen)

        fmtOrange = QTextCharFormat()
        fmtOrange.setFont(QFont("Microsoft YaHei", 17))
        fmtOrange.setForeground(QBrush(QColor(252, 140, 28)))
        self.setWeekdayTextFormat(Qt.Sunday, fmtOrange)

        # 修改字体
        wf = QTextCharFormat()
        wf.setFont(QFont("Microsoft YaHei", 17))
        #wf.setFontItalic(True)
        self.setWeekdayTextFormat(Qt.Monday, wf)
        self.setWeekdayTextFormat(Qt.Tuesday, wf)
        self.setWeekdayTextFormat(Qt.Wednesday, wf)
        self.setWeekdayTextFormat(Qt.Thursday, wf)
        self.setWeekdayTextFormat(Qt.Friday, wf)
        self.setStyleSheet(StyleSheet)

        # 双击打开“确认跳转每日任务”弹窗
        self.switch1.connect(self.goQuery)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.switch1.emit(self.selectedDate())

    def goQuery(self, date):
        date = date.toString("yyyy-MM-dd")
        datetime = QtCore.QDate.fromString(date, "yyyy-MM-dd")
        self.goEverydayTaskDialog.updateText(datetime)
        self.goEverydayTaskDialog.show()


    def timeout1(self):
        if self.switch1 == 1:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w = CalendarWidget()
    w.show()
    sys.exit(app.exec_())
