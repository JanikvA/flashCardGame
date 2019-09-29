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

        # self.master.bind('<KP_1>', lambda event: self.startRCM())
        # self.master.bind('<KP_2>', lambda event: self.loadFlashCards())
        # self.master.bind('<KP_9>', lambda event: self.master.destroy())

    def create_widgets(self):
        self.startRCM = tk.Button(self)
        self.startRCM["text"]='Random card mode(1)'
        self.startRCM["command"]=self.startRCM
        self.startRCM.pack(fill="none")

        self.loadFlashCards = tk.Button(
            text='Load flash cards(2)', command=self.loadFlashCards).pack(fill="none")

        self.quit = tk.Button(
            self, text="QUIT(9)", fg="red", command=self.master.destroy
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
