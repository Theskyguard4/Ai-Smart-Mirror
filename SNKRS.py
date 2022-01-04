import datetime
import json
import requests
def getCalendar():
    today = datetime.datetime.now().strftime("%Y-%m-%d-00-00")
    session = requests.post(str("https://www.nike.com/gb/launch?s=upcoming"))

    decoded_resp = json.loads(session.text)
    # you can do whatever you want with this
    print(decoded_resp)

getCalendar()