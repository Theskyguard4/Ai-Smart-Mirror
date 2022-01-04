import pyttsx3 as pt
import voicerecording as vs

def ttsstart(tosay):
    engine = pt.init()
    engine.say(tosay)
    engine.runAndWait()




