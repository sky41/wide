import xlwt
import csv
import openpyxl
import pandas as pd

# 导入原始数据
# Fpath1 = "附件_一季度.xlsx"
# df1 = pd.read_excel(Fpath1)
# Fpath2 = "附件_二季度.xlsx"
# df2 = pd.read_excel(Fpath2)

# pd打开，注意指定引擎
df = pd.read_excel("附件_一季度.xlsx", engine="openpyxl")

