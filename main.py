from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


class GUI:
    def __init__(self, app_naam: str):
        self.app_naam = app_naam
        self.root = Tk()
        self.app = Window(self.root)
        self.__runtime__()  # Initiate app

    def __runtime__(self):
        self.root.geometry('300x200')
        self.root.wm_title(self.app_naam)
        self.__make_label__("Mijn naam is")
        self.__make_entry__()
        self.root.mainloop()

    def __make_label__(self, text: str):
        labelVar = StringVar()
        label = Label(
            self.root,
            textvariable=labelVar,
            relief=RAISED,
            bg='#000',
            fg='#fff'
        )
        labelVar.set(text)
        label.pack()

    def __make_entry__(self):
        e1 = Entry(self.root, bd=5, bg="#000", fg="#fff")
        e1.pack(side=RIGHT)

if __name__ == '__main__':
    gui = GUI(
        app_naam="Begroeter"
    )
