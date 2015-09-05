#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time

timetable = json.load(open("timetable.json"))
subjects = json.load(open("subjects.json"))
short_subjects = json.load(open("short_subjects.json"))

def get_subjects(day):
    return timetable[day]["classes"]


def get_today_subjects():
    day = time.localtime().tm_wday
    return get_subjects(day)


def get_tomorrow_subjects():
    day = (time.localtime().tm_wday + 1) % 7
    return get_subjects(day)


def make_long_subject(subject):
    result = []
    if "start" in subject and "end" in subject:
        result.append("{} — {}".format(subject["start"], subject["end"]))
    result.append(subjects[subject["subject"]])
    if "room" in subject:
        result.append(subject["room"])
    return ", ".join(result)


def make_short_subject(subject):
    result = short_subjects[subject["subject"]]
    if "room" in subject:
        result = u"{:4} {}".format(subject["room"], result)
    return result
