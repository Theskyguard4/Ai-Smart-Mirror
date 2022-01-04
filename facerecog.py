import numpy as np
import cv2
import datetime
import scedulertimechecker as sc
import variables as v
import voicerecording as vs
import hardcodedvoiceinputs as hr
import winsound as ws
import os
import time as tm









def mainrec():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height
    count = 0
    trys = 0


    while True:
        sc.constant_check()
        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        if count == 0:
            if sc.check_alarms() == True:
                if os.environ.get('Awake_yet') == False:
                    sc.Alarm_Play()

        if len(faces) > 0:
            if count < 40:
                count += 1
        else:
            if count != 0:
                count -= 1
        #cv2.imshow('video', img)
        if count > 15:
            print("looking at screen")
            words = sc.timecheck()
            if words == "MORNING":
                return words





            if words != "NULL":
                print("INPUT OKAY!")

                return words

            else:
                print("INPUT NOT OKAY")
                return "NULL"



            count = 0
        else:
            if count == 0:
                if sc.printtime() == "TIME":
                    return "TIME"








            if datetime.datetime.today().hour > 14 and os.environ.get("Awake_Yet") == "False":
                os.environ["Awake_Yet"] = "True"
                os.environ["wokesent"] = "True"
            if datetime.datetime.today().hour > 4 and datetime.datetime.today().hour < 5:
                os.environ["Awake_Yet"] = "False"
                os.environ["wokesent"] = "False"














    cap.release()
    cv2.destroyAllWindows()

