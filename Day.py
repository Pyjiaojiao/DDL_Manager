import datetime
import Task
import my_data_base
import my_data_converter
import random


class Day(object):
    # valid_time 即 可工作时长
    TIME_ZERO = datetime.datetime.strptime("00:00:00", "%H:%M:%S")  # datetime基准值 1900-01-01 00:00:00

    def __init__(self, valid_time: datetime.time, date: datetime.date,
                 beginning_time: datetime.time = datetime.time(8, 0, 0)):
        self.valid_time = self.available_time = valid_time
        self.task_list = []
        self.date = date
        self.beginning_time = beginning_time

    def update_available_time(self, task):
        self.available_time = self.time_sub(self.available_time, task.time)

    def add_task(self, task):
        self.task_list.append(task)
        Day.update_available_time(self, task)

    @staticmethod
    def time_add(time1: datetime.time, time2: datetime.time) -> datetime.time:
        tmp_datetime1 = datetime.datetime.strptime(str(time1), "%H:%M:%S")
        tmp_timedelta = datetime.timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
        return (tmp_datetime1 + tmp_timedelta).time()

    @staticmethod
    def time_sub(time1: datetime.time, time2: datetime.time) -> datetime.time:
        tmp_datetime1 = datetime.datetime.strptime(str(time1), "%H:%M:%S")
        tmp_datetime2 = datetime.datetime.strptime(str(time2), "%H:%M:%S")
        tmp_timedelta = tmp_datetime1 - tmp_datetime2
        return (Day.TIME_ZERO + tmp_timedelta).time()

    @staticmethod
    def datetime_sub_time(dt: datetime.datetime, time: datetime.time) -> datetime.datetime:
        tmp_datetime = datetime.datetime.strptime(str(time), "%H:%M:%S")
        # print("dt", dt, "tmp_datetime", tmp_datetime)
        tmp_timedelta = dt - tmp_datetime
        # print("tmp_timedelta", tmp_timedelta, "dt-timedelta", dt - tmp_timedelta)
        return Day.TIME_ZERO + tmp_timedelta

    @staticmethod
    def datetime_add_time(dt: datetime.datetime, time: datetime.time) -> datetime.datetime:
        tmp_timedelta = datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
        return dt + tmp_timedelta

    # 重新洗牌当天任务序列
    # TODO: 随机填充数轴（24h） 更新：难度过高做不了
    def random_shuffle(self):
        random.shuffle(self.task_list)
        # 顺序填充数轴
        # pseudo code
        self.task_list.sort(key=lambda e: (- e.priority))  # 优先级高的任务放前面。sort是稳定排序，不影响shuffle的效果。
        i = datetime.datetime.strptime(str(self.date) + ' ' + str(self.beginning_time), "%Y-%m-%d %H:%M:%S")
        for task in self.task_list:
            task.date = self.date
            task.start_time = i
            task.end_time = Day.datetime_add_time(i, task.time)
            i = task.end_time  # TODO: 留出休息时间

    @staticmethod
    def save_all2db(day_list, usr_id):
        d = {}
        for day in day_list:
            for task in day.task_list:
                if task.name not in d:
                    d[task.name] = []
                # 将该subtask转为用于任务调度table的记录
                d[task.name].append(my_data_converter.subtask2record(task, 0))  # 0 means 未开始
        # print('-' * 10)
        # print("task_arrange result before storing")
        for task_name in d:
            # print(d[task_name])
            my_data_base.save_task_schedule_list2name_table(usr_id=usr_id, task_name=task_name,
                                                            schedule_list=d[task_name])
