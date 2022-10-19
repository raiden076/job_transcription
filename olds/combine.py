import os

os.system("rm *output*")
os.system("touch $(date '+%Y-%m-%d-%H:%M:%S')_output.txt")
directory = os.scandir("tempoutput3")
entries = [it.name for it in directory]
for i in entries:
    x = i
    os.system("echo " + x + ">> *output.txt")
    os.system("cat tempoutput3/" + x + ">> *output.txt")
    os.system('echo "" >> *output.txt')
    os.system('echo "" >> *output.txt')
    os.system('echo "" >> *output.txt')
