# import os

# # mylist = open("test.4").read().splitlines()
# # for i in mylist:
# #     os.system(
# #         "wget https://huexrb.ngrok.io/2021-selected/wendy/" + i + ".mp3 -P ./input2/"
# #     )


# mylistw = open("./rescue_7/input.txt").read().splitlines()
# for i in mylistw:
#     os.system(
#         "wget https://huexrb.ngrok.io/2021-selected/wendy/"
#         + i
#         + "-wendy.txt -P ./rescue_7/rescue/"
#     )
import requests


token = "5557434028:AAGNGR3Mlv7oWS-2TO3nUIwYysplhE34Wso"
method = "sendMessage"
myuserid = -1001753354502
text = "Hello World"
response = requests.post(
    url="https://api.telegram.org/bot{0}/{1}".format(token, method),
    data={"chat_id": myuserid, "text": text},
).json()
print(response["result"]["message_id"])
message_id = response["result"]["message_id"]

token = "5557434028:AAGNGR3Mlv7oWS-2TO3nUIwYysplhE34Wso"
method = "editMessageText"
myuserid = -1001753354502
text = "Hello World 2"
response = requests.post(
    url="https://api.telegram.org/bot{0}/{1}".format(token, method),
    data={"chat_id": myuserid, "message_id": message_id, "text": text},
).json()
print(response)
