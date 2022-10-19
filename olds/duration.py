import os

mylist = open("test.4").read().splitlines()
mylist = list(dict.fromkeys(mylist))
for i in mylist:
    os.system("echo " + i + ">> duration.txt")
    os.system(
        "ffprobe -i input/"
        + i
        + '.mp3 -show_entries format=duration -v quiet -of csv="p=0" >> duration.txt'
    )
    os.system('echo "" >> duration.txt')
