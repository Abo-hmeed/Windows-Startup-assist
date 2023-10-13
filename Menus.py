class Choice:
    choice_text = ""
    choice_index = 0

    def __init__(self, index: int, text=""):
        self.choice_text = text
        self.choice_index = index

    def show_choice(self):
        if self.choice_index != 0:
            print("%i) %s" % (self.choice_index, self.choice_text))
        else:
            print("%s" % (self.choice_text))


class Menu:
    menu_title = ""
    choices = []

    def __init__(self, title, num_of_choices):
        self.menu_title = title
        for num in range(num_of_choices):
            choice = Choice(num + 1, "Example Choice")
            self.choices.append(choice)

    def show_menu(self):
        print("\t\t %s \t\t\n" % (self.menu_title))
        for choice in self.choices:
            choice.show_choice()

    def change_choice_label(self, index, new_label):
        self.choices[index].choice_text = new_label


# menu = Menu("Main menu", 2)
# menu.change_choice_label(0, "open programs folder")       This is how the code works!
# menu.change_choice_label(1, "exit")
# menu.show_menu()
