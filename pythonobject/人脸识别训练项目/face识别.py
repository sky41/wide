import numpy as np
import cv2 as cv
import sys


camera = cv.VideoCapture(0)
face_casecade = cv.CascadeClassifier(r'D:/python/Scripts/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
# 编辑要调用的方法
def fac_detect_demo():
    # 将图片转换为灰度图
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 人脸检测参量
    face_detector = cv.CascadeClassifier("D:/python/Scripts/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml")
    # 对gray进行识别，人脸检测完成后返回一个人脸区域faces
    faces = face_detector.detectMultiScale(gray)
    # x,y是坐标，w，h是宽度和高度
    for x, y, w, h in faces:
        # 在彩色图像上绘制矩形框，调用rectangle，（x,y）是左上角，(x + w, y + h)右下角，图框颜色BGR绿色，图框宽度
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=3)
        # 画完图框后进行显示
        cv.imshow('result', img)
img = cv.imread('ssss.jpg')#识别图像文件
cv.imshow('input_img', img)
# 调用函数
fac_detect_demo()
cv.waitKey(0)
# 释放内存空间
cv.destroyAllWindows()
