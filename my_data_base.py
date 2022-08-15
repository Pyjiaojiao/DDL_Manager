"""
数据库读写
"""
import os.path
import pathlib

import Day
import Task
import sqlite3
import datetime
import my_data_converter
from base_op import SUBTASK_STATUS_CODE
from itertools import zip_longest


def db_start(usr_id: str) -> (sqlite3.Connection, sqlite3.Cursor):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id=usr_id))
    curs = conn.cursor()
    return conn, curs


def db_end(conn: sqlite3.Connection, curs: sqlite3.Cursor):
    conn.commit()
    curs.close()
    conn.close()


# 用于将任务字典转换为 ONGOING_TASK table 所需的任务序列
def _task_dict2ongoing_task_info_list(td: dict):
    l = [td['name'], td['is_daily'], td['priority'], td['time_estimated'], td['time_abd'], td['ddl'], td['detail'],
         td['type'], td['start_date'], 0]  # status 先默认为0，随子任务status同步变化即可
    return l


# 用户id转为对应db文件名
def _usr_id2db_filename(usr_id: str):
    path = './usr_data/'
    if not os.path.exists(path):
        os.mkdir(path)
    return path + str(usr_id) + '.db'


# 注册时调用，初始化数据库
def _init_db(usr_id):
    # print('dbname is ' + _usr_id2db_filename(usr_id))
    conn, curs = db_start(usr_id)
    # 所有正在进行的任务 name 均不相同
    tbl_crt = '''
         create table if not exists ONGOING_TASKS(name text, is_daily int, priority int,
         time_estimated datetime, time_abd datetime,
         ddl date, detail text, type text, start_date date, status int)
    '''
    curs.execute(tbl_crt)
    # type 用于标记完成状态：已完成？放弃？
    # 同名项应该被合并
    # detail 以最后一次合并时较新的任务的detail为准
    tbl_crt = '''
         create table if not exists TERMINATED_TASKS
         (name text, time_abd datetime,
         type int, detail text)
    '''
    curs.execute(tbl_crt)
    db_end(conn, curs)


# 新任务保存到db的 ONGOING_TASKS table
def save_new_task2db(usr_id, task_dict):
    conn, curs = db_start(usr_id)
    tbl_ins = '''
        insert into ONGOING_TASKS
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    task_info_list = _task_dict2ongoing_task_info_list(task_dict)
    curs.execute(tbl_ins, task_info_list)
    db_end(conn, curs)


# 从数据库中删除task
def del_task(usr_id, task_name):
    conn, curs = db_start(usr_id)
    curs.execute("select * from ONGOING_TASKS where name = '{task_name}'".format(task_name=task_name))
    ret = curs.fetchall()
    # 正在进行库没有task_name, 去终结库找
    if not ret:
        ret = curs.execute(
            "select * from TERMINATED_TASKS where name = '{task_name}'".format(task_name=task_name)).fetchall()
        if not ret:
            curs.execute("delete from TERMINATED_TASKS where name = '{task_name}'".format(task_name=task_name))
    else:
        curs.execute("drop table '{task_name}'".format(task_name=task_name))
        curs.execute("delete from ONGOING_TASKS where name = '{task_name}'".format(task_name=task_name))
    db_end(conn, curs)


# 将一个任务的调度列表存入数据库，表名为 task_name
# schedule_list 元素为 (date, start_time, end_time), type为 (date, datetime, datetime)
def save_task_schedule_list2name_table(usr_id, task_name, schedule_list):
    conn, curs = db_start(usr_id)
    tbl_drop = 'drop table if exists "{table_name}"'.format(table_name=task_name)
    tbl_crt = '''
        create table if not exists '{table_name}'
        (date date, start_time datetime, end_time datetime, status int)
    '''.format(table_name=task_name)  # status 0 未开始 1 正在进行 （根据时间来定） 2 已完成 3 已过期
    tbl_ins = '''
        insert into '{table_name}'
        values(?, ?, ?, ?)
    '''.format(table_name=task_name)
    curs.execute(tbl_drop)
    curs.execute(tbl_crt)
    curs.executemany(tbl_ins, schedule_list)
    db_end(conn, curs)


def rename_task(usr_id, old_name, new_name):
    conn, curs = db_start(usr_id)
    # 小表改名
    tbl_rnm = 'alter table "{table_old_name}" rename to "{table_new_name}"' \
        .format(table_old_name=old_name, table_new_name=new_name)
    tsk_rnm = 'update ONGOING_TASKS set name=? where name=?'  # 大表，只修改正在发生的任务表，已终结表是历史数据，不能修改
    curs.execute(tbl_rnm)
    name_tuple_new_old = (new_name, old_name)
    curs.execute(tsk_rnm, name_tuple_new_old)
    db_end(conn, curs)


# 用于修改除任务名(id)之外的普通任务属性
def normal_modify(usr_id, task_name, key, new_val):
    conn, curs = db_start(usr_id)
    # if is in ONGOING_TASKS table
    curs.execute(
        "update ONGOING_TASKS set '{key}' = '{new_val}' where name = '{task_name}'".format(key=key, new_val=new_val,
                                                                                           task_name=task_name))
    db_end(conn, curs)


def get_max_continuous_working_time(usr_id: str) -> datetime.time:
    conn, curs = db_start(usr_id)
    # TODO: 从数据库中查找
    db_end(conn, curs)
    return datetime.time(2, 0, 0)  # for test


# 返回全部正在发生的任务, 返回值类型为list[Task record[,...]]
def get_ongoing_tasks_rcds(usr_id: str, specify_str: str = '') -> 'Task records list':
    conn, curs = db_start(usr_id)
    curs.execute('select * from ONGOING_TASKS' + specify_str)
    rcd_list = curs.fetchall()
    db_end(conn, curs)
    return rcd_list


# 返回某一任务的全部subtask
def get_subtask_rcds(usr_id: str, task_name: str) -> list:
    conn, curs = db_start(usr_id)
    curs.execute(
        '''create table if not exists "{table_name}"
        (date date, start_time datetime, end_time datetime, status int)'''.format(table_name=task_name))
    curs.execute('select * from "{task_name}"'.format(task_name=task_name))
    ret = curs.fetchall()
    db_end(conn, curs)
    return ret

# clear现在不会清除已完成的任务，且不会清除已过期和已完成的日常任务
def clear_scheduled_subtasks(usr_id):
    conn, curs = db_start(usr_id)
    ongoing_tasks_rcds = get_ongoing_tasks_rcds(usr_id)
    for row in ongoing_tasks_rcds:
        task_name = row[0]
        is_daily = row[1]
        if not is_daily:
            # curs.execute('drop table if exists {table_name}'.format(table_name=task_name))
            curs.execute(
                '''create table if not exists "{table_name}"
                (date date, start_time datetime, end_time datetime, status int)'''.format(table_name=task_name))
            curs.execute('delete from "{table_name}" where status != "{finish_code}"'.
                         format(table_name=task_name, finish_code=SUBTASK_STATUS_CODE['finish']))
        else:
            curs.execute('delete from "{table_name}" where status != "{finish_code}" and status != "{time_out_code}"'
                         .format(table_name=task_name, finish_code=SUBTASK_STATUS_CODE['finish'],
                                 time_out_code=SUBTASK_STATUS_CODE['time_out']))
    db_end(conn, curs)


# 返回所有被调度进行的子任务，返回值类型为Task list
def get_all_ongoing_subtasks(usr_id: str) -> 'Task list':
    ongoing_task_rcd_list = get_ongoing_tasks_rcds(usr_id)
    # name-task dict for ongoing tasks
    task_dict = my_data_converter.records2ongoing_tasks_dict(ongoing_task_rcd_list)
    ret = []
    conn, curs = db_start(usr_id)
    for row in ongoing_task_rcd_list:
        task_name = row[0]
        curs.execute('select * from "{task_name}"'.format(task_name=task_name))
        subtasks_rcd_list = curs.fetchall()
        subtasks_list = my_data_converter.records2subtask_list(task_dict[task_name], subtasks_rcd_list)
        ret.extend(subtasks_list)
    db_end(conn, curs)
    return ret


# 返回满足特定检索条件的被调度子任务序列。返回值类型为list[records]
# 更新：返回值为list[Task]，其中，在输入任务所具有的属性外，增加了date, start_time, end_time属性用于前端展示
# specify_str 为 where ...
def get_specified_subtasks(usr_id: str, specify_str_4task: str, specify_str_4subtask: str) -> list:
    # 查找符合 限制条件的 ONGOING_TASK
    ongoing_task_rcd_list = get_ongoing_tasks_rcds(usr_id, specify_str=specify_str_4task)
    conn, curs = db_start(usr_id)
    ret = []
    for row in ongoing_task_rcd_list:
        task_name = row[0]
        tbl_slct = 'select * from "{table_name}"'.format(table_name=task_name) + specify_str_4subtask
        # print(tbl_slct)
        curs.execute(tbl_slct)
        # subtasks_rcd_list = []
        for row1 in curs.fetchall():
            task_dict = my_data_converter.record2ongoing_task_dict(row)
            task_dict = my_data_converter.subtask_record_and_task_dict2subtask_dict(row1, task_dict)
            # subtask_rcd_item = [task_name, row1]
            # subtasks_rcd_list.append(subtask_rcd_item)
            ret.append(task_dict)
    db_end(conn, curs)
    ret.sort(key=lambda e: e['startTime'])  # 小任务按开始时间排序
    return ret


def terminate_subtask(usr_id: str, task_name: str, task_start_time: datetime, terminate_code: int):
    conn, curs = db_start(usr_id)
    # 获取子任务持续时间
    curs.execute('select * from "{task_name}" where start_time = "{start_time}"'.format(task_name=task_name,
                                                                                        start_time=task_start_time))
    subtask_rcd = curs.fetchone()
    task_end_time = my_data_converter.datetime_str2datetime(subtask_rcd[2])
    task_timedelta = task_end_time - task_start_time  # 该子任务的持续时间
    # 如果是完成任务操作
    if terminate_code == SUBTASK_STATUS_CODE['finish']:
        # 先更新原始任务time_abd
        curs.execute('select * from ONGOING_TASKS where name = "{task_name}"'.format(task_name=task_name))
        task_rcd = curs.fetchone()
        task_abd = my_data_converter.datetime_str2datetime(task_rcd[4])  # 该子任务对应的总任务的已完成时间
        task_abd += task_timedelta
        curs.execute(
            'update ONGOING_TASKS set time_abd = "{task_abd}" where name = "{task_name}"'.format(task_abd=task_abd,
                                                                                                 task_name=task_name))
        # 再把子任务状态设置为已完成
        curs.execute(
            'update "{task_name}" set status = "{status}" where start_time = "{start_time}"'.format(task_name=task_name,
                                                                                                    status=
                                                                                                    SUBTASK_STATUS_CODE[
                                                                                                        'finish'],
                                                                                                    start_time=task_start_time))
        # TODO: 根据数据分析要求，更新历史记录表
    # 如果是删除任务操作
    elif terminate_code == SUBTASK_STATUS_CODE['delete']:
        # 原任务 time_estimated 减去 该子任务持续时间
        curs.execute('select * from ONGOING_TASKS where name="{task_name}"'.format(task_name=task_name))
        task_rcd = curs.fetchone()
        task_estimated = my_data_converter.datetime_str2datetime(task_rcd[3])
        task_estimated -= task_timedelta
        # 直接移除任务
        curs.execute('delete from "{task_name}" where start_time = "{start_time}"'.format(task_name=task_name,
                                                                                          start_time=task_start_time))
        # TODO: 根据数据分析要求，更新历史记录表
    db_end(conn, curs)


# 结束一个原始任务，terminate_code应为 已完成code 或 已过期code 或 删除code
# TODO: 根据数据分析要求，更新历史记录表
def terminate_task(usr_id: str, task_name: str, terminate_code: int):
    conn, curs = db_start(usr_id)
    if terminate_code != SUBTASK_STATUS_CODE['delete']:
        curs.execute(
            'update ONGOING_TASKS set status = "{status}" where name = "{task_name}"'.format(status=terminate_code,
                                                                                             task_name=task_name))
    else:
        curs.execute('delete from ONGOING_TASKS where name = "{task_name}"'.format(task_name=task_name))
        curs.execute('drop table "{task_name}"'.format(task_name=task_name))
    db_end(conn, curs)


# 利用计组数电知识更新状态表。precondition：子任务表非空
def _update_ongoing_task_status_logic(usr_id: str, task_name):
    conn, curs = db_start(usr_id)
    tbl_slct = 'select * from "{task_name}" where status = "{status}"'.format(task_name=task_name, status="{status}")
    curs.execute(tbl_slct.format(status=SUBTASK_STATUS_CODE['not_start']))
    A = not _is_curs_empty(curs)  # not_start
    curs.execute(tbl_slct.format(status=SUBTASK_STATUS_CODE['doing']))
    B = not _is_curs_empty(curs)  # doing
    curs.execute(tbl_slct.format(status=SUBTASK_STATUS_CODE['time_out']))
    C = not _is_curs_empty(curs)  # time_out
    curs.execute(tbl_slct.format(status=SUBTASK_STATUS_CODE['finish']))
    D = not _is_curs_empty(curs)  # finish
    big_task_status_E = (C or D) and (not B) and (not A)
    big_task_status_F = C or B or (A and D)
    status_d_int = big_task_status_E * 2 + big_task_status_F
    tbl_upd = 'update ONGOING_TASKS set status = "{new_status}" where name = "{task_name}"'.format(
        new_status=status_d_int, task_name=task_name)
    # print("tbl_upd", tbl_upd)
    curs.execute(tbl_upd)
    db_end(conn, curs)
    # TODO: 把ONGOING_TASKS中已完成和已过期的任务移到TERMINATED_TASKS中，同时根据数据分析要求相应做变更


def _is_subtask_table_empty(usr_id: str, task_name: str) -> bool:
    conn, curs = db_start(usr_id)
    # 先尝试创建表，以免找不到表 报错
    curs.execute(
        f'create table if not exists "{task_name}" (date date, start_time datetime, end_time datetime, status int)')
    # 判断表是否为空
    curs.execute(f'select * from "{task_name}"')
    ret = _is_curs_empty(curs)
    # print(ret, "ret")
    db_end(conn, curs)
    return ret


def update_all_ongoing_tasks_status(usr_id: str, dt_now: datetime):
    conn, curs = db_start(usr_id)
    curs.execute('select * from ONGOING_TASKS')
    big_tasks_rcds = curs.fetchall()
    db_end(conn, curs)
    for row in big_tasks_rcds:
        task_name = row[0]
        # print("update_all_ongoing_tasks_status, task_name is ", task_name)
        # 先检查子任务表是否存在和是否为空，如果不存在或为空，则跳过
        if _is_subtask_table_empty(usr_id, task_name):
            continue
        # print('UPDATE starts...')
        # 先更新全部下属子任务的状态
        update_subtasks_status(usr_id, dt_now, task_name)
        # 再更新原任务的状态
        _update_ongoing_task_status_logic(usr_id, task_name)


# 更新一个原任务的全部下属子任务(subtasks)的状态。precondition:子任务表非空
def update_subtasks_status(usr_id: str, dt_now: datetime, task_name: str):
    conn, curs = db_start(usr_id)
    # 先检查有无可以从 未开始 -> 正在进行
    # print(
    #     'select * from "{task_name}" where status = {not_start_code} and start_time <= "{dt_now}" and end_time >= "{dt_now}"'.format(
    #         task_name=task_name, not_start_code=SUBTASK_STATUS_CODE['not_start'], dt_now=dt_now))
    curs.execute(
        'select * from "{task_name}" where status = "{not_start_code}" and start_time <= "{dt_now}" and end_time >= "{dt_now}"'.format(
            task_name=task_name, not_start_code=SUBTASK_STATUS_CODE['not_start'], dt_now=dt_now))
    # 如果存在命中结果，则更新数据
    if not _is_curs_empty(curs):
        curs.execute('update ONGOING_TASKS set status = "{doing_code}" where name = "{task_name}"'.format(
            doing_code=SUBTASK_STATUS_CODE['doing'], task_name=task_name))  # 更新ONGOING_TASKS
        curs.execute(
            'update "{task_name}" set status = "{doing_code}" where status = "{not_start_code}" and start_time <= "{dt_now}" and endtime >= "{dt_now}"'.format(
                task_name=task_name, doing_code=SUBTASK_STATUS_CODE['doing'],
                not_start_code=SUBTASK_STATUS_CODE['not_start'], dt_now=dt_now))  # 更新具体的任务table
    # 再检查有无可以从 正在进行 -> 已过期
    curs.execute(
        'select * from "{task_name}" where status = "{doing_code}" and end_time < "{dt_now}"'.format(
            task_name=task_name, doing_code=SUBTASK_STATUS_CODE['not_start'], dt_now=dt_now))
    # 存在这样的任务，更新状态
    if not _is_curs_empty(curs):
        curs.execute(
            'update "{task_name}" set status = "{time_out_code}" where status = "{doing_code}" and end_time < "{dt_now}"'.format(
                task_name=task_name, doing_code=SUBTASK_STATUS_CODE['doing'],
                time_out_code=SUBTASK_STATUS_CODE['time_out'], dt_now=dt_now))  # 更新具体的任务table
    # 再检查有无可以从 未开始 -> 已过期
    curs.execute('select * from "{task_name}" where status = "{not_start_code}" and end_time < "{dt_now}"'.format(
        task_name=task_name, not_start_code=SUBTASK_STATUS_CODE['not_start'], dt_now=dt_now))
    if not _is_curs_empty(curs):
        curs.execute(
            'update "{task_name}" set status = "{time_out_code}" where status = "{not_start_code}" and end_time < "{dt_now}"'.format(
                task_name=task_name, time_out_code=SUBTASK_STATUS_CODE['time_out'],
                not_start_code=SUBTASK_STATUS_CODE['not_start'], dt_now=dt_now))
    db_end(conn, curs)

    # # 最后检查是否还存在 正在进行 或 未开始的子任务
    # curs.execute(
    #     'select * from {task_name} where status = {not_start_code} or status = {doing_code}'.format(
    #         task_name=task_name, not_start_code=SUBTASK_STATUS_CODE['not_start'],
    #         doing_code=SUBTASK_STATUS_CODE['doing']))
    # # 如果不存在，则根据是否存在已过期的子任务（表里是否还有记录），将原任务判定为已过期 或 已完成（只要有已过期的子任务，原任务必然过期）
    # if _is_curs_empty(curs):
    #     # 检查是否存在已过期任务
    #     curs.execute('select * from {task_name} where status = {time_out_code}'.format(task_name=task_name,
    #                                                                                    time_out_code=
    #                                                                                    SUBTASK_STATUS_CODE['time_out']))
    #     # 如果不存在已过期子任务（原任务完成）
    #     if _is_curs_empty(curs):
    #         db_end(conn, curs)
    #         terminate_task(usr_id, task_name, SUBTASK_STATUS_CODE['finish'])
    #     else:
    #         db_end(conn, curs)
    #         terminate_task(usr_id, task_name, SUBTASK_STATUS_CODE['time_out'])
    # else:
    #     # 如果不存在正在进行任务
    #     curs.execute('select * from {task_name} where status = {doing}'.format(task_name, SUBTASK_STATUS_CODE['doing']))
    #     if _is_curs_empty(curs):
    #         curs.execute('update ONGOING_TASKS set status = {not_start} where name = {task_name}'.format(
    #             SUBTASK_STATUS_CODE['not_start'], task_name))
    #     else:
    #         curs.execute('update ONGOING')
    #     db_end(conn, curs)


# 返回 str, str 或 None, None
def get_task_startTime_and_endTime(usr_id: str, task_name: str) -> tuple:
    conn, curs = db_start(usr_id)
    curs.execute(
        'create table if not exists "{task_name}"(date date, start_time datetime, end_time datetime, status int)'.format(
            task_name=task_name))
    curs.execute('select * from "{task_name}"'.format(task_name=task_name))
    ret = curs.fetchall()
    db_end(conn, curs)
    if len(ret) == 0:
        return None, None
    else:
        ret.sort(key=lambda e: e[1])
        return ret[0][1], ret[-1][2]


def _is_curs_empty(cursor: sqlite3.Cursor) -> bool:
    tmp = cursor.fetchone()
    return False if tmp else True


def is_usr_existed(usr_id: str):
    filename = _usr_id2db_filename(usr_id)
    path = pathlib.Path(filename)
    print(path)
    return path.exists()


def is_password_correct(usr_id: str, password_in_encrypted: str):
    conn, curs = db_start(usr_id)
    curs.execute('select pass_word from PASS_WORD')
    qry_ret = curs.fetchone()
    db_end(conn, curs)
    if qry_ret[0] == password_in_encrypted:
        return 0
    return -1


def usr_update_password(usr_id: str, encrypted_password: str):
    conn, curs = db_start(usr_id)
    tbl_drp = 'drop table if exists PASS_WORD'
    curs.execute(tbl_drp)
    tbl_crt = 'create table if not exists PASS_WORD(pass_word text)'
    curs.execute(tbl_crt)
    curs.execute('delete from PASS_WORD')
    curs.execute('insert into PASS_WORD values(?)', [encrypted_password])
    db_end(conn, curs)


def usr_update_profile(usr_id: str, p_dict: dict = {}):
    conn, curs = db_start(usr_id)
    tbl_drp = 'drop table if exists USR_PROFILE'
    curs.execute(tbl_drp)
    tbl_crt = 'create table if not exists USR_PROFILE(nickname text, gender text, region text, signature text)'
    curs.execute(tbl_crt)
    tbl_ins = 'insert into USR_PROFILE(?, ?, ?, ?)'
    curs.execute(tbl_ins, [p_dict['nickname'], p_dict['gender'], p_dict['region'], p_dict['signature']])
    db_end(conn, curs)


def usr_get_profile(usr_id: str) -> dict:
    conn, curs = db_start(usr_id)
    tbl_crt = 'create table if not exists USR_PROFILE(nickname text, gender text, region text, signature text)'
    curs.execute(tbl_crt)
    curs.execute('select * from USR_PROFILE')
    profile_rcd = curs.fetchone()
    keys = ['nickname', 'gender', 'region', 'signature']
    if not profile_rcd:
        p_dict = dict(zip_longest(keys, []))
    else:
        p_dict = dict(zip(keys, profile_rcd))
    return p_dict


def usr_register(usr_id: str, encrypted_password: str):
    _init_db(usr_id)
    usr_update_password(usr_id, encrypted_password)


def usr_login(usr_id: str, password_in: str):
    if not is_usr_existed(usr_id):
        print("用户不存在")
        return -1
    elif is_password_correct(usr_id, password_in) != 0:
        print("密码错误")
        return -2
    return 0
