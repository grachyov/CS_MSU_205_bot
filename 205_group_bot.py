#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import time
import random
import BotPrivateConstants

bot = telebot.TeleBot(BotPrivateConstants.api_token)

@bot.message_handler(commands=['shuffled_list'])
def shuffled_list(message):
	shuffled_list = list(BotPrivateConstants.group_list)
	random.shuffle(shuffled_list)
	random_list_string = ""
	for index, person in enumerate(shuffled_list, start = 1):
		random_list_string += str(index) + ". " + person + "\n"
	bot.send_message(message.chat.id, random_list_string)

@bot.message_handler(commands=['group_list'])
def group_list(message):
	group_list_string = ""
	for index, person in enumerate(BotPrivateConstants.group_list, start = 1):
		group_list_string += str(index) + ". " + person + "\n"
	bot.send_message(message.chat.id, group_list_string)	

bot.polling()
while True:
    time.sleep(100)