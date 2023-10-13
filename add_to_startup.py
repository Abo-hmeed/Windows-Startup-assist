from sys import argv
from shutil import copy
from winshell import startup
from os import listdir
from os import path as pth


def add_to_startup():
    opened_befor = True
    file_name = '\\'+pth.basename(argv[0])
    path = argv[0].replace(file_name,'')
    if 'done.txt' not in listdir(path):
        file = open('done.txt', 'x')
    else:
        file = open('done.txt', 'r')
    if (file.read()) != '1':
        path = argv[0].replace('main.py','add_to_startup - Shortcut')
        copy(path, startup())
        file.close()
        file = open('done.txt', 'w')
        file.write('1')
        opened_befor = False
    file.close()
    return opened_befor
