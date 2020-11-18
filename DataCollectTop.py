import cv2
import pathlib
import time
#Save Location
data_dir = "F:\\Hands Hands Hands\\top\\p\\"

imgcount = 1000

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 768)
c = 0
n = 0

time.sleep(3)  # Get set up

print("ran")

while True:

    ret, image = cap.read()

    image = cv2.resize(image, (1280, 720))

    show = image

    cv2.rectangle(show, (400, 0), (880, 360), (255, 0, 0), 2)

    cv2.imshow("View", show)

    k = cv2.waitKey(1)
    if k == 27:

        for count in range(imgcount):
            ret, image = cap.read()

            cv2.waitKey(1)

            cropped = image[0:360, 400:880]
            cropped = cv2.resize(cropped, (120, 90))

            cv2.imwrite(data_dir + str(n) + ".jpg", cropped)

            print(n)
            time.sleep(0.01)
            cv2.imshow('View1', cropped)
            cv2.waitKey(1)
            n += 1

        break

while True:

    ret, image = cap.read()

    image = cv2.resize(image, (1280, 720))

    show = image

    cv2.rectangle(show, (400, 360), (880, 720), (255, 0, 0), 2)

    cv2.imshow("View", show)

    k = cv2.waitKey(1)
    if k == 27:

        for count in range(imgcount):
            ret, image = cap.read()

            cv2.waitKey(1)

            cropped = image[360:720, 400:880]
            cropped = cv2.resize(cropped, (120, 90))
            cv2.imwrite(data_dir + str(n) + ".jpg", cropped)

            cv2.imshow('View1', cropped)
            cv2.waitKey(1)
            n += 1
            print(n)
            time.sleep(0.01)

        break
