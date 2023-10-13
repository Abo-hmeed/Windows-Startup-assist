import os
import sys


def open_programs():
    path = sys.argv[0].replace('\\open programs.py','')
    if 'programs' not in os.listdir(path):
        os.mkdir('programs')
    path = path + '\\programs'
    if len(os.listdir(path)) == 1:
        os.startfile(path)
    else:
        for i in os.listdir(path):
            os.startfile(path+'\\'+i)