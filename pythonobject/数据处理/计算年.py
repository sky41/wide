# -*- coding: UTF-8 -*-
import time


def What_day_of_the_year(inputTime):
    # 函数，判断字符串是否为数字
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    # 判断字符串是否含有“-”分割符（是否按格式输入）
    if inputTime.find('-') != -1:
        # if '' in inputTime != 'False' or ' ' in inputTime != 'False': #想判断是否含空格（含空格不符合格式）,效果不佳，已废弃;改用Python异常处理
        timeList = inputTime.split('-')  # 以“-”符分割字符串，赋值为列表

        # 通过for循环+自定义的is_number函数判断列表是否含有字母（含有字母不符合格式）
        trueList = []
        for numberValue in timeList:
            trueList.append(is_number(numberValue))
        if trueList.count('False') == 0:

            timeList = list(map(int, timeList))  # 将列表从字符串转换为int整数
            if timeList[0] % 4 == 0 or timeList[0] % 400 == 0:  # 判断是否为闰年。
                timeTotal = (7 * 31) + (4 * 30) + 29

                exceptSameMonthDay = 0
                for monthValue in range(1, timeList[1]):  # 计算除当月在内的，已过天数；如：2009-11-14，不算第11月。仅算1～10月
                    if monthValue == 1 or monthValue == 3 or monthValue == 5 or monthValue == 7 or monthValue == 8 or monthValue == 10 or monthValue == 12:
                        exceptSameMonthDay += 31
                    elif monthValue == 4 or monthValue == 6 or monthValue == 9 or monthValue == 11:
                        exceptSameMonthDay += 30
                    elif monthValue == 2:
                        exceptSameMonthDay += 29
                return exceptSameMonthDay + timeList[2]
            else:
                timeTotal = (7 * 31) + (4 * 30) + 28

                exceptSameMonthDay = 0
                for monthValue in range(1, timeList[1]):
                    if monthValue == 1 or monthValue == 3 or monthValue == 5 or monthValue == 7 or monthValue == 8 or monthValue == 10 or monthValue == 12:
                        exceptSameMonthDay += 31
                    elif monthValue == 4 or monthValue == 6 or monthValue == 9 or monthValue == 11:
                        exceptSameMonthDay += 30
                    elif monthValue == 2:
                        exceptSameMonthDay += 28
                return exceptSameMonthDay + timeList[2]
        else:
            return 1
    # else:
    # return 1
    else:
        return 1


timeValue = time.strftime("%Y-%m-%d", time.localtime())  # 获取当前日期，并格式化
# 格式化成2020-02-26形式

tipsValue = '请输入日期，如:' + timeValue + ':'
inputTime = input(tipsValue)
try:
    inputTime = What_day_of_the_year(inputTime)
    if inputTime == 1:
        print('您的输入有误!')
    else:
        print(inputTime)
except:
    print('您的输入有误!')
