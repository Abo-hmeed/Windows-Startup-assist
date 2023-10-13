from sys import argv
from shutil import copy
from winshell import startup

def add_to_startup():
    file = open('done.txt', 'r')
    print()
    if (file.read()) == '0':
        path = argv[0].replace('main.py','add_to_startup - Shortcut')
        print(path)
        copy(path, startup())
        file.close()
        file = open('done.txt', 'w')
        file.write('1')
    file.close()
