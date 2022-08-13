"""
任务调度
"""
from Day import Day
import copy
import random
import bisect
import datetime
import my_data_base
import my_data_converter

# DAY_FROM = QDateTime.currentDateTime()  # year-month-day
# DAY_END = DAY_FROM.addDays(31)
# print(DAY_END.daysTo(DAY_FROM))


# print(DAY_FROM.date().day())
DAY_FROM = datetime.date.today() + datetime.timedelta(days=1)  # 开始日期
DAY_END = DAY_FROM + datetime.timedelta(days=31)  # 最后日期，左闭右开


# 提供一个迭代器, 输入 (dateTime.datetime, dateTime.datetime), 返回dateTime.datetime。左闭右开
def date_range(start, end):
    delta_int = (end - start).days
    print(delta_int, type(delta_int))
    for i in range(delta_int):
        # yield start.addDays(i)    for QDateTime
        yield start + datetime.timedelta(days=i)


# test
# for i in date_range(DAY_FROM, DAY_END):
#     # print(i.date().day())
#     print(i)

MAX_AVAILABLE_DTIME = datetime.time(9, 0, 0)  # 一天最大可用时间
MAX_CONTINUOUS_WORKING_TIME = datetime.time(2, 0, 0)  # 最大连续工作时间

TIMETABLE = {}  # 日程表
AVAILABLE_TIMETABLE = []  # 仅存放可用日期date，用于二分查找可用日期
TASKS = []


# 返回两个datetime或date中较小的
def datetime_min(a: datetime, b: datetime) -> datetime:
    return a if a <= b else b


def datetime_max(a: datetime, b: datetime) -> datetime:
    return b if a <= b else a


def task_sort(task_list):
    task_list.sort(key=lambda e: (not e.is_daily, - e.priority, e.ddl))
    # 安排任务时，排序优先级: 日常 > 优先级 > ddl


# a demo
def task_init(usr_id=None):
    # print("input the task number:...")
    # n = int(input())
    # print("input %d TASKS,\n format: name-time-ddl" % n)
    global TASKS
    tasks_rcd = my_data_base.get_ongoing_tasks_rcds(usr_id)
    TASKS = my_data_converter.records2ongoing_tasks(tasks_rcd)
    # for i in range(n):
    #     task_key_attrs = tuple(input().split('-'))
    #     print(task_key_attrs)
    #     task = Task(*task_key_attrs)
    #     TASKS.append(task)
    task_sort(TASKS)
    print("schedule.py line 69")
    for task in TASKS:
        print(task.__dict__)


def timetable_init():
    global AVAILABLE_TIMETABLE
    # TODO: 根据不可用天或不可用时间定制
    for i in date_range(DAY_FROM, DAY_END):
        AVAILABLE_TIMETABLE.append(i)
        TIMETABLE[i] = Day(MAX_AVAILABLE_DTIME, i)


# 初始化日程表：将每天可用空闲时间置为 可工作时间（非睡眠时间 - sum不能工作时间）
def _init(usr_id=None):
    global TIMETABLE, MAX_CONTINUOUS_WORKING_TIME, AVAILABLE_TIMETABLE, TASKS
    TIMETABLE = {}  # 日程表
    AVAILABLE_TIMETABLE = []  # 仅存放可用日期序号，用于二分查找可用日期
    TASKS = []
    MAX_CONTINUOUS_WORKING_TIME = my_data_base.get_max_continuous_working_time(usr_id)
    global DAY_FROM, DAY_END
    DAY_FROM = datetime.date.today() + datetime.timedelta(days=1)  # 开始日期 TODO: 根据情况改成从当天开始
    DAY_END = DAY_FROM + datetime.timedelta(days=31)  # 最后日期，左闭右开
    print("max continuous working time inited: %s..." % MAX_CONTINUOUS_WORKING_TIME)
    # 初始化TASKS列表
    task_init(usr_id=usr_id)
    # 初始化“空闲天序列” 和 “日程表”
    timetable_init()
    my_data_base.clear_scheduled_subtasks(usr_id)
    pass  # 待填充扣减ban掉的时间


# 根据传入起止时期，选择一个可用天
# return 可用天的key
def select_a_day(day_from, day_to):
    day_from_index = bisect.bisect_left(AVAILABLE_TIMETABLE, day_from)
    day_to_index = bisect.bisect_right(AVAILABLE_TIMETABLE, day_to, lo=day_from_index)
    print("day_from_index", day_from_index, "day_to_index", day_to_index)
    rand_day_key = random.randint(day_from_index, day_to_index - 1)
    return AVAILABLE_TIMETABLE[rand_day_key]


cnt = 0


def _get_sub_task_from_task(task, part_time: datetime.time):
    task_part = copy.copy(task)  # shallow copy
    task_part.time = task_part.remaining_time = part_time
    return task_part


# 将一个任务单元安排到某一天
def task_part_fill(time_table, task, selected_day_key=None):
    # 选择一个可用天
    if selected_day_key is None:
        print(DAY_FROM, task.start_date, DAY_END, task.ddl)
        selected_day_key = select_a_day(datetime_max(DAY_FROM, task.start_date), datetime_min(DAY_END, task.ddl))
    selected_day = TIMETABLE[selected_day_key]
    # 求应安排时间
    print(selected_day.available_time, type(selected_day.available_time), "type selected_day.available_time")
    part_time = min(MAX_CONTINUOUS_WORKING_TIME, task.remaining_time.time())  # 这次安排部分 的时间
    print("type part_time", type(part_time), part_time)
    part_time = min(part_time, selected_day.available_time)
    # 调试用。只要其他地方没问题，这里也不会有问题。
    global cnt
    print("cnt: %d" % cnt)
    cnt += 1
    # 原则上不可能，因为没有比TIME_ZERO更小的时间了
    if selected_day.available_time <= Day.TIME_ZERO.time():
        raise Exception("选到了一个无可用时间的天！")
    # 新建一个部分任务，添加进选中的天中
    # 该方法会自动更新天剩余可用时间
    # task_part = Task(task.name, part_time, task.ddl)
    task_part = _get_sub_task_from_task(task, part_time)
    selected_day.add_task(task_part)
    # 更新任务未安排时间
    task.remaining_time = Day.datetime_sub_time(task.remaining_time, part_time)
    selected_day.available_time = Day.time_sub(selected_day.available_time, part_time)
    # 从“可用天key列表”中移除不再可用的天
    if selected_day.available_time == Day.TIME_ZERO.time():
        AVAILABLE_TIMETABLE.remove(selected_day_key)


# 重新安排所有任务
def task_arrange(usr_id):
    _init(usr_id=usr_id)
    # 将所有任务分别分解，并插入到合理的天中
    # 如果出现有任务出现在ddl之后的天，说明已经无法再提前了。
    for task in TASKS:
        if task.is_daily:
            # 在日期范围内的每一天为该日常任务安排时间
            for date in date_range(datetime_max(DAY_FROM, task.start_date),
                                   datetime_min(DAY_END, task.ddl) + datetime.timedelta(days=1)):
                while task.remaining_time > Day.TIME_ZERO:
                    task_part_fill(TIMETABLE, task, date)
                task.remaining_time = task.time  # 日常任务每过一天，剩余时间应该重置
        else:
            while task.remaining_time > Day.TIME_ZERO:
                task_part_fill(TIMETABLE, task)
    # 为每一个有任务的天随机排列任务
    for key, day in TIMETABLE.items():
        day.random_shuffle()
    print("TIMETABLE_VALUES type is ", type(TIMETABLE.values()))
    Day.save_all2db(TIMETABLE.values(), usr_id)

# def debug():
#     _init()
#     task_arrange()
#     # """
#     for key, day in TIMETABLE.items():
#         print(day.task_list)
#         if day.task_list:
#             print("day %d: " % key)
#             for i in range(len(day.task_list)):
#                 task = day.task_list[i]
#                 print("\ttask %d: name-%s time-%d ddl-%d" % (i, task.name, task.time, task.ddl))
#     # """
#
#
# debug()
