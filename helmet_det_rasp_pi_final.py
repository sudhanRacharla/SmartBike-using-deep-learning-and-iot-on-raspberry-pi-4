import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import cv2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

# change model path

mymodel = load_model(r'C:\PycharmProjects\Major\hd-models\mymodel4.h5')

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
temp=0
flag=0
while cap.isOpened():
    _, img = cap.read()
    face = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in face:
        face_img = img[y:y + h, x:x + w]
        cv2.imwrite('temp2.jpg', face_img)
        test_image = image.load_img('temp2.jpg', target_size=(150, 150, 3))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        pred = mymodel.predict(test_image)[0][0]
        if temp==0:
            if pred == 1:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, 'NO HELMET', ((x + w) // 2, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("no helmet")
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, 'HELMET', ((x + w) // 2, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                print("helmet")
                temp + 1
                GPIO.output(32,GPIO.HIGH)
        else:
            GPIO.output(17,True)
            _, img = cap.read()
            face = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in face:
                face_img = img[y:y + h, x:x + w]
                cv2.imwrite('temp2.jpg', face_img)
                test_image = image.load_img('temp2.jpg', target_size=(150, 150, 3))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis=0)
                pred = mymodel.predict(test_image)[0][0]
                if pred != 1:
                    GPIO.output(17,False)
                    break
                else:
                    flag+1
                if flag==8:
                    GPIO.output(32,GPIO.LOW)
                    flag=0
    cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
