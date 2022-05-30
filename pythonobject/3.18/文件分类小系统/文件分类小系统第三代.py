import os
import shutil

print("================欢迎进入文件分类小系统=================")
print("需要分类的的文件夹里面不能包含文件夹，在分类前请先自己备份一份")
# 源文件
src_dir = input('r' + "请输入需要分类的源文件目录:\n")

# 分类文件
data_dir = input('r' + "请输入想要将分完类的文件储存目录:\n")
# 判断分类文件是否存在
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
