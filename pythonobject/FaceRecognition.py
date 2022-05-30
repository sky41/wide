import pickle
import cv2
import numpy

# 3打开摄像头
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # 人脸
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')  # 人眼
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')  # 微笑
while True:
    # 读取该帧的画面
    ret, img = capture.read()
    # 6灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 7检查人脸
    faces = face_cascade.detectMultiScale(gray, 1.1, 3, 0, (120, 120))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
        face_area = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_area, 1.3, 10)
        # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        for (ex, ey, ew, eh) in eyes:
            # 画出人眼框，绿色，画笔宽度为1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

        smile = smile_cascade.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=50, minSize=(50, 50),
                                               flags=cv2.CASCADE_SCALE_IMAGE)
        # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        for (ex, ey, ew, eh) in smile:
            # 画出人眼框，绿色，画笔宽度为1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
            cv2.putText(img, 'Smile', (x, y - 7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
    # 9显示图片
    cv2.imshow("My_按q退出", img)
    # 10暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
# 11释放资源
capture.release()
# #12销毁窗口
cv2.destoryAllWindows()
Webcam = cv2.VideoCapture(0)
# 加载OpenCV人脸检测分类器Haar
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

Recognizer = cv2.face.LBPHFaceRecognizer_create()
Recognizer.read('Training.yml')

Labels = {}

with open('Label.pickle', 'rb') as file:
    OriginalLabel = pickle.load(file)
    Labels = {v: k for k, v in OriginalLabel.items()}

while (True):
    Return, Frame = Webcam.read()  # 读取该帧的画面
    Frame = cv2.flip(Frame, 1)

    GrayScale = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)  # 6灰度处理
    Faces = face_cascade.detectMultiScale(GrayScale, 1.3, 5)  # 检查人脸
    for X, Y, W, H in Faces:
        ROI_GRAY = GrayScale[Y:Y + H, X:X + W]
        ROI_COLOR = Frame[Y:Y + H, X:X + W]

        ID, Confidence = Recognizer.predict(ROI_GRAY)  # 预测函数
        if Confidence >= 45:
            print(Labels[ID])
            cv2.putText(Frame, Labels[ID], (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.rectangle(Frame, (X, Y), (X + W, Y + H), (255, 0, 0), 1)
    # 9显示图片
    cv2.imshow('Image', Frame)
    # 10暂停窗口
    if cv2.waitKey(1) == ord('q'):
        break
# 11释放资源
Webcam.release()
# #12销毁窗口
cv2.destroyAllWindows()
