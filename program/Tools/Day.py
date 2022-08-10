import datetime

import my_data_base


class Day(object):
    # valid_time 即 可工作时长
    def __init__(self, valid_time: datetime.time, date: datetime.date,
                 beginning_time: datetime.time = datetime.time(8, 0, 0)):
        self.valid_time = self.available_time = valid_time
        self.task_list = []
        self.date = date
        self.beginning_time = beginning_time

    def update_available_time(self, task):
        self.available_time -= task.time

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
        return (tmp_datetime1 + tmp_timedelta).time()

    # 重新洗牌当天任务序列
    # TODO: 随机填充数轴（24h）
    def random_shuffle(self):
        random.shuffle(self.task_list)
        # 顺序填充数轴
        # pseudo code
        i = self.beginning_time
        for task in self.task_list:
            task.date = self.date
            task.start_time = i
            task.end_time = Day.time_add(i, task.time)

    @staticmethod
    def save_all2db(day_list):
        d = {}
        for day in day_list:
            for task in day.task_list:
                if task.name not in d:
                    d[task.name] = []
                d[task.name].append(task)
        for task_name in d:
            my_data_base.save_task_schedule_list2name_table(task_name=task_name, schedule_list=d[task_name])
