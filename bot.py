# coding: utf-8
import os
import telebot
from api import get_league, get_partials


bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot do Cartola!")


@bot.message_handler(commands=['liga'])
def send_league_data(message):
    bot.reply_to(message, get_league())


@bot.message_handler(commands=['parciais'])
def send_partials(message):
    bot.reply_to(message, get_partials())

bot.polling()
