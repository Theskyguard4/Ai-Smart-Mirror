import discord
import textfile as tf
import datetime as dt
client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('-scedule'):
        content = str(message.content).split()
        date = content[1]
        date_split = date.split("/")
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


        if validdate == True:
            tf.appendtotxt(message.content, 'scedule', True)
            await message.channel.send('ADDED')
        else:
            await message.channel.send('INVALID: DATE')








client.run('ODYwMjM2MDY2MTMyNTkwNjEy.YN4TRA.d-da6_4W1o4gqv2xRXo44Cw-Gbk')
