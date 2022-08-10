"""
这个包实现 数据库记录 与 调度所需类 之间的双向转换
"""
import copy

from Task import Task
from datetime import datetime

_base_datetime = datetime(1900, 1, 1)
print(_base_datetime)


def _record2ongoing_task(rcd) -> Task:
    ddl_date = datetime.strptime(rcd[5], "%Y-%m-%d").date()
    time_est = datetime.strptime(rcd[3], "%Y-%m-%d %H:%M:%S")  # 基准值1900-1-1 00:00:00
    return Task(name=rcd[0], is_daily=rcd[1], priority=rcd[2],
                time_estimated=time_est, ddl=ddl_date, detail=rcd[6])


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
