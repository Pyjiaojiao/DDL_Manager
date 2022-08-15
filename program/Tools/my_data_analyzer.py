"""
专注于数据分析的数据库
"""
import my_data_base
import my_data_converter
import datetime
import sqlite3
from PyQt5.QtCore import QDateTime, QDate
import bisect

TASK_STATUS_CODE = {'not_start': 0, 'doing': 1, 'finish': 2, 'time_out': 3,
                    'delete': 4}  # dict{op_str: int} 0 未开始 1 正在做 2 完成 3 过期 4 删除

HOUR_STEP_TE = 4
HOUR_STEPS_TE = [x for x in range(0, 24, HOUR_STEP_TE)]  # timeEstimatedList hour步长为4

HOUR_STEP_DS = 3
HOUR_STEPS_DS = [x for x in range(0, 24, HOUR_STEP_DS)]  # subtask distribute hour步长为3


# 提供给base_op的接口，供base_op构造好检索表达式后获取分析结果
def get_analyze_result(usr_id: str, specify: dict) -> dict:
    ret_dict = ret_dict_init()  # 放前端需要的返回值
    analyze_ongoing_tasks(usr_id, specify, ret_dict)
    ret_dict_reorganize(ret_dict)
    return ret_dict


# key ret字典的key  index_list key对应的ret元组列表应该具有的索引
def dict2list(ret: dict, key: str, index_list: list):
    if type(ret[key]) == list:
        return
    new_list = []
    for x in index_list:
        val = ret[key][x] if x in ret[key] else 0
        new_list.append((x, val))
    ret[key] = new_list


# 更新带有hour step的结构
def dict2list_with_hour_steps(ret: dict, key: str, hour_steps: list, hour_step: int):
    if type(ret[key]) == list:
        return
    new_lst = []
    for x in hour_steps:
        val = ret[key][x] if x in ret[key] else 0
        new_lst.append((x + hour_step, val))
    ret[key] = new_lst


def ret_dict_reorganize(ret: dict):
    ret['curTaskFinishRate'] = ret['curTaskFinishCount'] / ret['curTaskCount']
    dict2list_with_hour_steps(ret, 'timeEstimatedList', HOUR_STEPS_TE, HOUR_STEP_TE)
    # 在更新接下来要更新的结构前，先利用之做计算
    for key in ret['taskTimeDistributeInOneDay']:
        if key not in ret['taskFinishCountInOneDay']:
            ret['taskFinishRateInOneDay'][key] = 0
        else:
            ret['taskFinishRateInOneDay'][key] = \
                ret['taskFinishCountInOneDay'][key] / ret['taskTimeDistributeInOneDay'][key]
    dict2list_with_hour_steps(ret, 'taskTimeDistributeInOneDay', HOUR_STEPS_DS, HOUR_STEP_DS)
    dict2list_with_hour_steps(ret, 'taskFinishCountInOneDay', HOUR_STEPS_DS, HOUR_STEP_DS)
    dict2list_with_hour_steps(ret, 'taskFinishRateInOneDay', HOUR_STEPS_DS, HOUR_STEP_DS)
    dict2list(ret, 'taskFinishmentList', [True, False])
    dict2list(ret, 'taskImportanceList', [0, 1, 2, 3])
    dict2list(ret, 'taskStatusList', [0, 1, 2, 3])
    dict2list(ret, 'taskTypeList', ['学习', '运动', '娱乐', '工作', '其他'])


# 改: 凡列表含元组的，统统改成列表含字典。元组操作真的反人类。字典转元组放最后，转完记得排序。
def ret_dict_init() -> dict:
    ret = {
        'startDate': QDate(1970, 1, 1),  # QDateTime
        'endDate': QDate(2050, 1, 1),  # QDateTime 指定查询的开始和截止日期（只考虑日期，不计小时分钟）
        # # 以下字段均针对“所有时间”
        # 'totalOriginTaskCount': 0,
        # 'totalTaskCount': 0,
        # 'totalTaskFinishRate': 0,
        # 以下字段均针对“指定的startDate和endDate之间”
        'curOriginTaskCount': 0,
        'curTaskCount': 0,
        'curTaskFinishCount': 0,
        'curTaskFinishRate': 0,
        'timeEstimatedList': {},
        'taskTypeList': {},
        'taskStatusList': {},
        'taskImportanceList': {},
        'taskFinishmentList': {},
        'taskTimeDistributeInOneDay': {},
        'taskFinishRateInOneDay': {},
        'taskFinishCountInOneDay':{}
    }
    return ret


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
        ret['curOriginTaskCount'] += 1
        task_type = rcd[7]
        ret['taskTypeList'][task_type] = 1 \
            if task_type not in ret['taskTypeList'] else 1 + ret['taskTypeList'][task_type]
        task_status = int(rcd[9])
        ret['taskStatusList'][task_status] = 1 \
            if task_status not in ret['taskStatusList'] else 1 + ret['taskStatusList'][task_status]
        task_importance = int(rcd[2])
        ret['taskImportanceList'][task_importance] = 1 \
            if task_importance not in ret['taskImportanceList'] else 1 + ret['taskImportanceList'][task_importance]
        if task_status == TASK_STATUS_CODE['finish']:
            ret['taskFinishmentList'][True] = 1 if True not in ret['taskFinishmentList'] else 1 + ret[
                'taskFinishmentList']
        elif task_status == TASK_STATUS_CODE['time_out']:
            ret['taskFinishmentList'][False] = 1 if False not in ret['taskFinishmentList'] else 1 + ret[
                'taskFinishmentList']
        task_estimated = my_data_converter.datetime_str2datetime(rcd[3])
        index = _get_first_index_ge(HOUR_STEPS_TE, task_estimated.hour) - 1
        # index = bisect.bisect_right(HOUR_STEPS_TE, task_estimated.hour) - 1
        hour_key = HOUR_STEPS_TE[index]
        ret['timeEstimatedList'][hour_key] = 1 \
            if hour_key not in ret['timeEstimatedList'] else 1 + ret['timeEstimatedList'][hour_key]
        analyze_subtasks(usr_id, task_name, specify, ret)


def _get_first_index_ge(li: list, val: int) -> int:
    return bisect.bisect_right(li, val) - 1


def analyze_subtasks(usr_id: str, task_name: str, specify: dict, ret: dict):
    subtask_rcds = my_data_base.get_subtask_rcds(usr_id, task_name)
    for rcd in subtask_rcds:
        subtask_end_date = subtask_start_date = my_data_converter.date_str2date(rcd[0])
        if not date_ranges_intersect((subtask_start_date, subtask_end_date),
                                     (specify['start_date'], specify['end_date'])):
            continue
        ret['curTaskCount'] += 1
        subtask_status = int(rcd[3])
        ret['curTaskFinishCount'] += 1 if subtask_status == TASK_STATUS_CODE['finish'] else 0
        start_time = my_data_converter.datetime_str2datetime(rcd[1])
        end_time = my_data_converter.datetime_str2datetime(rcd[2])
        left_index = _get_first_index_ge(HOUR_STEPS_DS, start_time.hour)
        right_index = _get_first_index_ge(HOUR_STEPS_DS, end_time.hour)
        for i in range(left_index, right_index + 1):
            hour_key = HOUR_STEPS_DS[i]
            ret['taskTimeDistributeInOneDay'][hour_key] = 1 \
                if hour_key not in ret['taskTimeDistributeInOneDay'] else 1 + ret['taskTimeDistributeInOneDay'][
                hour_key]
            if subtask_status == TASK_STATUS_CODE['finish']:
                # 'taskFinishCountInOneDay' 是额外增加的字段
                ret['taskFinishCountInOneDay'][hour_key] = 1 \
                    if hour_key not in ret['taskFinishCountInOneDay'] else 1 + ret['taskFinishCountInOneDay'][hour_key]
