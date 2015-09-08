#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from pluralization import s1, s2

timetable = json.load(open("timetable.json"))
subjects = json.load(open("subjects.json"))
short_subjects = json.load(open("short_subjects.json"))

def get_subjects(day):
    return timetable[day]["classes"]


def get_today_subjects():
    day = time.localtime().tm_wday
    return get_subjects(day)


def get_time_delta(tm1, tm2):
    t = lambda x: time.mktime(time.strptime(x, "%H:%M"))
    return t(tm2) - t(tm1)


def get_next_subject():
    now = time.strftime("%H:%M")

    if time.localtime().tm_wday == 6:
        return None, get_time_delta(now, "00:00") + 24 * 3600

    subjects = get_today_subjects()
    for x in range(len(subjects)):
        if is_now(now, subjects[x]):
            return subjects[x], get_time_delta(subjects[x]["end"], now)
        if is_later(now, subjects[x]):
            return subjects[x], get_time_delta(now, subjects[x]["start"])
    if time.localtime().tm_wday == 6:
        return None, get_time_delta(now, "00:00") + 24 * 3600
    return None, 0


def get_tomorrow_subjects():
    day = (time.localtime().tm_wday + 1) % 7
    return get_subjects(day)


def is_now(tm, sbj):
    return (get_time_delta(tm, sbj["start"]) <= 0 and
            get_time_delta(tm, sbj["end"]) >= 0)


def is_later(tm, sbj):
    return get_time_delta(tm, sbj["start"]) > 0


def make_long_subject(subject):
    result = []
    if "start" in subject and "end" in subject:
        result.append("{}-{}".format(subject["start"], subject["end"]))
    result.append(subjects[subject["subject"]])
    if "room" in subject:
        result.append(subject["room"])
    return ", ".join(result)


def make_inline_subject(subject):
    result = []
    result.append(subjects[subject["subject"]].lower())
    if "room" in subject:
        result.append(subject["room"])
    return ", ".join(result)


def make_short_subject(subject):
    result = short_subjects[subject["subject"]]
    if "room" in subject:
        result = u"{:4} {}".format(subject["room"], result)
    return result


def make_human_time(tm):
    hours, mins = tuple(map(int, tm.split(':')))
    if hours > 0:
        if mins > 0:
            return "{} час{} {} минут{}".format(hours, s1(hours),
                    mins, s2(mins))
        else:
            return "{} час{}".format(hours, s1(hours))
    else:
        return "{} минут{}".format(mins, s2(mins))
