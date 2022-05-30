import sys
from PyQt5.QtWidgets import *
import os
import shutil


# 未解决问题：1.def 的目录函数还不能连接到图形化界面
# 源文件目录调用函数
def Sdirectory():
    input('r' + '源文件目录:')


# 分类文件目录调用函数
def Tdirectory():
    input('r' + "分类文件目录")


def config(self):  # 各功能聚合函数
    print("截至")


def hander():
    src_dir = Sdirectory()

    data_dir = Tdirectory()
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    else:
        print("分类文件目录存在")
    file = os.listdir(src_dir)
    for ittt in file:

        src_path = os.path.join(src_dir, ittt)
        print(src_path)

        if os.path.isfile(src_path):
            ndir = ittt.split('.')[-1]

            ddd_path = os.path.join(data_dir, ndir)

            if not os.path.exists(ddd_path):
                os.mkdir(ddd_path)
                shutil.move(src_path, ddd_path)
                print("文件分类完毕")


# 连接图形化界面
app = QApplication(sys.argv)  # 提供图形化界面的底层管理
w = QMainWindow()
w.resize(400, 300)
w.move(400, 400)  # 启动窗口位置
w.setWindowTitle('文件分类系统')
textEdit = QPlainTextEdit(w)
textEdit.setPlaceholderText("hhhhh")
textEdit.move(30, 30)
textEdit.resize(60, 90)

buttonyuan = QPushButton('输入源文件目录', w)
buttonyuan.resize(100, 38)
buttonyuan.move(40, 200)
buttonyuan.clicked.connect(Sdirectory)

buttonfenlei = QPushButton('输入源文件目录', w)
buttonfenlei.resize(100, 38)
buttonfenlei.move(180, 200)
buttonfenlei.clicked.connect(Tdirectory)

shuchu = QPushButton('确定', w)
shuchu.resize(60, 38)
shuchu.move(100, 250)
shuchu.clicked.connect(hander)
w.show()
app.exec_()
