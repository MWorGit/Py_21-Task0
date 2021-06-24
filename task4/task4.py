import telebot
import config
import http.client
import json

#Init tmp
text1 = ''
text2 = ''
text3 = ''
text4 = ''
text5 = ''
text6 = ''
stopcounter = True

#Get statistic
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}

conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
json = json.loads(data.decode("utf-8"))

def outF(json, i):
    text = ""
    text = list(json[i].items())[14]
    text += list(json[i].items())[12]
    text += list(json[i].items())[10]
    text += list(json[i].items())[2]
    str1 = text[6] + ' : ' + text[7] + '\n'\
           + text[0] + ' : ' + str(text[1]) + '\n'\
           + text[2] + ' : ' + str(text[3]) + '\n'\
           + text[4] + ' : ' + str(text[5]) + '\n\n'
    return str1

#CM-work
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def str_message(message):
    global text1
    global text2
    global text3
    global text4
    global text5

    text1 = outF(json, 1)
    text2 = outF(json, 2)
    text3 = outF(json, 3)
    text4 = outF(json, 4)
    text5 = outF(json, 5)

    bot.send_message(message.chat.id, text1 + text2 + text3 + text4 + text5)

@bot.message_handler(commands=['Turkey'])
def tr_message(message):
    global text1
    text1 = outF(json, 1)
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['Iran'])
def tr_message(message):
    global text2
    text2 = outF(json, 2)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['Indonesia'])
def tr_message(message):
    global text3
    text3 = outF(json, 3)
    bot.send_message(message.chat.id, text3)

@bot.message_handler(commands=['Philippines'])
def tr_message(message):
    global text4
    text4 = outF(json, 4)
    bot.send_message(message.chat.id, text4)

@bot.message_handler(commands=['Iraq'])
def tr_message(message):
    global text5
    text5 = outF(json, 5)
    bot.send_message(message.chat.id, text5)

@bot.message_handler(commands=['updatem'])
def update_message(message):
    global text1
    global text2
    global text3
    global text4
    global text5

    text1 = outF(json, 1)
    text2 = outF(json, 2)
    text3 = outF(json, 3)
    text4 = outF(json, 4)
    text5 = outF(json, 5)
    bot.send_message(message.chat.id, "Данние обновлены!")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     "/start        - запускает программу\n"
                     "/updatem        - обновляет данные\n"
                     "/stp         - останавливает программу\n"
                     "/Turkey     - виводит статистику по Турцыи\n"
                     "/Iran          - виводит статистику по Ирану\n"
                     "/Indonesia    - виводит статистику по Индонезии\n"
                     "/Philippines  - виводит статистику по Филипинам\n"
                     "/Iraq           - виводит статистику по Ираку\n"
                     "/getstats    - получить txt file со статистикой")


@bot.message_handler(commands=['getstats'])
def get_txt_message(message):
    f = open('stats.txt', 'w')
    f.write(text1 + text2 + text3 + text4 + text5)
    f.close()
    file = open('stats.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file.close()


@bot.message_handler(content_types=['text'])
def unno_message(message):
    bot.send_message(message.chat.id, 'Неизвестная команда!'
                                      '\nВведите /help для списка команд.')


@bot.message_handler(content_types=['stp'])
def stop_message(message):
    bot.stop_polling()

bot.polling()
