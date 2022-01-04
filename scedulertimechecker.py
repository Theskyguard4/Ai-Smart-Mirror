import variables as v
import datetime as dt
import hardcodedvoiceinputs as hr
import createresponce as cr
import voicerecording as vs
import os
import textfile as tf
from pygame import mixer



import facerecog as fr

def clear_sc_file():
    scedule_file = open("scedule", "r").readlines()
    with open("scedule", 'r+') as f:
        f.truncate(0)

    new_scedule = []
    for each in scedule_file:
        split_of_each_line = each.split()
        try:
            if split_of_each_line[0] == "-scedule":
                date = split_of_each_line[1].split("/")
                if int(date[2]) < dt.datetime.today().year:
                    pass
                else:
                    if int(date[1]) < dt.datetime.today().month:
                        pass
                    else:
                        if int(date[0]) < dt.datetime.today().day:
                            pass
                        else:
                            new_scedule.append(each)


        except:
            print("NO LIne")
    for each in new_scedule:
        tf.appendtotxt(each, "scedule", False)










def load_day():
    clear_sc_file()
    alarms = tf.read_file("Alarms")
    today = hr.get_day_word()
    for each in alarms:
        splitline = each.split()

        if splitline[0] == today:
            os.environ["Todays_alarm"] = splitline[1]
            return splitline[1]


def Alarm_Play():

    mixer.init()
    mixer.music.load('iPhone Morning Alarm Sound Effect (Annoying) - IOS Ringtone Sound Effect (HD) _ Sound Effects.mp3') # you may use .mp3 but support is limited
    mixer.music.play()

def check_alarms():
    time = str(str(dt.datetime.today().hour) + ":" + str(dt.datetime.today().minute))
    if str(os.environ.get("Todays_alarm").split(":")[0]) == str(dt.datetime.today().hour) and str(
            dt.datetime.today().minute) == str(os.environ.get("Todays_alarm").split(":")[1]):
        return True
    return False

def timecheck():
    if dt.datetime.today().hour > 6:
        if "True" in os.environ.get('Awake_Yet'):
            if "False" in os.environ.get('wokesent'):
                os.environ['wokesent'] = "True"
                return "MORNING"
            else:
                return vs.go()
        os.environ['Awake_yet'] = "True"
        return "NULL"
    return "NULL"


def constant_check():
    if dt.datetime.today().hour < 5 and dt.datetime.today().hour > 4:
        if os.environ.get('Awake_Yet') == "True" or os.environ.get("wokesent") == "True":
            os.environ['Awake_Yet'] = "False"
            os.environ['wokesent'] = "False"


def Calender():
    print(dt.datetime.today().date())
    split = str(dt.datetime.today().date()).split("-")
    if str(split[1][0]) == "0":
        split[1] = split[1][1]
    date = split[2] + "/" + split[1] + "/" + split[0]
    return date


def Gettodaysthings(date):
    filep = str(os.path.abspath(os.getcwd()))
    file_path = filep.split("\\")[0] + chr(92) + filep.split("\\")[1]

    file = str(file_path + chr(92) + "scedule.txt")

    print(file)

    file1 = open(file, "r").readlines()
    count = 0

    for each in file1:
        print(each)
        if count != 0:

            line = each.split(" ")
            if line[1] == date:
                return line[2]
        count += 1
    return "NULL"


def printtime():
    if os.environ.get("Time") != None:
        if str(str(dt.datetime.today().hour) + ":" + str(dt.datetime.today().minute) + "   ") != os.environ.get("Time"):
            os.environ["Time"] = str(str(dt.datetime.today().hour) + ":" + str(dt.datetime.today().minute) + "   ")
            return "TIME"

    else:
        os.environ["Time"] = str(
            str(dt.datetime.today().hour) + ":" + str(dt.datetime.today().minute) + "   ")
        return "TIME"


def isdatevalid(date_split):
    validdate = False
    if dt.datetime.today().year < int(date_split[2]):
        validdate = True
    elif dt.datetime.today().year == int(date_split[2]):
        if dt.datetime.today().month > int(date_split[1]):
            validdate = False
        elif dt.datetime.today().month > int(date_split[1]):
            if dt.datetime.today().day < int(date_split[0]):
                validdate = True
            else:
                validdate = False

    return validdate
