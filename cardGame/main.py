#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import randomCardMode
import loadFlashCards
import utils
import userCards


class Application(tk.Frame):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.startRCM = tk.Button(
            text='Random card mode', command=self.startRCM).pack(fill="none")

        self.loadFlashCards = tk.Button(
            text='Load flash cards', command=self.loadFlashCards).pack(fill="none")

        self.quit = tk.Button(
            self, text="QUIT", fg="red", command=self.master.destroy
        )
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def loadFlashCards(self):
        utils.clearScreen(self.master)
        loadFlashCards.loadFlashCards.load(frame=self.master, user=self.user)

    def startRCM(self):
        utils.clearScreen(self.master)
        randomCardMode.randomCardMode.load(frame=self.master, user=self.user)


def main(args):
    #  TODO: Handle user login properly <28-09-19, Janik von Ahnen> #
    dummyUser = userCards.userClass(name="Janik")
    dummyUser.loadUserInfo()
    root = tk.Tk()
    app = Application(master=root, user=dummyUser)
    app.mainloop()
    dummyUser.writeUserInfo()



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Simple game for learning flash cards."
    )
    args = parser.parse_args()
    main(args)
