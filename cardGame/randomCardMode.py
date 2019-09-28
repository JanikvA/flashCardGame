#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import random


class randomCardMode(tk.Frame):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.randomCardMode = tk.Button(
            text='next', command=self.next).pack(fill="none")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).pack(side="bottom")

    def next(self):
        nextCard = random.choice(self.user.allFashCards)
        nextCard.showContent("front")

    @classmethod
    def load(cls, frame, user):
        print(" #### *!*Debug*!* #### , self.user 2", user)
        print(" #### *!*Debug*!* #### , 2 ", user.allFashCards)
        obj = randomCardMode(master=frame, user=user)
        # obj.create_widgets()
        # obj.mainloop()
