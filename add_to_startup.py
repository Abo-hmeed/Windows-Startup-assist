import sys
import os
import shutil


def add_to_startup():
    file = open('done.txt', 'r')
    print()
    if (file.read()) == '0':
        path = sys.argv[0].replace('main.py','add_to_startup - Shortcut')
        print(path)
        shutil.copy(path, r'C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
        file.close()
        file = open('done.txt', 'w')
        file.write('1')
    file.close()
