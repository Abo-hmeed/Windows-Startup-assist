from Menus import Menu
import os


def mainMenu():
    mainMenu = Menu("Main Menu", 2)
    mainMenu.change_choice_label(0, "open programs folder")
    mainMenu.change_choice_label(1, "Exit")

    while TypeError:
        mainMenu.show_menu()
        try:
            user_choice = int(input("Enter your Choice: "))
            return user_choice
        except:
            os.system("cls")
            print("Invaild choice!")


choice = mainMenu()
print(str(choice))
