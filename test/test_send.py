import requests

headers = {
    "Host": "huexrb.ngrok.io",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept": "/",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate',
    "Content-Type": "application/x-www-form-urlencoded",
    # 'Content-Length': '91',
    "Origin": "https://huexrb.ngrok.io",
    "Referer": "https://huexrb.ngrok.io/tagger?user=%27wendy%27",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    # Requests doesn't support trailers
    # 'Te': 'trailers',
}

# data = '2021-selected/wendy/2022-09-06_16-06-04-wendy.txt\n2.044 98.253 G TEST2\n98.264 98.764 G TEST2\n'

data = (
    "2021-selected/wendy/"
    + "2022-09-06_16-06-04"
    + "-wendy.txt\n"
    + "2.044 98.253 G TEST2\n98.264 98.764 G TEST2\n"
)
response = requests.post("https://huexrb.ngrok.io/", headers=headers, data=data)
#  verify=False)
print(response.text)
