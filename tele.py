import os
import pickle

dirc = os.listdir("input/wendy")

start_f = "2022-10-03_21-44-13"
end_f = "2022-10-03_22-17-06"


def remove_ext_list(list):
    tmp_list = []
    list.sort()
    for z in list:
        tmp_list.append(os.path.splitext(z)[0])
    return tmp_list


# print(remove_ext_list(dirc))
in_list = remove_ext_list(dirc)
print((remove_ext_list(dirc)).index("2022-10-05_23-21-07"))
start = in_list.index(start_f)
end = in_list.index(end_f)
for i in range(start, end):
    print(in_list[i])
