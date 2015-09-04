#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import time
import random
import BotPrivateConstants

bot = telebot.TeleBot(BotPrivateConstants.api_token)

commands_with_description = [
	"/group_list - Список группы",
	"/shuffled_list - Перемешанный список группы",
	"/random_person - Случайный человек",
]

@bot.message_handler(commands = ['shuffled_list'])
def shuffled_list(message):
	shuffled_list = list(BotPrivateConstants.group_list)
	random.shuffle(shuffled_list)
	random_list_string = ""
	for index, person in enumerate(shuffled_list, start = 1):
		random_list_string += str(index) + ". " + person + "\n"
	bot.send_message(message.chat.id, random_list_string)

@bot.message_handler(commands = ['group_list'])
def group_list(message):
	group_list_string = ""
	for index, person in enumerate(BotPrivateConstants.group_list, start = 1):
		group_list_string += str(index) + ". " + person + "\n"
	bot.send_message(message.chat.id, group_list_string)

@bot.message_handler(commands = ['random_person'])
def random_person(message):
	bot.send_message(message.chat.id, random.choice(BotPrivateConstants.group_list))

@bot.message_handler(commands = ['help', 'start'])
def introduction(message):
	intro_message = "Я помощник 205 группы.\nСделайте меня лучше: https://github.com/grachyov/CS_MSU_205_bot\n\nЯ уже отвечаю на команды:\n\n"
	for command in commands_with_description:
		intro_message += command + "\n"
	bot.send_message(message.chat.id, intro_message, True)

@bot.message_handler(commands = ['today'])
def today(message):
    timetable = "\n".join(
        map(timetable.make_short_subject,
            timetable.get_today_subjects()))
    bot.send_message(message.chat.id, timetable)

@bot.message_handler(commands = ['tomorrow'])
def tomorrow(message):
    timetable = "\n".join(
        map(timetable.make_short_subject,
            timetable.get_tomorrow_subjects()))
    bot.send_message(message.chat.id, timetable)

bot.polling()
while True:
    time.sleep(100)
