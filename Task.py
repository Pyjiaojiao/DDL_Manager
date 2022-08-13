import datetime


class Task(object):
    def __init__(self, name, time_estimated: datetime.datetime, ddl: datetime.date, detail, type: str,
                 start_date: datetime.date, status: int, priority=0, is_daily=0):
        self.name = name
        # 仅供demo用，实际可能采用str格式的时间
        # if type(time_estimated) != int:
        #     time = int(time_estimated)
        # # 仅供demo用，实际可能采用str格式的日期
        # if type(ddl) != int:
        #     ddl = int(ddl)
        self.time = time_estimated  # 总时间   注意基准为1900-01-01 00:00:00
        self.remaining_time = time_estimated  # 尚未安排时间  同上
        self.ddl = ddl
        self.priority = priority
        self.is_daily = is_daily
        self.detail = detail
        self.start_date = start_date
        self.type = type
        self.status = status
