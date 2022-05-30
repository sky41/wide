import time


# 定义一个带参函数方法，里面设置时分秒，通过计算秒数来获取定时多久
def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 这是隔5秒执行一次
second = sleeptime(0, 0, 5)
while 1 == 1:
    time.sleep(second)
    print('do action')
