import datetime
import time


def time_ti():
    now = datetime.datetime.now()
    # 初始设定秒数，初始+现在输出时间
    print(now.hour, now.minute, now.second)
    print(str(now.hour + now.minute + now.second) + datetime.datetime.now().strftime('%Y%m%d'))


def s():
    second = 1
    while 1 == 1:
        time.sleep(second)
        time_ti()


s()
