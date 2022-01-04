import python_weather as pw
import asyncio
import googlemaps as gm
import datetime
import variables as v
import urllib.request
import objectpath
import discordwebhook as ds
import json
import tinytuya
def morningwakeup():








    morningdm = str("Good Morning Lewis! Its " + str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + " On " + get_day_word() + " the " + str(datetime.datetime.today().day) + get_day_prefix() + " of " + get_month_word())
    return morningdm
def get_day_word():
    if datetime.datetime.today().weekday() == 0:
        day = "Monday"
    if datetime.datetime.today().weekday() == 1:
        day = "Tuesday"
    if datetime.datetime.today().weekday() == 2:
        day = "Wednesday"
    if datetime.datetime.today().weekday() == 3:
        day = "Thursday"
    if datetime.datetime.today().weekday() == 4:
        day = "Friday"
    if datetime.datetime.today().weekday() == 5:
        day = "Saturday"
    if datetime.datetime.today().weekday() == 6:
        day = "Sunday"
    return day
def get_day_prefix():
    dateday = str(datetime.datetime.today().day)
    if len(dateday) == 2:
        if dateday[1] == "1":
            prefix = "st"
        if dateday[1] == "2":
            prefix = "nd"
        if dateday[1] == "3":
            prefix = "rd"
        if dateday[1] == "4":
            prefix = "th"
        if dateday[1] == "5":
            prefix = "th"
        if dateday[1] == "6":
            prefix = "th"
        if dateday[1] == "7":
            prefix = "th"
        if dateday[1] == "8":
            prefix = "th"
        if dateday[1] == "9":
            prefix = "th"
        if dateday[1] == "0":
            prefix = "th"
    else:
        if dateday == "1":
            prefix = "st"
        if dateday == "2":
            prefix = "nd"
        if dateday == "3":
            prefix = "rd"
        if dateday == "4":
            prefix = "th"
        if dateday == "5":
            prefix = "th"
        if dateday == "6":
            prefix = "th"
        if dateday == "7":
            prefix = "th"
        if dateday == "8":
            prefix = "th"
        if dateday == "9":
            prefix = "th"
        if dateday == "0":
            prefix = "th"
    return prefix
def get_month_word():
    The_month = ""
    themo = datetime.datetime.today().month

    if themo == 1:
        The_month = "January"
    if themo == 2:
        The_month = "February"
    if themo == 3:
        The_month = "March"
    if themo == 4:
        The_month = "April"
    if themo == 5:
        The_month = "May"
    if themo == 6:
        The_month = "June"
    if themo == 7:
        The_month = "July"
    if themo == 8:
        The_month = "August"
    if themo == 9:
        The_month = "September"
    if themo == 10:
        The_month = "October"
    if themo == 11:
        The_month = "November"
    if themo == 12:
        The_month = "December"
    return The_month

def questiondecider(inputsplit):
    responce = ""
    upperword = ""

    inputsplit = inputsplit.split()

    for word in inputsplit:
        upperword = word.upper()
        if upperword == "WHAT" or upperword == "WHAT'S":
            responce = Whatq(inputsplit)
            return responce
        if upperword == "WHERE" or upperword == "WHERE'S" or upperword == "WHERES":
            return 1
        if upperword == "WHO" or upperword == "WHO'S" or upperword == "WHOS":
            return Whosq(inputsplit)
        if upperword == "WHY" or upperword == "WHYS":
            return 1
        if upperword == "WHEN" or upperword == "WHERES":
            return 1
        if upperword == "HOW" or upperword == "HOWS":
            return HowQ(inputsplit)
        if upperword == "GET":
            return Getq(inputsplit)

        if upperword == "TURN":
            return 1
        if upperword == "SET":
            return 1
        if upperword == "BOOK":
            return 1
        if upperword == "CHANGE":
            return 1
        if upperword == "SEND":
            return 1
        if upperword == "IS":
            return 1
        if upperword == "I" or upperword == "I'M" or upperword == "IM":
            reponce = ImQ(inputsplit)
            return reponce
        if upperword == "PLAY":
            return 1
        if upperword == "PAUSE":
            return 1
        if upperword == "STOP" or upperword == "CANCEL" or upperword == "NO":
            return 1
        if upperword == "NUTS":
            return "Sukkon Deezz Nuts"
    return "NULL"

def ImQ(listofwords):
    counter = 0
    for each in listofwords:
        uppwords = each.upper()
        if each.upper() == "GOING":
            return add_to_scedule(listofwords,counter)
        counter += 1
def add_to_scedule(listofwords, counter):
    count = 0
    place = ""

    if listofwords[counter + 1] == "to":
        for each in listofwords:
            if count >= counter + 2:
                if listofwords[count] == "at":
                    diff = count - counter
                    loop = counter + 2
                    while loop < count:
                        place += " " + listofwords[loop]
                        loop += 1

                    time = listofwords[count + 1]
                    countsfor = 0
                    for each_of in listofwords:
                        if countsfor > count + 1:
                            if listofwords[countsfor] == "on":

                                date = listofwords[countsfor + 1]
                        countsfor += 1
            count += 1

        print("your going to" + place + " on " + date + " at " + time)
        return "Added Day"




    else:
        place = listofwords[counter + 1]







def SetQ(listofwords):
    for words in listofwords:
        upperword = words.upper()
        if upperword == "LIGHT" or upperword == "LIGHTS" or upperword == "LIGHT'S":
            for wordst in listofwords:
                upword = wordst.upper()
                if upword == "ON":
                    return lights("ON", "")
                elif upperword == "OFF":
                    return 1
def lights(whatdo, device_id):
    devices = tinytuya.deviceScan()
    if devices != None:
        for each in devices:
            if each.dev_id == device_id:
                print("")




    #if whatdo == "ON":



def HowQ(listofwords):
    for word in listofwords:
        upperword = word.upper()
        if upperword != "HOW":
            if upperword == "GET" or upperword == "GETS":
                how = True
                return looplistofwords(listofwords, "GET", "GO", "MAPS", how)

def looplistofwords(listofwords, searchingforone, searchingfortwo, whattodo, How_):
    count = 0
    place = ""

    for wordsii in listofwords:
        upperword = wordsii.upper()
        if upperword == searchingfortwo or upperword == searchingforone:
            counter = count + 1
            print("found get")
            while counter <= len(listofwords) - 1:
                if counter == len(listofwords) - 1:
                    place = place + listofwords[counter]
                else:
                    place = place + listofwords[counter] + "+"
                counter += 1
            break
        count += 1
    print(place)





    return getdirections(place + ",UK", "15+Cheyne+walk,+CR0+7HH")

def getdirections(place, froms):


    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    API_KEY = 'AIzaSyA9ggMAvvcw2TO89cqYDvz6E4aM79TitTQ'
    origin = froms
    destination = place
    nav_request = 'origin=' + origin +'&destination='+ destination +'&mode=transit&key=' + API_KEY +''
    request = endpoint + nav_request
    print(request)
    responce = urllib.request.urlopen(request).read()
    derections = json.loads(responce)
    jsonnn_tree = objectpath.Tree(derections['routes'])
    steps = tuple(jsonnn_tree.execute('$..steps'))



    #stop = str(departstop).split(',')[2]
    list_to_print = []
    full_directions_list = []
    for legs in steps:

        if "html_instructions" in legs:
            if 'transit_details' in legs:
                details = objectpath.Tree(legs['transit_details'])

                transport_details = tuple(details.execute('$..name'))

                bus_num = tuple(details.execute('$..short_name'))
                splittransdetails = str(transport_details).split(',')


                stop_to = str(splittransdetails[0].split("'")[1])
                stop_from = str(splittransdetails[1].split("'")[1])
                end_and_stop = str(splittransdetails[2].split("'")[1])
                transport_company = str(splittransdetails[3].split("'")[1])
                transport_type = str(splittransdetails[4].split("'")[1])


                if transport_type == "Bus":
                    bus = str(str(bus_num).split("'")[1])
                    direction_step = str(bus + " From " + stop_from + " to " + stop_to)
                else:
                    bus = transport_type
                    direction_step =  transport_type + " From " + stop_from + " to " + stop_to + " via " + transport_company + " Services"
                list_to_print.append(str(bus + " to " + stop_to))
                full_directions_list.append(str(direction_step))















            else:
                if "Take" not in legs['html_instructions'] and "Turn" not in legs['html_instructions'] and "Head" not in legs['html_instructions'] and "Slight" not in legs['html_instructions'] and "Stay" not in legs['html_instructions']:
                    full_directions_list.append(legs['html_instructions'])




    print(list_to_print)
    print(full_directions_list)
    v.directions_saved_full_list = full_directions_list
    v.directions_saved_printabel_list = list_to_print

    list_to_str = ""
    full_to_str = ""
    for each in list_to_print:
         list_to_str += each + ", "
    for each in full_directions_list:
         full_to_str += each + ", "
    v.directions_saved_full_str = full_to_str
    v.directions_saved_printabel_str = list_to_print
    ds.createhook(full_to_str,'https://discord.com/api/webhooks/860160111078932520/ipibKHicpqunwVrUkEtQj_6upUv9BHVrT8sRuVbAZ3zmn9onSGbGiyTTd5CRRRpXmP_B')






    return full_to_str

def Getq(upinput):
    for wordsii in upinput:
        upperword = wordsii.upper()
        if upperword != "GET":
            if upperword == "DIRECTIONS" or upperword == "DIRECTION":
                how = False
                return looplistofwords(upinput, "TOO", "TO", "MAPS", how)

            if upperword == "YURI" or upperword == "YURE":
                return "Yur Retarded"

def Whosq(upinput):
    for wordsii in upinput:
        upperword = wordsii.upper()
        if upperword != "WHO" or upperword != "WHO'S":
            if upperword == "CANDICE":
                return "Can Deez Nuts fit in you mouth"
            if upperword == "YURI" or upperword == "YURE":
                return "Yur Retarded"

def Whatq(upinput):
    for word in upinput:
        upperword = word.upper()

        if upperword != "WHAT" or upperword != "WHAT'S":
            #name
            if upperword == "NAME":

                for wordsii in upinput:
                    upword = wordsii.upper()
                    if upword == "YOUR":
                        return "My Name Is Eve"
                    if upword == "MY":
                        return "Your Name Is Lewis"

            #tempreture
            if upperword == "TEMPERATURE":
                isusingplace = False
                count = 0
                place = ""
                for wordii in upinput:

                    upword = wordii.upper()
                    if isusingplace == True:
                        place = upinput[count + 1]
                    if upword == "IN":
                        isusingplace = True
                    if isusingplace == False:
                        count += 1
                if isusingplace != True:
                    loop = asyncio.get_event_loop()
                    weathertemp = loop.run_until_complete(getweather("London"))
                    output = str("The Tempreture in London is " + str(weathertemp.current.temperature) + ".C")
                    return output
                else:
                    print("hhh")
                    loop = asyncio.get_event_loop()
                    weathertemp = loop.run_until_complete(getweather(place))
                    output = str("The Tempreture in " + place + " is " + str(weathertemp.current.temperature) + ".C")
                    return output



            #weather
            if upperword == "WEATHER":
                isusingplace = False
                count = 0
                place = ""
                for wordii in upinput:

                    upword = wordii.upper()
                    if isusingplace == True:
                        place = upinput[count + 1]
                        print(place)



                    if upword == "IN":

                        isusingplace = True
                    if isusingplace == False:
                        count += 1
                if isusingplace != True:

                    loop = asyncio.get_event_loop()
                    weathertemp = loop.run_until_complete(getweather("London"))
                    output = str("The weather in London is " + weathertemp.forecasts[0].sky_text)
                    return output
                else:

                    loop = asyncio.get_event_loop()
                    weathertemp = loop.run_until_complete(getweather(place))
                    print(weathertemp.forecasts[0].sky_text)
                    output = str("The weather in " + place + " is " + weathertemp.forecasts[0].sky_text)
                    return output
            #time
            if upperword == "TIME":
                isusingplace = False
                count = 0
                place = ""
                for wordii in upinput:

                    upword = wordii.upper()
                    if isusingplace == True:
                        place = upinput[count + 1]
                        print(place)

                    if upword == "IN":
                        isusingplace = True
                    if isusingplace == False:
                        count += 1
                if isusingplace == True:
                    return "CANNOT GET TIME OF PLACE"
                else:
                    time = str(gettimeofhere())
                    return "The time is " + time













def gettimeofhere():
    time = str(datetime.datetime.now().time()).split(":")
    hour = int(time[0])
    min = str(time[1])
    if hour > 12:
        hour = hour - 12
        min = min + " PM"
    else:
        min = min + " AM"
    newtime = str(hour) + ":" + min
    return newtime

async def getweather(place):
    client = pw.Client(format=pw.IMPERIAL)
    weather = await client.find(place)



    await client.close()
    return weather









