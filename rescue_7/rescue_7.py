import os

# mylist = open("test.4").read().splitlines()
# for i in mylist:
#     os.system(
#         "wget https://huexrb.ngrok.io/2021-selected/wendy/" + i + ".mp3 -P ./input2/"
#     )


mylistw = open("./rescue_7/input.txt").read().splitlines()
for i in mylistw:
    os.system(
        "wget https://huexrb.ngrok.io/2021-selected/wendy/"
        + i
        + "-wendy.txt -P ./rescue_7/rescue/"
    )
