"""
专注于数据分析的数据库
"""
import my_data_base
import my_data_converter
import datetime
import sqlite3
from PyQt5.QtCore import QDateTime


# 提供给base_op的接口，供base_op构造好检索表达式后获取分析结果
def get_analyze_result(usr_id: str, specify: dict) -> dict:
    ret_dict = ret_dict_init()  # 放前端需要的返回值
    analyze_ongoing_tasks(usr_id, specify, ret_dict)

def ret_dict_init() -> dict:
    ret = {}

def date_ranges_intersect(range1: tuple, range2: tuple) -> bool:
    # 整理range1, range2，使之按start_date升序排列
    range1, range2 = sorted([range1, range2], key=lambda e: e[0])
    # 如果start_date晚的range的start_date晚于早的end_date，应返回不相交False
    if range2[0] > range1[1]:
        return False
    return True


# 开始分析原始任务 (均在ONGOING_TASKS表中)
def analyze_ongoing_tasks(usr_id: str, specify: dict, ret: dict):
    # 从ongoing表中获取全部原始任务记录
    all_ongoing_tasks_rcd = my_data_base.get_ongoing_tasks_rcds(usr_id)
    for rcd in all_ongoing_tasks_rcd:
        task_name = rcd[0]
        start_time_str, end_time_str = my_data_base.get_task_startTime_and_endTime(usr_id, task_name)
        # 提取任务起止日期
        if start_time_str and end_time_str:
            task_start_date = my_data_converter.datetime_str2datetime(start_time_str).date()
            task_end_date = my_data_converter.datetime_str2datetime(end_time_str).date()
        else:
            task_start_date = my_data_converter.date_str2date(rcd[8])  # start_date
            task_end_date = my_data_converter.date_str2date(rcd[5])  # ddl
        # 任务起止日期与传入起止日期比较, 不相交的直接跳过
        if not date_ranges_intersect((task_start_date, task_end_date), (specify['start_date'], specify['end_date'])):
            continue

