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
    result = subjects[subject["subject"]]
    if "room" in subject:
        result += ", аудитория " + subject["room"]
    return result


def make_short_subject(subject):
    result = short_subjects[subject["subject"]]
    if "room" in subject:
        result = subject["room"] + " " + result
    return result
