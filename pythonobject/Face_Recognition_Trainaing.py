# ________________________Lets start the project_______________________#

# Importing Modules necessary for the Training
import cv2
import os
import numpy
from PIL import Image
import pickle
import FaceRecognition
# Determining the Base or root directory where our python file is present
# 确定python文件所在的基目录或根目录
BaseDirectory = os.path.dirname(os.path.abspath(__file__))
print(BaseDirectory)

# 我们在操作系统库的帮助下找到了工作目录
# 初始化Images文件夹的路径
ImageDirectory = os.path.join(BaseDirectory, "Training Data")
print(ImageDirectory)

# As the path of the image directory is been found out
# We are going to create an recognizer
# 创建LBPH识别器并开始训练，当然也可以选择Eigen或者Fisher识别器
Recogniser = cv2.face.LBPHFaceRecognizer_create()

# Recogniser is created
# 加载Face Casecade或haarcascade文件来预测图像中的人脸
FaceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# Now the Haarcascade.xml file is loaded

# 创建一个变量CurrentID来初始化我们必须跟踪的图片的id
CurrentId = 0

# 创建字典以存储具有相应标签ID的标签名称
LabelID = {}

# 创建列表以存储标签id数据
YLabel = []
# 创建列表以数组的形式存储图像
XTrain = []

# 现在在找到的映像目录中运行循环
for root, dir, files in os.walk(ImageDirectory):

    # running another loop across files in files that has been found
    for file in files:

        # 实现If语句以仅捕获.jpg文件
        if file.endswith('jpg'):

            # 对于该特定文件，有一个名为persons Name的文件夹
            # #文件夹名初始化为标签名
            label = os.path.basename(root)

            # 添加根目录和文件名以创建文件的完整路径
            path = os.path.join(root, file)
            print(path)
            print(label)

            # 检查标签是否已用ID初始化如果未初始化ID
            if not label in LabelID:
                # Initialising to the label
                LabelID[label] = CurrentId

                # Incrementing the ID
                CurrentId += 1

            ID = LabelID[label]

            # Now Pillow library is used
            # Pillow 模块中的图像对象用于通过给定路径打开图像
            # 平行图像被转换成灰度

            OriginalImage = Image.open(path).convert("L")
            ##正在调整图像大小以更好地理解

            OriginalImage = OriginalImage.resize((550, 550), Image.ANTIALIAS)

            # 将图像转换为numpy数组
            ImageArray = numpy.array(OriginalImage, "uint8")
            print(ImageArray)
            print(LabelID)

            # 使用FaceCascade 检测图像中的多个人脸
            Faces = FaceCascade.detectMultiScale(ImageArray, 1.3, 5)

            for x, y, w, h in Faces:
                # Finding the region of intrest
                ROI = ImageArray[y:y + h, x:x + w]

                # Appending the region of intrest in to Xtrain List
                XTrain.append(ROI)

                # Appending ID in to label list
                YLabel.append(ID)
print(YLabel)
# print(XTrain)

# 现在标签被写入一个pickel文件，可以在识别时进一步使用
with open('Label.pickle', 'wb') as file:
    pickle.dump(LabelID, file)

# 为给定的带有标签id的图像设置训练计算机
Recogniser.train(XTrain, numpy.array(YLabel))

# 将训练过的数据保存到.yml文件中，以便识别
Recogniser.save('Training.yml')