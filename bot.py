# -*- coding: utf-8 -*-
import telebot;
from telebot import types;
bot = telebot.TeleBot("1315642306:AAGrnAPBjIkMFQg_hA79j7FBR46INhtFRU0")
@bot.message_handler(commands=['start'])
def start(message):
  keyboard = types.InlineKeyboardMarkup();
  key_ru = types.InlineKeyboardButton(text='RU', callback_data='ru');
  keyboard.add(key_ru);
  key_en= types.InlineKeyboardButton(text='EN', callback_data='en');
  keyboard.add(key_en);
  bot.send_message(message.from_user.id, "\xF0\x9F\x91\x8B", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "ru":
        bot.send_message(call.message.chat.id, 'Привет! Я TL;DR бот! Нужно краткое содержание текста? Просто вставьте его сюда или прикрепите файл в формате pdf.');
    elif call.data == "en":
        bot.send_message(call.message.chat.id, 'Hi there! I\'m the TL;DR bot, I can summarize the text for You. Just copy it here or attach a pdf file.');
bot.polling();
