import cv2

camera = cv2.VideoCapture(0)
face_casecade = cv2.CascadeClassifier(r'D:/pythonobject/人脸识别训练项目/haarcascade_frontalface_default.xml')
while (True):
    ret, frame = camera.read()
    if ret:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_casecade.detectMultiScale(gray_img, 1.3, 3)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            print("(x:", (x + w) / 2, ",y:", (y + h) / 2, ")")
            cv2.imshow("camera", frame);
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
camera.release()
cv2.destroyAllWindows()
