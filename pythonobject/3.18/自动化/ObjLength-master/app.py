import cv2
import numpy as np

# cv2.IMREAD_COLOR，读取BGR通道数值，即彩色通道，该参数为函数默认值
# cv2.IMREAD_UNCHANGED，读取透明（alpha）通道数值
# cv2.IMREAD_ANYDEPTH，读取灰色图，返回矩阵是两维的
pic = cv2.imread('D:\\pythonobject\\3.18\\自动化\\size-of-objects\\images\\example_01.png', cv2.IMREAD_COLOR)

# 设置比例尺放置范围
scaleH = 20
scaleW = 150

pic_height = pic.shape[0]
pic_width = pic.shape[1]

pic_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

ret, pic_gray = cv2.threshold(pic_gray, 220, 255, cv2.THRESH_BINARY)

# 显示比例尺区域
cv2.line(pic, (pic_width - scaleW, 0), (pic_width - scaleW, scaleH), (0, 0, 0), 2)
cv2.line(pic, (pic_width - scaleW, scaleH), (pic_width, scaleH), (0, 0, 0), 2)

leftScale = 0
rightScale = 0

# 获取比例尺长度
for i in range(scaleW):
    for j in range(scaleH):
        if pic_gray[j][pic_width - scaleW + i] == 0:
            if leftScale != 0:
                break

            leftScale = pic_width - scaleW + i
for i in range(scaleW):
    for j in range(scaleH):
        if pic_gray[j][pic_width - i - 1] == 0:
            if rightScale != 0:
                break

            rightScale = pic_width - i

if leftScale > 0:
    cv2.line(pic, (leftScale, 0), (leftScale, scaleH), (0, 0, 255), 1)

if rightScale > 0:
    cv2.line(pic, (rightScale, 0), (rightScale, scaleH), (0, 0, 255), 1)

leftW = 0
leftH = 0
i = 0
j = 0

for i in range(int(pic_width / 2)):
    for j in range(pic_height):
        # 把比例尺屏蔽
        if j < scaleH and i > (pic_width - scaleW):
            pic_gray[j][i] = 255

        if pic_gray[j][i] == 0:
            if leftW != 0 and leftH != 0:
                break

            leftW = i
            leftH = j

print("Left Edge: " + str(leftW) + ':' + str(leftH))

cv2.line(pic, (leftW, 0), (leftW, pic_height), (0, 0, 255), 1)

rightW = 0
rightH = 0

for i in range(pic_width - 1, int(pic_width / 2) - 1, -1):
    for j in range(pic_height):
        # 把比例尺屏蔽
        if j < scaleH and i > (pic_width - scaleW):
            pic_gray[j][i] = 255

        if pic_gray[j][i] == 0:
            if rightW != 0 and rightH != 0:
                break

            rightW = i
            rightH = j

print("Right Edge: " + str(rightW) + ':' + str(rightH))

cv2.line(pic, (rightW, 0), (rightW, pic_height), (0, 0, 255), 1)

cv2.line(pic, (leftW, leftH), (rightW, rightH), (255, 0, 0), 2)
cv2.line(pic, (leftW, leftH), (rightW, leftH), (0, 255, 0), 2)
cv2.line(pic, (rightW, leftH), (rightW, rightH), (0, 255, 0), 2)

cv2.putText(pic, 'L Edge: ' + str(leftW) + ',' + str(leftH), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
cv2.putText(pic, 'R Edge: ' + str(rightW) + ',' + str(rightH), (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

distance = np.round(np.sqrt(np.square(abs(leftH - rightH)) + np.square(abs(leftW - rightW))))
cv2.putText(pic, 'Pix Len: ' + str(distance), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

cv2.putText(pic, 'Scale Len: ' + str(rightScale - leftScale) + "(10cm)", (10, 105), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

objLen = np.round((distance / (rightScale - leftScale)) * 10)

cv2.putText(pic, 'Obj Len: ' + str(objLen) + "(cm)", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

cv2.imshow('pic', pic)

while True:
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
