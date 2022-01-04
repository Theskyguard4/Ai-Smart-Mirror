import tkinter as tk
import subprocess
import threading
#import dicordbot
from tkinter import *
import time as tm
import facerecog as fr

import os
import hardcodedvoiceinputs as hr
import variables as v
import scedulertimechecker as st
import discordwebhook as dw
import datetime
class display():
    def creategui(self):
        gui = Tk()
        gui.resizable(FALSE, FALSE)
        return gui

    def settitle(self, gui):
        gui.title("hello world")
        return gui

    def showdisplay(self, gui):
        gui.update()
    def Sizeset(self, gui):
        gui.geometry('1024x600')

    def SetLabel(self, gui, message, backcolour, fontcolour, fontsize):

        label = Label(gui, text=message, font=('Bahnschrift SemiBold', fontsize),bg=backcolour,fg= fontcolour, wraplength=1000)

        label.grid(column=0, row=0)
        label.pack
        return label

    def SetBackColour(self, gui, colour):

        gui.configure(bg=colour)
        return gui

    def setfontsize(self, rp, lines):
        if len(rp) > 100:
            fonts = 1000 / (len(rp)/ 7)
        else:
            if len(rp) < 5:
                fonts = 1000 / len(rp)
            else:
                fonts = 1000 / (len(rp) / 2)









        print(fonts)


        return int(fonts)
    def clearlabel(self, label):
        label.config(text="")
        self.showdisplay(self, gui)
    def updatelabel(self, label, text, gui):
        fonts = self.setfontsize(display, text)
        label.config(text=text, font=('Bahnschrift SemiBold', fonts), wraplength=1000)
        self.showdisplay(self, gui)

    def labellines(self, rp):
        lines = 10

        return lines






if __name__ == "__main__":
    st.load_day()

    os.environ["TodayDate"] = st.Calender()
    colour = 'black'
    fontcolour = "#49A"
    gui = display.creategui(display)
    lines = 1

    gui = display.settitle(display, gui)
    display.Sizeset(display, gui)
    display.SetBackColour(display, gui, colour)

    display.showdisplay(display, gui)

    while True:
        if datetime.datetime.now().hour == 1:
            st.load_day()
        print(os.environ.get("TodayDate"))
        if str(os.environ.get("TodayDate")) != str(datetime.datetime.today().date()):
            os.environ["TodayDate"] = st.Calender()


        input = fr.mainrec()


        if input != "NULL":
            if input == "MORNING":
                Todays = st.Calender()
                todays_things = st.Gettodaysthings(str(os.environ.get("TodayDate")))
                if todays_things == "NULL":
                    responce = hr.morningwakeup()
                else:
                    responce = hr.morningwakeup() + " and today you are " + todays_things + " at "
            elif input == "TIME":
                responce = os.environ.get("Time")





            else:
                responce = hr.questiondecider(input)
            if responce != "NULL":
                print(responce)

                lines = display.labellines(display, responce)
                fontsize = display.setfontsize(display, responce, lines)
                if "TIME" in input or "MORNING" in input:
                    input = input
                else:

                    dw.createhook(
                        " You Said: '" + input + "' and i responded with: '" + responce + "'",
                        "https://discord.com/api/webhooks/860193209468190731/1nJtam1Qm1RT6OsdyJHzs7F0arGduvHr1Ovb6TzSLYlPZF1Vr9yutKhcPdadz7ZK8N8N"
                    )



                label = ""

                label = display.SetLabel(display, gui, responce, colour, fontcolour, fontsize)
                display.showdisplay(display, gui)
                os.environ["msg_displayed"] = "True"

                tm.sleep(10)
                if input != "TIME":
                    display.clearlabel(display, label)
                    os.environ["msg_displayed"] = "False"


            else:
                dw.createhook(" ERROR CODE: 'NULL' RESPONCE", "https://discord.com/api/webhooks/860189712953507912/PuMx60XpDdZ8GUv_0R5qQUnTwEHgfT8fv75pwGhpxCgkxEzvFt_QaTKe5J-Gd4KRlHTm")
                print("ERROR CODE: 'NULL'")
                display.clearlabel(display, label)
                os.environ["msg_displayed"] = "False"

















    tm.sleep(10)








