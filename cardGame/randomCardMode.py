#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import random
import utils


class randomCardMode(tk.Frame):
    def __init__(self, master=None, userName=None):
        super().__init__(master)
        self.master = master
        self.user = userName
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.randomCardMode = tk.Button(
            text='next', command=self.next).pack(fill="none")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).pack(side="bottom")

    def next(self):
        nextCard = random.choice(self.user.allFlashCards)
        nextCard.showContent("front")
        self.cardLabel = tk.Button(self.master,
                                   text=nextCard.content["front"].__repr__(), command=lambda: self.showFullCard(nextCard)).pack(fill="none")
        for widget in self.master.winfo_children():
            print(widget)

    def showFullCard(self, flashCard):
        utils.clearScreen(self.master)
        self.create_widgets()
        self.cardLabel = tk.Button(self.master,
                                   text=flashCard.fullCardContent(), command=self.next).pack(fill="none")

    @classmethod
    def load(cls, frame, user):
        obj = randomCardMode(master=frame, userName=user)
