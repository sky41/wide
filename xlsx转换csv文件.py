# 把需要转化的xlsx文件放在pycharm项目文件目录里
import pandas as pd


def xlsx_to_csv_pd():
    data_xls = pd.read_excel('附件_一季度.xlsx', index_col=0)  # 输入xlsx文件名
    data_xls.to_csv('2.csv', encoding='utf-8')  # 输出csv文件名


if __name__ == '__main__':
    xlsx_to_csv_pd()
