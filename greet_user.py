from os import system


def greetUser(first_launch):
    if first_launch:
        print(
            """
Hello user, welcome to the windows starup assistant.
my job is to set up your workspace as your pc start while you go get some coffee :)
all the programs you want to be opened in the next pc starup"""
        )
    else:
        print("welcome back user!\n")
