"""
数据库读写
"""
import pathlib

import Day
import Task
import sqlite3
import datetime
import my_data_converter


# 用于将任务字典转换为 ONGOING_TASK table 所需的任务序列
def _task_dict2ongoing_task_info_list(td):
    l = [td.name, td.is_daily, td.priority, td.time_estimated, td.time_abd, td.ddl, td.detail]
    return l


# 用户id转为对应db文件名
def _usr_id2db_filename(usr_id):
    return str(usr_id) + '.db'


# 注册时调用，初始化数据库
def _init_db(usr_id):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))  # 打开一个数据库的链接
    curs = conn.cursor()  # 创建游标
    # 所有正在进行的任务 name 均不相同
    tbl_crt = '''
         create table if not exists ONGING_TASKS
         (name text, is_daily int, priority int,
         time_estimated datetime, time_abd datetime,
         ddl date, detail text)
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
    conn.commit()
    curs.close()
    conn.close()


# 新任务保存到db的 ONGOING_TASKS table
def save_new_task2db(usr_id, task_dict):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    tbl_ins = '''
        insert into ONGING_TASKS
        values(?, ?, ?, ?, ?, ?, ?)
    '''
    task_info_list = _task_dict2ongoing_task_info_list(task_dict)
    curs.execute(tbl_ins, task_info_list)
    conn.commit()
    curs.close()
    conn.close()


# 从数据库中删除task
def del_task(usr_id, task_name):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    curs.execute("select * from ONGOING_TASKS where name = {task_name}".format(task_name))
    ret = curs.fetchall()
    # 正在进行库没有task_name, 去终结库找
    if not ret:
        ret = curs.execute("select * from TERMINATED_TASKS where name = {task_name}".format(task_name)).fetchall()
        if not ret:
            curs.execute("delete from TERMINATED_TASKS where name = {task_name}".format(task_name))
    else:
        curs.execute("drop table {task_name}".format(task_name))
        curs.execute("delete from ONGOING_TASKS where name = {task_name}".format(task_name))
    curs.close()
    conn.commit()
    conn.close()


# 将一个任务的调度列表存入数据库，表名为 task_name
# schedule_list 元素为 (date, start_time, end_time), type为 (date, time, time)
def save_task_schedule_list2name_table(usr_id, task_name, schedule_list):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    tbl_drop = 'drop table if exists {table_name}'.format(table_name=task_name)
    tbl_crt = '''
        create table if not exist {table_name}
        (date date, start_time datetime, end_time datetime)
    '''.format(table_name=task_name)
    tbl_ins = '''
        insert into {table_name}
        values(?, ?, ?)
    '''.format(table_name=task_name)
    curs.execute(tbl_drop)
    curs.execute(tbl_crt)
    curs.executemany(tbl_ins, schedule_list)
    conn.commit()
    curs.close()
    conn.close()


def rename_task(usr_id, old_name, new_name):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    # 小表改名
    tbl_rnm = 'alter table {table_old_name} rename to {table_new_name}' \
        .format(table_old_name=old_name, table_new_name=new_name)
    tsk_rnm = 'update ONGOING_TASKS set name=? where name=?'  # 大表，只修改正在发生的任务表，已终结表是历史数据，不能修改
    curs.execute(tbl_rnm)
    name_tuple_new_old = (new_name, old_name)
    curs.execute(tsk_rnm, name_tuple_new_old)
    conn.commit()
    curs.close()
    conn.close()


# 用于修改除任务名(id)之外的普通任务属性
def normal_modify(usr_id, task_name, key, new_val):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    # if is in ONGOING_TASKS table
    curs.execute("update ONGOING_TAKS set {key}={new_val} where name = {task_name}".format(key=key, new_val=new_val))
    conn.commit()
    curs.close()
    conn.close()


def get_max_continuous_working_time(usr_id: str) -> datetime.time:
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    # TODO: 从数据库中查找
    conn.commit()
    curs.close()
    conn.close()
    return datetime.time(2, 0, 0)  # for test


# 返回全部正在发生的任务, 返回值类型为list[Task[,...]]
def get_ongoing_tasks_rcds(usr_id: str) -> 'Task records list':
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    curs.execute('select * from ONGOING_TASKS')
    rcd_list = curs.fetchall()
    curs.close()
    conn.close()
    return rcd_list


def clear_scheduled_subtasks(usr_id):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    ongoing_tasks_rcds = get_ongoing_tasks_rcds(usr_id)
    for row in ongoing_tasks_rcds:
        task_name = row[0]
        curs.execute('drop table {table_name}'.format(table_name=task_name))
    conn.commit()
    curs.close()
    conn.close()


# 返回所有被调度进行的子任务，返回值类型为Task list
def get_all_ongoing_subtasks(usr_id: str) -> 'Task list':
    ongoing_task_rcd_list = get_ongoing_tasks_rcds(usr_id)
    # name-task dict for ongoing tasks
    task_dict = my_data_converter.records2ongoing_tasks_dict(ongoing_task_rcd_list)
    ret = []
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    for row in ongoing_task_rcd_list:
        task_name = row[0]
        curs.execute('select * from table {task_name}'.format(task_name))
        subtasks_rcd_list = curs.fetchall()
        subtasks_list = my_data_converter.records2subtask_list(task_dict[task_name], subtasks_rcd_list)
        ret.extend(subtasks_list)
    curs.close()
    conn.close()
    return ret


# 返回满足特定检索条件的被调度子任务序列。返回值类型为list[records]
# specify_str 为 where ...
def get_specified_subtasks(usr_id: str, specify_str: str) -> list:
    ongoing_task_rcd_list = get_ongoing_tasks_rcds(usr_id)
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    ret = []
    for row in ongoing_task_rcd_list:
        task_name = row[0]
        curs.execute('select * from {table_name} '.format(table_name=task_name) + specify_str)
        subtasks_rcd_list = curs.fetchall()
        ret.extend(subtasks_rcd_list)
    curs.close()
    conn.close()
    return ret


def is_usr_existed(usr_id: str):
    filename = _usr_id2db_filename(usr_id)
    path = pathlib.Path(filename)
    return path.exists()


def is_password_correct(usr_id: str, password_in_encrypted: str):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    curs.execute('select pass_word from PASS_WORD')
    qry_ret = curs.fetchone()
    curs.close()
    conn.close()
    if qry_ret[0] == password_in_encrypted:
        return 0
    return -1


def usr_update_password(usr_id: str, encrypted_password: str):
    conn = sqlite3.connect(_usr_id2db_filename(usr_id))
    curs = conn.cursor()
    tbl_crt = 'create table if not exists PASS_WORD(pass_word text)'
    curs.execute(tbl_crt)
    curs.execute('delete from PASS_WORD')
    curs.execute('insert into PASS_WORD values(?)', encrypted_password)
    conn.commit()
    curs.close()
    conn.close()


def usr_register(usr_id: str, encrypted_password: str):
    _init_db(usr_id)
    usr_update_password(usr_id, encrypted_password)


def usr_login(usr_id: str, password_in: str):
    if not is_usr_existed(usr_id):
        return -1
    elif not is_password_correct(usr_id, password_in):
        return -2
    return 0
