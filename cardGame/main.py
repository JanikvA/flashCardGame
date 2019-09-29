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

        self.master.bind('j', lambda event: self.startRCM())
        self.master.bind('l', lambda event: self.loadFlashCards())
        self.master.bind('q', lambda event: self.master.destroy())

    def create_widgets(self):
        self.startRandomCardMode = tk.Button(self)
        self.startRandomCardMode["text"]='Random card mode(j)'
        self.startRandomCardMode["command"]=self.startRCM
        self.startRandomCardMode.pack(fill="none")

        self.loadFlashCards = tk.Button(
            text='Load flash cards(l)', command=self.loadFlashCards)
        self.loadFlashCards.pack()

        self.quit = tk.Button(
            self, text="QUIT(q)", fg="red", command=self.master.destroy
        )
        self.quit.pack(side="bottom")


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
