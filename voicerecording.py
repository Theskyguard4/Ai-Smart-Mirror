import speech_recognition as sr
import cv2
import winsound as ws
import discordwebhook as dw
import datetime as dt
#import facerecog as fr
# obtain audio from the microphone
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
count = 0
voiceinput = ""
def go():

    r = sr.Recognizer()


    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=4)
        ws.MessageBeep(-1)
        print("Say something!")
        audio = r.listen(source)



        if islooking() == True:
            try:

                voiceinput = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said " + voiceinput)


                return voiceinput





            except sr.UnknownValueError:
                dw.createhook(" ERROR CODE: Could Not Understand Audio", "https://discord.com/api/webhooks/860189712953507912/PuMx60XpDdZ8GUv_0R5qQUnTwEHgfT8fv75pwGhpxCgkxEzvFt_QaTKe5J-Gd4KRlHTm")
                print("Google Speech Recognition could not understand audio")

                return "NULL"
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                dw.createhook(" ERROR CODE: Could Not Get Request Of Voice reg From Google", "https://discord.com/api/webhooks/860189712953507912/PuMx60XpDdZ8GUv_0R5qQUnTwEHgfT8fv75pwGhpxCgkxEzvFt_QaTKe5J-Gd4KRlHTm")
                return "NULL"
            except:
                print("No input")
        else:
            return "NULL"

#checks if person still looking, then will do command
def islooking():
    counter = 20
    while True:
        ret, img = cap.read()

        gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces2 = faceCascade.detectMultiScale(
            gray2,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        #if len(faces2) > 0:
           # counter += 1
            #if counter >= 30:
        print("still looking at screen")
        return True
        #else:
        #    counter -= 1
        #    if count <= 0:
        #        print("No longer looking, canceling")
        #        return False



def isaskingme(voiceinput):
    splitinputby_ = voiceinput.split()
    word = splitinputby_[0]
    wordupper = word.upper()
    if wordupper == "EVEE":
        print("EVEE")
        return True
    if wordupper == "EVE":
        print("EVE")
        return True
    if wordupper == "EEVEE":
        print("EEVEE")
        return True
    if wordupper == "EEVE":
        print("EEVE")
        return True
    print("no eve found")
    return False













