import os
from os import path as pth
from sys import argv


def open_programs():
    file_name = '\\' + pth.basename(argv[0])
    path = argv[0].replace(file_name, '')
    if 'programs' not in os.listdir(path):
        os.mkdir('programs')
    path = path + '\\progras'
    if len(os.listdir(path)) == 0:
        os.startfile(path)
    else:
        for i in os.listdir(path):
            os.startfile(path+'\\'+i)
