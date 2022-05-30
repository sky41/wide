# coding: utf-8

# In[1]:


import pandas as pd

data1 = pd.read_csv('附件_一季度0001.csv')
data2 = pd.read_csv('附件_一季度0001.csv')
data3 = pd.read_csv('附件_一季度0001.csv')
data4 = pd.read_csv('附件_一季度0001.csv')
data1.head(5)

# In[2]:


data1.describe()

# In[3]:


data1.info()

# In[4]:


data1.head(5)

# In[5]:


data1.head(5)

# In[6]:


data1['水表名'].unique()

# In[7]:


lever_table = pd.read_excel("附件_水表层级.xlsx")

# In[8]:


lever_table.to_csv('lever_table.csv', index=False)

# In[9]:


level = pd.read_csv('lever_table.csv')

# In[10]:


level.head(5)

# In[11]:


level['水表名'].unique()

# In[12]:


len(level['水表名'].unique()
    )

# In[13]:


len(data1['水表名'].unique())

# In[14]:


len(data2['水表名'].unique())

# In[15]:


len(data3['水表名'].unique())

# In[16]:


len(data4['水表名'].unique())

# In[17]:


data2.info()

# In[18]:


data3.info()

# In[19]:


data4.info()

# In[20]:


import numpy as np

len(data1.index)
data1['季度'] = pd.Series(["一季度" for i in range(len(data1.index))])

data1

# In[21]:


data2['季度'] = pd.Series(["二季度" for i in range(len(data2.index))])
data3['季度'] = pd.Series(["三季度" for i in range(len(data3.index))])
data4['季度'] = pd.Series(["四季度" for i in range(len(data4.index))])

# In[22]:


data4

# In[23]:


data = data1.append(data2, ignore_index=True)
data

# In[24]:


data = data.append([data3, data4], ignore_index=True)

# In[25]:


len(data['水表名'].unique())

# In[26]:


len(level['水表名'].unique())

# In[27]:


len(data1['水表名'].unique())

# In[28]:


len(data['水表号'].unique())

# In[29]:


data.head(4)

# In[30]:


level.head(4)

# In[31]:


data['水表名'].unique()

# In[32]:


len(level.index)

# In[33]:


use_water = data.groupby(by='水表名')['用量'].sum()

# In[34]:


use_water.sort_values(ascending=False)

# In[35]:


use_water.plot.hist()

# In[36]:


list_table_name = list(data['水表名'].unique())
list_table_name

# In[37]:


list_home = []
list_teaching_build = []
list_teacher_build = []
for name in list_table_name.copy():
    if name.find("学生宿舍") != -1 or name.find("留学生楼") != -1:
        list_home.append(name)
        list_table_name.remove(name)
list_home

# In[38]:


list_table_name
for name in list_table_name.copy():
    if name.find("XX") != -1 and name.find("楼") != -1:
        print(name)
        list_teaching_build.append(name)
        list_table_name.remove(name)
list_teaching_build

# In[39]:


list_table_name
for name in list_table_name.copy():
    if name.find("XX") != -1 and name.find("花") == -1:
        list_teacher_build.append(name)
        list_table_name.remove(name)
list_teacher_build

# In[40]:


list_agritural = []
for name in list_table_name.copy():
    if name.find("养殖") != -1 or name.find("养鱼") != -1 or name.find("大棚") != -1 or name.find("花") != -1:
        list_agritural.append(name)
        list_table_name.remove(name)
list_agritural

# In[41]:


for name in list_table_name.copy():
    if name.find("楼") != -1:
        list_teaching_build.append(name)
        list_table_name.remove(name)
list_table_name

# In[42]:


list_backup = list_table_name
name_list = data['水表名'].tolist()
name_list
type_list = []
for name in name_list:
    if name in list_backup:
        type_list.append("后勤")
    elif name in list_agritural:
        type_list.append("农业")
    elif name in list_home:
        type_list.append('宿舍')
    elif name in list_teacher_build:
        type_list.append("活动地方")
    else:
        type_list.append('教学楼')
type_list

# In[43]:


data['类型'] = pd.Series(type_list)
data

# In[44]:


type_sum = data.groupby(by='类型')['用量'].sum()

# In[45]:


import matplotlib  as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
type_sum.plot.barh(alpha=0.7)

# In[48]:


df_group_two = data.groupby(by=['类型'])
from matplotlib import pyplot as plt

i = 0
plt.figure(figsize=(25, 35), dpi=100)
for types, group in df_group_two:
    i += 1
    plt.subplot(3, 2, i)
    group.groupby(by='水表名').sum()["用量"].plot.barh(title=types, color='blue', alpha=.5)
plt.show()

# In[50]:


pd.read_csv('data.csv')

# In[49]:


# 判断用电层次关系
