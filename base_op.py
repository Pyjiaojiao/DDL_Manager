import datetime
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

TRIVIAL_KEY = {'type', 'detail', 'name'}
SCHEDULE_KEY = {'is_daily', 'priority', 'time_estimated', 'ddl'}
STATUS_KEY = {'status'}
RANGE_KEY = ['start_date', 'end_date']

QRY_MANAGER_KEY = {'is_daily', 'status', 'type', 'priority'}
QRY_DATE_KEY = {'date'}

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
        task_dict['ddl'] = my_data_converter.QDate2date(task_dict['endDate'])
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
            my_data_base.normal_modify(usr_id=usr_id, task_name=task_name, key=key, value=task_mod_dict[key])
            # TODO: 是否触发调度？


def finish_subtask(usr_id: str = USR_ID, task_name="test", task_start_time: QDateTime = None):
    usr_id = USR_ID
    my_data_base.terminate_subtask(usr_id=usr_id, task_name=task_name,
                                   task_start_time=my_data_converter.QDateTime2datetime(task_start_time),
                                   terminate_code=2)
    dt_now = datetime.datetime.now()  # type - datetime
    my_data_base.update_subtasks_status(usr_id, dt_now, task_name)


def delete_subtask(usr_id: str = USR_ID, task_name="test", task_start_time: QDateTime = None):
    usr_id = USR_ID
    my_data_base.terminate_subtask(usr_id=usr_id, task_name=task_name,
                                   task_start_time=my_data_converter.QDateTime2datetime(task_start_time),
                                   terminate_code=4)


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
    if not my_data_base.usr_login(usr_id, password_encrypted):
        # login failed
        return -1
    # login succeed
    global USR_ID
    USR_ID = usr_id
    return 0


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
            specify_keys_4task.append(key + ' = ' + str(specify[key]))
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
            task['startTime'] = my_data_converter.date_str2QDateTime(start_time_str) if start_time_str else None
            task['endTime'] = my_data_converter.date_str2QDateTime(end_time_str) if end_time_str else None
        return tasks
    else:
        # 有date需求，认为是在日历系统查询
        _update_all_ongoing_tasks_status(usr_id)
        return my_data_base.get_specified_subtasks(usr_id, specify_str_4task, specify_str_4subtask)


def _update_all_ongoing_tasks_status(usr_id: str):
    dt_now = datetime.datetime.now().replace(microsecond=0)  # type - datetime
    my_data_base.update_all_ongoing_tasks_status(usr_id=usr_id, dt_now=dt_now)


def debug():
    register("admin", '123')
    if login('admin', '123') == 0:
        print('login succeed!')
    task_dict = {'name': "TestTask",  # str
                 'isDaily': False,  # bool
                 'startTime': QDateTime(1970, 1, 1, 0, 0),  # QDateTime
                 'endTime': QDateTime(2050, 1, 1, 0, 0),  # QDateTime
                 'startDate': QDateTime(2022, 8, 14, 0, 0).date(),
                 'endDate': QDateTime(2022, 8, 14, 0, 0).date(),
                 'costTime': QTime(3, 30),  # QTime
                 'type': None,  # str
                 'importance': 0,  # int:[0,4)
                 'status': 0,  # int:[0,4)
                 'detail': "Detail Text"}  # str
    add_task("admin", task_dict=task_dict)
    task_dict = {'name': "DAILY",  # str
                 'isDaily': True,  # bool
                 'startTime': QDateTime(1970, 1, 1, 0, 0),  # QDateTime
                 'endTime': QDateTime(2050, 1, 1, 0, 0),  # QDateTime
                 'startDate': QDateTime(2022, 8, 15, 0, 0).date(),
                 'endDate': QDateTime(2022, 8, 19, 0, 0).date(),
                 'costTime': QTime(3, 30),  # QTime
                 'type': None,  # str
                 'importance': 0,  # int:[0,4)
                 'status': 0,  # int:[0,4)
                 'detail': "Detail Text"}  # str
    add_task("admin", task_dict=task_dict)
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
        print([(e['name'], e['startTime'], e['endTime']) for e in item])


if __name__ == '__main__':
    debug()
