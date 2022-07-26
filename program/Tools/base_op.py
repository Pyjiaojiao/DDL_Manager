import datetime

import my_data_analyzer
import my_data_base
from hashlib import md5
import schedule
import my_data_converter
from PyQt5.QtCore import QTime, QDateTime

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

NAME_KEY = {'name'}
TRIVIAL_KEY = {'type', 'detail'}
SCHEDULE_KEY = {'priority', 'time_estimated', 'start_date', 'ddl'}
STATUS_KEY = {'status'}

QRY_MANAGER_KEY = {'is_daily', 'status', 'type', 'priority'}
QRY_DATE_KEY = {'date'}
QRY_RANGE_KEY = {'start_date', 'end_date'}

SUBTASK_STATUS_CODE = {'not_start': 0, 'doing': 1, 'finish': 2, 'time_out': 3,
                       'delete': 4}  # dict{op_str: int} 0 未开始 1 正在做 2 完成 3 过期 4 删除


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
        task_dict["time_abd"] = datetime.datetime(1900, 1, 1)
        task_dict["time_estimated"] = datetime.datetime.strptime(str(hour) + ':' + str(minute),
                                                                 "%H:%M")
    if "endDate" in task_dict:
        task_dict['end_date'] = task_dict['ddl'] = my_data_converter.QDate2date(task_dict['endDate'])
    # if "startDate" in task_dict:
    #     task_dict["start_time"] = my_data_converter.QDateTime2datetime(task_dict["startTime"])
    #     task_dict['start_date'] = task_dict['start_time'].date()
    if "startDate" in task_dict:
        task_dict["start_date"] = my_data_converter.QDate2date(task_dict["startDate"])
    # 需求更改了，现在type可以是str
    # if "type" in task_dict and task_dict["type"] not in range(0, 5):
    #     task_dict['type'] = 0
    if "date" in task_dict:
        task_dict['date'] = my_data_converter.QDate2date(task_dict['date'])


def add_task(usr_id: str = USR_ID, task_dict: dict = {}):
    usr_id = USR_ID
    pretreatment(task_dict)
    my_data_base.save_new_task2db(usr_id, task_dict)


def del_task(usr_id: str = USR_ID, task_name="test"):
    usr_id = USR_ID
    my_data_base.del_task(usr_id, task_name)


def mod_task(usr_id: str = USR_ID, task_name="test", task_start_time: QDateTime = None, task_mod_dict: dict = {}):
    usr_id = USR_ID
    pretreatment(task_mod_dict)
    # 数据库函数已写，待讨论调用形式
    for key in task_mod_dict:
        if key in SCHEDULE_KEY:
            my_data_base.normal_modify(usr_id=usr_id, task_name=task_name, key=key, new_val=str(task_mod_dict[key]))
            # TODO: 是否触发调度？
        elif key in TRIVIAL_KEY:
            my_data_base.normal_modify(usr_id=usr_id, task_name=task_name, key=key, new_val=str(task_mod_dict[key]))


def finish_subtask(usr_id: str = USR_ID, task_name="test", task_start_time: QDateTime = None):
    usr_id = USR_ID
    my_data_base.terminate_subtask(usr_id=usr_id, task_name=task_name,
                                   task_start_time=my_data_converter.QDateTime2datetime(task_start_time),
                                   terminate_code=SUBTASK_STATUS_CODE['finish'])
    dt_now = datetime.datetime.now()  # type - datetime
    my_data_base.update_subtasks_status(usr_id, dt_now, task_name)


def delete_subtask(usr_id: str = USR_ID, task_name="test", task_start_time: QDateTime = None):
    usr_id = USR_ID
    my_data_base.terminate_subtask(usr_id=usr_id, task_name=task_name,
                                   task_start_time=my_data_converter.QDateTime2datetime(task_start_time),
                                   terminate_code=SUBTASK_STATUS_CODE['delete'])


def re_arrange(usr_id: str = USR_ID):
    usr_id = USR_ID
    schedule.task_arrange(usr_id)
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
    if my_data_base.usr_login(usr_id, password_encrypted) < 0:
        # login failed
        return -1
    # login succeed
    global USR_ID
    USR_ID = usr_id
    return 0


# 改密码。需要登录后调用。需要传入新密码原文。
def update_password(new_password: str, usr_id: str = USR_ID):
    usr_id = USR_ID
    password_encrypted = encrypt_usr_password(new_password)
    my_data_base.usr_update_password(usr_id, password_encrypted)


# 更新用户个人资料。需要登录后调用。profile_dict应该包含 "nickname"、"gender"、"region"、"signature"键，值应该为str，或者None。
# 账号（usr_id）不可更改。
def update_profile(usr_id: str = USR_ID, profile_dict: dict = {}):
    usr_id = USR_ID
    my_data_base.usr_update_profile(usr_id, profile_dict)


# 查询用户个人资料。返回值为(usr_id, 字典)。字典包含update_profile接口中提到的键。可能有值为空。
def get_profile(usr_id: str = USR_ID) -> tuple:
    usr_id = USR_ID
    return usr_id, my_data_base.usr_get_profile(usr_id)


# 从db恢复已保存的全部子任务，返回列表，按date, start_time排序
def load_all_subtasks(usr_id: str = USR_ID) -> list:
    usr_id = USR_ID
    all_subtasks = my_data_base.get_all_ongoing_subtasks(usr_id)
    all_subtasks.sort(key=lambda e: (e.date, e.start_time))
    return all_subtasks


# 返回满足查询条件的任务字典序列（不论是查询原始任务，还是查询子任务，都是这个格式的返回值）
def load_specified_subtasks(usr_id: str = USR_ID, specify: dict = {}) -> list:
    usr_id = USR_ID
    pretreatment(specify)
    print('load_specified_subtasks USR_ID is %s' % usr_id)
    specify_keys_4task = []
    specify_keys_4subtask = []
    for key in specify:
        if key in QRY_MANAGER_KEY:
            specify_keys_4task.append(key + ' = "' + str(specify[key]) + '"')
        elif key in QRY_DATE_KEY:
            specify_keys_4subtask.append(key + ' = ' + '"' + str(specify[key]) + '"')
        # elif key == 'start_date':
        #     specify_keys.append(key + ' >= ' + specify[key])
        # elif key == 'end_date':
        #     specify_keys.append(key + ' <= ' + specify[key])
    specify_str_4task = (' where ' + ' and '.join(specify_keys_4task)) if specify_keys_4task else ''
    specify_str_4subtask = (' where ' + ' and '.join(specify_keys_4subtask)) if specify_keys_4subtask else ''
    print("specify_str_4subtask is: " + specify_str_4subtask)
    if specify_str_4subtask == '':
        # 无date需求，认为是在任务管理页面查询
        _update_all_ongoing_tasks_status(usr_id)
        tasks = my_data_converter.records2ongoing_task_dicts(
            my_data_base.get_ongoing_tasks_rcds(usr_id=usr_id, specify_str=specify_str_4task))
        for task in tasks:
            start_time_str, end_time_str = my_data_base.get_task_startTime_and_endTime(usr_id, task['name'])
            task['startTime'] = my_data_converter.datetime_str2QDateTime(start_time_str) if start_time_str else None
            task['endTime'] = my_data_converter.datetime_str2QDateTime(end_time_str) if end_time_str else None
        return tasks
    else:
        # 有date需求，认为是在日历系统查询
        _update_all_ongoing_tasks_status(usr_id)
        return my_data_base.get_specified_subtasks(usr_id, specify_str_4task, specify_str_4subtask)


def _update_all_ongoing_tasks_status(usr_id: str):
    dt_now = datetime.datetime.now().replace(microsecond=0)  # type - datetime
    my_data_base.update_all_ongoing_tasks_status(usr_id=usr_id, dt_now=dt_now)


def get_analyze_result(usr_id: str = USR_ID, specify: dict = {}) -> dict:
    usr_id = USR_ID
    pretreatment(task_dict=specify)
    _update_all_ongoing_tasks_status(usr_id)
    return my_data_analyzer.get_analyze_result(usr_id, specify)


def debug():
    register("admin", '123456')
    if login("admin", '123456') == 0:
        print('login succeed!')
    else:
        exit()
    task_dict = {'name': "111",  # str
                 'isDaily': False,  # bool
                 'startTime': QDateTime(1970, 1, 1, 0, 0),  # QDateTime
                 'endTime': QDateTime(2050, 1, 1, 0, 0),  # QDateTime
                 'startDate': QDateTime(2022, 8, 15, 0, 0).date(),
                 'endDate': QDateTime(2022, 8, 15, 0, 0).date(),
                 'costTime': QTime(3, 30),  # QTime
                 'type': "运动",  # str
                 'importance': 0,  # int:[0,4)
                 'status': 0,  # int:[0,4)
                 'detail': "Detail Text"}  # str
    add_task("admin", task_dict=task_dict)
    task_dict = {'name': "日常任务",  # str
                 'isDaily': True,  # bool
                 'startTime': QDateTime(1970, 1, 1, 0, 0),  # QDateTime
                 'endTime': QDateTime(2050, 1, 1, 0, 0),  # QDateTime
                 'startDate': QDateTime(2022, 8, 15, 0, 0).date(),
                 'endDate': QDateTime(2022, 8, 19, 0, 0).date(),
                 'costTime': QTime(3, 30),  # QTime
                 'type': "学习",  # str
                 'importance': 0,  # int:[0,4)
                 'status': 0,  # int:[0,4)
                 'detail': "Detail Text"}  # str
    # add_task("admin", task_dict=task_dict)
    qdict = {}
    print("USR_ID is %s" % USR_ID)
    rcds = load_specified_subtasks(specify=qdict)
    print(rcds)
    re_arrange()
    rcd2 = []
    qdict2 = {'date': QDateTime(2022, 8, 13, 0, 0).date()}
    for i in range(13, 20):
        qdict2['date'] = QDateTime(2022, 8, i, 0, 0).date()
        rcd2.append(load_specified_subtasks(specify=qdict2))
    # print(rcd2)
    for item in rcd2:
        item.sort(key=lambda e: e['startTime'])
        print([(e['name'], e['startTime'], e['endTime'], e['type']) for e in item])
    mod_task("admin", "111", QDateTime.fromString('2022-8-15 08:00', "yyyy-MM-dd hh:mm"),
             {"ddl": datetime.datetime(2022, 8, 21).date()})
    rcds = load_specified_subtasks({})
    print(rcds)


if __name__ == '__main__':
    debug()
