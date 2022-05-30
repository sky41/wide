#  编码必须要，因为里面有中文，要不然索引不成功，已开始索引没成功就是因为编码问题；
# coding=utf-8

# 导入pandas库
import pandas as pd
import xlwt
import csv
import openpyxl
import pandas as pd

select_list = [
    "AAA",
    "BBB"
]

datas = []
# pd打开，注意指定引擎
df = pd.read_excel("附件_一季度.xlsx", engine="openpyxl")

# 获取行号的索引，并对其进行遍历：
for i in df.index.values:
    if df.loc[i].values[2] in select_list:
        print(df.loc[i].values)
        datas.append(df.loc[i].values.tolist())

# 遍历写入结果文件
with open("分类01.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in datas:
        writer.writerow(row)
# 这两个可以忽略，因为没用到；
import numpy as np
# 这个是数据库导入的，用来练手的，你们没有本地数据库也用不用；
import pymysql
import xlwings

# 导入数据
Fpath1 = "附件_一季度.xlsx"
df1 = pd.read_excel(Fpath1)
Fpath2 = "附件_二季度.xlsx"
df2 = pd.read_excel(Fpath2)
# 因为两个数据时间格式不一样，需要调整，然后且切片；

# 输出调整后的两个表，看是否样式一样；
print(df1)

# 判断是否有缺失值，很高兴，发现没有缺失值，如果有的话会输出True

# 保存数据，开始愉快的分析数据吧，

# -----------------------------------------------#
# -----------现在代码结束了-----------------------#
# -----------底下是联系写的-----------------------#
# ----------------------------------------------#

# df1.to_excel("K:/马雷/zy1.xls")
# s3 = df.set_index("最大风向", inplace=True, drop=False)
# print(s3)
# print(s3.head(5))

# print(s2);
# cloumes=["平均风速" ,"zuixiao"];
# s3 = df(cloumes);
# print(df.zuixiao)
# print(df.describe())
# print(df["最小风向"].mean)
# print(df.cov())
# print(df.corr())
# s1 = df[1:3];
# s1.to_excel("K:/马雷/zy1.xls", index=False)
# s3 = df["最大风向"].fillna(0);
# s4=df["最大风向"].notnull()
# print(s4)
# print(s3)
# print(df["zuixiao"].df["zuida"])

# print(df[1:3])

# print(s3)
# print(s1.index)
# s1=pd.Series(re
# ads.head(2))
# print(reads.reindex)
# print(reads.dtypes)
#  导入数据库数据
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="zy2015532",
#     database="myemployees",
#     charset="utf8"
# )
# mysql_page = pd.read_sql("select * from employees where salary>10000", con=conn)
# print(mysql_page)
