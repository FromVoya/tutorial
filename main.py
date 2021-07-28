#import library telebot and assigning token
# -*- coding: utf8 -*-
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import dollar_history
import evro,yan,gbp,chf
import datetime
import aiogram

bot=telebot.TeleBot('1912651897:AAELMglzDr1mHZ55dYihitU1VEvBhMm3F5A')



class Currency:
    DOLLAR_RUB = "https://bankiros.ru/convert/usd-rub/1"

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"}
    current_convert_price=0
    difference=0
    def __init__(self):
        self.current_convert_price=float(self.get_currency_price().replace(",","."))
    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "xxx-fast-converter__out"})
        return convert[0].text
    def attend(self):
         full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

         soup = BeautifulSoup(full_page.content, 'html.parser')
         convert = soup.findAll("span", {"class": "xxx-fast-converter__out"})
    def check(self):
        global currency
        currency=float(self.get_currency_price().replace(",","."))

        return str(currency)




time=datetime.datetime.now().hour
privet=" "
if 0 <= time < 6 or 21 <= time <= 23:
    privet = "Доброй ночи"
elif 6 <= time < 10:
    privet = "Доброе утро"
elif 10 <= time < 16:
    privet = "Добрый день"
elif 16 <= time < 21:
    privet = "Добрый день"




@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Курс")
    item2 = types.KeyboardButton("История")
    markup.add(item1,item2)

    bot.send_message(message.from_user.id,f"{privet}",reply_markup=markup)



@bot.message_handler(commands=['Курс'])
def nachalo(message):
    keyboard = types.InlineKeyboardMarkup()
    key_usd = types.InlineKeyboardButton(text="USD", callback_data='USD')
    keyboard.add(key_usd)
    key_eur = types.InlineKeyboardButton(text="EUR", callback_data='EUR')
    keyboard.add(key_eur)
    key_yan = types.InlineKeyboardButton(text="YAN", callback_data='YAN')
    keyboard.add(key_yan)
    key_gbp = types.InlineKeyboardButton(text="GBP", callback_data='GBP')
    keyboard.add(key_gbp)
    key_chf = types.InlineKeyboardButton(text="CHF", callback_data='CHF')
    keyboard.add(key_chf)
    question = f"Какая валюта Вас интересует"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data=="USD":
        bot.send_message(call.from_user.id, f"Курс доллара:  {float(Currency().check())}  рубля")
    elif call.data=="EUR":
        bot.send_message(call.from_user.id, f"Курс евро:  {float(evro.Currency().check())} рубля")
    elif call.data=="YAN":
        bot.send_message(call.from_user.id, f"Курс юаня:  {float(yan.Currency().check())} рубля")
    elif call.data=="GBP":
        bot.send_message(call.from_user.id, f"Курс фунта:  {float(gbp.Currency().check())} рубля")
    elif call.data=="CHF":
        bot.send_message(call.from_user.id, f"Курс франка:  {float(chf.Currency().check())} рубля")
    if call.data=="h_USD":
        bot.send_message(call.from_user.id, f"{dollar_history.usd}")
    elif call.data=="h_EUR":
        bot.send_message(call.from_user.id, f"{dollar_history.eur}")
    elif call.data=="h_YAN":
        bot.send_message(call.from_user.id, f"{dollar_history.yan}")
    elif call.data=="h_GBP":
        bot.send_message(call.from_user.id, f"{dollar_history.gbp}")
    elif call.data=="h_CHF":
        bot.send_message(call.from_user.id, f"{dollar_history.chf}")






@bot.message_handler(commands=['История'])
def seredina(message):
    keyboard = types.InlineKeyboardMarkup()
    key_husd = types.InlineKeyboardButton(text="USD", callback_data='h_USD')
    keyboard.add(key_husd)
    key_heur = types.InlineKeyboardButton(text="EUR", callback_data='h_EUR')
    keyboard.add(key_heur)
    key_hyan = types.InlineKeyboardButton(text="YAN", callback_data='h_YAN')
    keyboard.add(key_hyan)
    key_hgbp = types.InlineKeyboardButton(text="GBP", callback_data='h_GBP')
    keyboard.add(key_hgbp)
    key_hchf = types.InlineKeyboardButton(text="CHF", callback_data='h_CHF')
    keyboard.add(key_hchf)
    question = f"История какой валюты Вас интересует?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)









@bot.message_handler(content_types=['text'])
def start(message):
    if message.text=='Курс':
        nachalo(message)
    elif message.text=="История":
        seredina(message)



bot.polling(none_stop=True,interval=0)