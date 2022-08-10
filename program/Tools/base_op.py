import Day
import Task
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime
import sqlite3
import datetime
import my_data_base
from hashlib import md5
from my_data_converter import records2ongoing_tasks
import schedule

# def add_task(usr_id, task_dict):
#     a = datetime.date(1970,1,1)
#     li = [a]
#     print(li)
#     li[0] += datetime.timedelta(days=1)
#     print(li)
#     b = datetime.date(1970,1,1)
#     dict = {a:1}
#     print(dict[b])
# add_task(0,0)


USR_ID = 0  # 当前正在操作用户

PLAIN_KEY = ['is_daily', 'type', 'importance', 'status']
RANGE_KEY = ['start_date', 'end_date']


# 整理传入字典格式
def pretreatment(task_dict):
    if "isDaily" in task_dict:
        task_dict["is_daily"] = 1 if task_dict["isDaily"] else 0
    if "importance" in task_dict:
        task_dict["priority"] = task_dict["importance"]
    if "costTime" in task_dict:
        # NOTICE: 目前前端需求不超过24h，只用到hour和minute。如需扩展时间范围，记得改这里。
        hour = task_dict['costTime'].hour()
        minute = task_dict['costTime'].minute()
        task_dict["time_abd"] = task_dict["time_estimated"] = datetime.datetime.strptime(hour + ':' + minute, "%H:%M")
    if "endTime" in task_dict:
        q_date = task_dict['endTime'].date()
        year = q_date.year()
        month = q_date.month()
        day = q_date.day()
        task_dict['ddl'] = datetime.datetime(year, month, day).date()


def add_task(usr_id: str = USR_ID, task_dict: dict = {}):
    pretreatment(task_dict)
    my_data_base.save_new_task2db(usr_id, task_dict)


def del_task(usr_id: str = USR_ID, task_name="test"):
    my_data_base.del_task(usr_id, task_name)


def mod_task(usr_id: str = USR_ID, task_name="test", task_mod_dict: dict = {}):
    pretreatment(task_mod_dict)
    # 数据库函数已写，待讨论调用形式
    pass


def re_arrange(usr_id: str = USR_ID):
    schedule.task_arrange()
    # 不返回调度结果，只存储调度结果。
    # 调度结果需要由前端给出查询请求来获取。
    pass


def encrypt_usr_password(password_in: str) -> str:
    password = password_in.strip()
    m = md5(b'key2022python')
    m.update(password.encode("utf-8"))
    password_encrypted = m.hexdigest()
    return password_encrypted


def register(usr_id: str, password: str) -> 'Finish Code':
    if my_data_base.is_usr_existed(usr_id):
        # register failed
        return -1
    password_encrypted = encrypt_usr_password(password)
    my_data_base.usr_register(usr_id, password_encrypted)
    # register succeed
    return 0


def login(usr_id: str, password_in: str) -> 'Finish Code':
    password_encrypted = encrypt_usr_password(password_in)
    if not my_data_base.usr_login(usr_id, password_encrypted):
        # login failed
        return -1
    # login succeed
    global USR_ID
    USR_ID = usr_id
    return 0


# 从db恢复已保存的全部子任务，返回列表，按date, start_time排序
def load_all_subtasks(usr_id: str) -> list:
    all_subtasks = my_data_base.get_all_ongoing_subtasks(usr_id)
    all_subtasks.sort(key=lambda e: (e.date, e.start_time))
    return all_subtasks


def load_specified_subtasks(usr_id: str, specify: dict) -> list:
    pretreatment(specify)
    if not specify:
        return load_all_subtasks(usr_id)
    specify_keys = []
    for key in specify:
        if key in PLAIN_KEY:
            specify_keys.append(key + ' = ' + specify[key])
        elif key == 'start_date':
            specify_keys.append(key + ' >= ' + specify[key])
        elif key == 'end_date':
            specify_keys.append(key + ' <= ' + specify[key])
    specify_str = 'where ' + ' and '.join(specify_keys)
    return my_data_base.get_specified_subtasks(usr_id, specify_str)
