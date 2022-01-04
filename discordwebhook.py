from dhooks import Webhook
import datetime
def createhook(input, url):

    try:
        hook = Webhook(url)

        hook.send("[" + str(datetime.datetime.today().now()) + "]" + str(input))
    except:
        print("ERROR CODE: WEBHOOK")








