import cv2 as cv


image = cv.imread("D:/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg")
cv.imshow("input",image)
h,w =image.shape[:2]
detector = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_alt.xml")
detector.detectMultiScale(image,scaleFactor=1.09,minNeighbors=3,
                          minSize=(30,30),maxSize=(w//2,h//2))
for x,y, width, height in faces:
    cv.rectangle(image,(x,y),(x+width,y+height),(0,0,225),2,cv.LINE_8,0)
cv.imshow("faces", image)
cv.waitKey(0)
cv.destroyAllWindows()