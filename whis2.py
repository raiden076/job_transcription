""" This file is for automating transcriptions for huex """


import string
import subprocess
from datetime import datetime
from zoneinfo import ZoneInfo

import pysrt
import requests
from tqdm.contrib.telegram import trange

TOKEN = "5557434028:AAGNGR3Mlv7oWS-2TO3nUIwYysplhE34Wso"
CHAT_ID = "-1001753354502"

input_list = open("input.txt").read().splitlines()
input_list.sort()

start = input_list.index(str(input("Enter start file: ")))
end = input_list.index(str(input("Enter end file: ")))


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


def send_message(text):
    method = "sendMessage"
    response_tele = requests.post(
        timeout=5,
        url="https://api.telegram.org/bot{0}/{1}".format(TOKEN, method),
        data={"chat_id": CHAT_ID, "text": text},
    ).json()
    return response_tele


def send_file(text):
    method = "sendDocument"
    response_tele = requests.post(
        timeout=5,
        url="https://api.telegram.org/bot{0}/{1}".format(TOKEN, method),
        data={"chat_id": CHAT_ID, "caption": text},
        files={"document": doc},
    ).json()
    return response_tele


t = trange(start, end, TOKEN=TOKEN, chat_id=str(CHAT_ID), desc="Progress", unit="files")
for y in t:
    i = input_list[y]
    t.set_description("processing " + str(i) + "\n", refresh=True)
    subprocess.run(
        [
            "whisper",
            "./input/" + i + ".mp3",
            "--language",
            "English",
            "--model",
            "large",
            "-o",
            "output",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        check=True,
    )
    subs = pysrt.open("./output/" + i + ".mp3.srt")
    DATA = ""
    length = len(subs)
    for z in range(length):
        DATA = DATA + whole_line(z) + "\n"
    with open("./output.txt", "a") as f:
        f.write(i + "\n\n" + DATA + "\n\n")

    if y > 5332:
        DATA = "2021-selected/wendy/" + i + "-wendy2.txt\n" + DATA
    else:
        DATA = "2021-selected/wendy/" + i + "-wendy.txt\n" + DATA

    response = requests.post("https://huexrb.ngrok.io/", data=DATA, timeout=5)
    if response.status_code == 200:
        send_message(i)


zip_name = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d-%H-%M-%S")

doc = open(zip_name, "rb")
send_file("the latest and the greatest: " + zip_name)
