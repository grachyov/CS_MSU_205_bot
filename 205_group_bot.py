#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bot_private_constants
import timetable

import telebot

import json
import time
import random
import re

bot = telebot.TeleBot(bot_private_constants.api_token)

S = json.load(open("strings.json"))

commands_with_description = [
	"/group_list — Список группы",
	"/shuffled_list — Перемешанный список группы",
	"/random_person — Случайный человек",
	"/today — Расписание на сегодня",
	"/tomorrow — Расписание на завтра"
]

@bot.message_handler(commands = ['shuffled_list'])
def shuffled_list(message):
	shuffled_list = list(bot_private_constants.group_list)
	random.shuffle(shuffled_list)
	random_list_string = ""
	for index, person in enumerate(shuffled_list, start = 1):
		random_list_string += str(index) + ". " + person + "\n"
	bot.send_message(message.chat.id, random_list_string)

@bot.message_handler(commands = ['group_list'])
def group_list(message):
	group_list_string = ""
	for index, person in enumerate(bot_private_constants.group_list, start = 1):
		group_list_string += str(index) + ". " + person + "\n"
	bot.send_message(message.chat.id, group_list_string)

@bot.message_handler(commands = ['random_person'])
def random_person(message):
	bot.send_message(message.chat.id, random.choice(bot_private_constants.group_list))

@bot.message_handler(commands = ['help', 'start'])
def introduction(message):
	intro_message = "Я помощник 205 группы.\nСделайте меня лучше: https://github.com/grachyov/CS_MSU_205_bot\n\nЯ уже отвечаю на команды:\n\n"
	for command in commands_with_description:
		intro_message += command + "\n"
	bot.send_message(message.chat.id, intro_message, True)

@bot.message_handler(commands = ['today'])
def today(message):
    timetable_string = "\n".join(
        map(timetable.make_long_subject,
            timetable.get_today_subjects()))
    bot.send_message(message.chat.id, timetable_string)

@bot.message_handler(commands = ['tomorrow'])
def tomorrow(message):
    timetable_string = "\n".join(
        map(timetable.make_long_subject,
            timetable.get_tomorrow_subjects()))
    bot.send_message(message.chat.id, timetable_string)

@bot.message_handler(commands = ['timetable'])
def show_timetable(message):
    timetable_string = ""
    for day, dayname in enumerate(S['weekdays'][:-1]):
        timetable_string += "{}\n{}\n\n".format(
                dayname,
                "\n".join(
                    map(timetable.make_long_subject,
                        timetable.get_subjects(day))))
    bot.send_message(message.chat.id, timetable_string)

@bot.message_handler(commands = ['now'])
def tomorrow(message):
    subject, tm = timetable.get_next_subject()
    if tm < 0:
        fmt = S["next_subject"]
    else:
        fmt = S["current_subject"]
    interval = "{:02}:{:02}".format(abs(int(tm)) % 60, abs(int(tm)) // 60)
    message_string = fmt.format(subject=timetable.make_inline_subject(subject),
            interval=interval)
    bot.send_message(message.chat.id, message_string)

@bot.message_handler(regexp='(?i)(?=Кто|Кого)(.*?)\?$')
def answer_who_is_question(message):
    bot.send_message(message.chat.id, random.choice(bot_private_constants.group_list))

@bot.message_handler(regexp='(?i)Teorver( [0-9]\d*\.[0-9]\d*)+')
def send_task_pic(message):
    for task in re.findall("([0-9]\d*\.[0-9]\d*)", message.text):
        with open('Taskbooks/Statistics/Zubkov/' + task + '.png', 'rb') as pic:
            bot.send_photo(message.chat.id, pic)

bot.polling(none_stop=True)
while True:
    time.sleep(100)
