import pysrt
from datetime import timedelta
import string
import requests
import os


def get_seconds(time_str):
    hh, mm, ss = time_str.split(":")
    return float(hh) * 3600 + float(mm) * 60 + float(ss)


def get_end_time(line_num):
    return str(get_seconds(str(subs[line_num].end.to_time())))


def get_start_time(line_num):
    return str(get_seconds(str(subs[line_num].start.to_time())))


def get_text(line_num):
    x = subs[line_num].text
    x = x.translate(str.maketrans("", "", string.punctuation))
    return x.upper()


def whole_line(line_num):
    return (
        get_start_time(line_num)
        + " "
        + get_end_time(line_num)
        + " "
        + get_text(line_num)
    )


mylist = open("./input.txt").read().splitlines()
for z in mylist:
    subs = pysrt.open("./21-missing/" + z + ".mp3.srt")
    data = ""
    length = len(subs)
    for i in range(length):
        data = data + whole_line(i) + "\n"
    headers = {
        "Host": "huexrb.ngrok.io",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "/",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://huexrb.ngrok.io",
        "Referer": "https://huexrb.ngrok.io/tagger?user=%27wendy%27",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    data1 = "2021-selected/wendy/" + z + "-wendy.txt\n" + data
    response = requests.post("https://huexrb.ngrok.io/", headers=headers, data=data1)
    print(response.text)
