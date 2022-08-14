"""
这个包实现 数据库记录 与 调度所需类 之间的双向转换
"""
import copy

from Task import Task
from datetime import datetime, date
from PyQt5.QtCore import QDateTime, QDate

_base_datetime = datetime(1900, 1, 1)
# print(_base_datetime)


def _record2ongoing_task(rcd) -> Task:
    ddl_date = datetime.strptime(rcd[5], "%Y-%m-%d").date()
    time_est = datetime.strptime(rcd[3], "%Y-%m-%d %H:%M:%S")  # 基准值1900-1-1 00:00:00
    start_date = datetime.strptime(rcd[8], "%Y-%m-%d").date()
    return Task(name=rcd[0], is_daily=rcd[1], priority=rcd[2], time_estimated=time_est, ddl=ddl_date, detail=rcd[6],
                type=rcd[7], start_date=start_date, status=int(rcd[9]))


def record2ongoing_task_dict(rcd) -> dict:
    ret_dict = {'name': rcd[0],
                'isDaily': True if rcd[1] else False,
                'importance': int(rcd[2]),
                'time_estimated': datetime_str2QDateTime(rcd[3]),
                'time_abd': datetime_str2QDateTime(rcd[4]),
                'endDate': date_str2QDateTime(rcd[5]).date(),  # ddl是某一天
                'detail': rcd[6],
                'type': rcd[7],
                'startDate': date_str2QDateTime(rcd[8]).date(),  # 这是用户输入的开始日期
                'status': int(rcd[9])}  # 因为是从ongoing_task表中找的，所以肯定是正在进行(0) 由于需求变化，前面那句作废
    return ret_dict


def records2ongoing_task_dicts(rcd_list) -> 'dict list':
    dict_list = []
    for rcd in rcd_list:
        task_dict = record2ongoing_task_dict(rcd)
        dict_list.append(task_dict)
    return dict_list


def records2ongoing_tasks(rcd_list) -> list:
    task_list = []
    for item in rcd_list:
        task = _record2ongoing_task(item)
        task_list.append(task)
    return task_list


def records2ongoing_tasks_dict(rcd_list) -> dict:
    task_list = records2ongoing_tasks(rcd_list)
    keys_list = [task.name for task in task_list]
    key_task_zip = zip(keys_list, task_list)
    return dict(key_task_zip)


def subtask_record_and_task_dict2subtask_dict(rcd, task_dict) -> dict:
    task_dict['date'] = date_str2QDate(rcd[0])
    task_dict['startTime'] = datetime_str2QDateTime(rcd[1])
    task_dict['endTime'] = datetime_str2QDateTime(rcd[2])
    return task_dict


# 前端注意，生成的子任务都是由同一个master_task浅克隆的，只有date, start_time和end_time是独立的
def records2subtask_list(master_task, subtask_rcd_list: list) -> list:
    ret = []
    for rcd in subtask_rcd_list:
        subtask = copy.copy(master_task)
        subtask.date = datetime.strptime(rcd[0], "%Y-%m-%d").date()
        subtask.start_time = datetime.strptime(rcd[1], "%H:%M:%S").time()
        subtask.end_time = datetime.strptime(rcd[2], "%H:%M:%S").time()
        ret.append(subtask)
    return ret


# 调度生成的子任务 转为 3关键字+status (4关键字) 的记录
def subtask2record(subtask: Task, subtask_status: int) -> list:
    ret = [subtask.date, subtask.start_time, subtask.end_time, subtask_status]
    return ret


def QDateTime2datetime(qdt: QDateTime) -> datetime:
    qdt_str = qdt.toString("yyyy-MM-dd hh:mm")
    return datetime.strptime(qdt_str, "%Y-%m-%d %H:%M")


def QDate2date(qd: QDate) -> date:
    qd_str = qd.toString("yyyy-MM-dd")
    return datetime.strptime(qd_str, "%Y-%m-%d").date()


def datetime_str2QDateTime(dt_str: 'datetime_str') -> QDateTime:
    return QDateTime.fromString(dt_str, "yyyy-MM-dd hh:mm:ss")


def datetime_str2datetime(dt_str: 'datetime str') -> datetime:
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")


def date_str2QDateTime(d_str: 'date_str') -> QDateTime:
    return QDateTime.fromString(d_str, "yyyy-MM-dd")


def date_str2QDate(d_str: 'date_str') -> QDate:
    return date_str2QDateTime(d_str).date()
