import cv2
import pathlib
import tensorflow as tf
import os
import pyautogui as gui
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from tensorflow import keras

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

TrainedTop = keras.models.load_model("TrainedTop.h5")
TrainedSide = keras.models.load_model("TrainedSide.h5")

c = 0

while True:

    ret, image = cap.read()
    test = image
    test = cv2.resize(test, (320,180))

    cv2.imshow("Preview", test)
    cv2.waitKey(1)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    imgBot = image[360:720, 400:880]
    imgTop = image[0:360, 400:880]

    imgTop = cv2.resize(imgTop, (60, 45))
    imgBot = cv2.resize(imgBot, (60, 45))

    ##############################

    imgLeft = image[0:720, 0:400]
    imgRight = image[0:720, 880:1280]

    imgLeft = cv2.resize(imgLeft, (50, 90))
    imgRight = cv2.resize(imgRight, (50, 90))

    ###########################################



    data = np.expand_dims(imgTop, 0)
    predict = TrainedTop.predict(data)

    predict = np.argmax(predict, axis=1)


    if predict[0] == 1:

        gui.moveTo(825, 525)
        gui.drag(0, 70, 0.2, button='middle')

        print("top")



    data = np.expand_dims(imgBot, 0)
    predict = TrainedTop.predict(data)
    predict = np.argmax(predict, axis=1)


    if predict[0] == 1:
        imgBot=cv2.resize(imgBot, (256, 256))

        cv2.imshow("POSITIVE", imgBot)
        gui.moveTo(825, 525)
        gui.drag(0, -70, 0.2, button='middle')

        print("bot")


    data = np.expand_dims(imgRight, 0)
    predict = TrainedSide.predict(data)
    predict = np.argmax(predict, axis=1)

    if predict[0] == 1:
        imgRight=cv2.resize(imgRight, (256, 256))
        cv2.imshow("POSITIVE", imgRight)

        gui.moveTo(825, 525)
        gui.drag(-70, 0, 0.2, button='middle')

        print("Right")

    cv2.waitKey(1)
    data = np.expand_dims(imgLeft, 0)
    predict = TrainedSide.predict(data)
    predict = np.argmax(predict, axis=1)

    if predict[0] == 1:
        imgLeft = cv2.resize(imgLeft, (256,256))
        cv2.imshow("POSITIVE", imgLeft)
        gui.moveTo(825, 525)
        gui.drag(70, 0, 0.2, button='middle')

        print("Left")

    cv2.waitKey(1)

    k = cv2.waitKey(1)
    if k == 27:
        break
