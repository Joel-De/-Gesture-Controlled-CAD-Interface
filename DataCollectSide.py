import cv2
import pathlib
import time

data_dir = "F:\\Hands Hands Hands\\side\\p\\"


imgcount = 1000


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 768)
c = 0
n = 0

time.sleep(3)  # Get set up

while True:

    ret, image = cap.read()

    image = cv2.resize(image, (1280, 720))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show = image

    cv2.rectangle(show, (0, 0), (400, 720), (255, 0, 0), 2)

    cv2.imshow("View", show)

    k = cv2.waitKey(1)
    if k == 27:

        for count in range(imgcount):
            ret, image = cap.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.waitKey(1)

            cropped = image[0:720, 0:400]
            cropped = cv2.resize(cropped, (100, 180))

            cv2.imwrite(data_dir + str(n) + ".jpg", cropped)
            time.sleep(0.01)

            cv2.imshow('View2', cropped)
            cv2.waitKey(1)
            n += 1

        break

while True:

    ret, image = cap.read()

    image = cv2.resize(image, (1280, 720))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show = image

    cv2.rectangle(show, (880, 0), (1280, 720), (255, 0, 0), 2)

    cv2.imshow("View", show)

    k = cv2.waitKey(1)
    if k == 27:

        for count in range(imgcount):
            ret, image = cap.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.waitKey(1)

            cropped = image[0:720, 880:1280]
            cropped = cv2.resize(cropped, (100, 180))
            cv2.imwrite(data_dir + str(n) + ".jpg", cropped)

            time.sleep(0.01)
            cv2.imshow('View2', cropped)
            cv2.waitKey(1)
            n += 1

        break
