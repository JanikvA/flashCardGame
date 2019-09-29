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
        self.currentFlashCard = None

    def create_widgets(self):

        self.randomCardMode=tk.Button(self)
        self.randomCardMode["text"] = "next"
        self.randomCardMode["command"] = self.next
        self.randomCardMode.pack(side="top")

        self.cardLabel = tk.Label(self)
        self.cardLabel.pack()
        # self.randomCardMode = tk.Button(self,
            # text='next', command=self.next).pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).pack(side="bottom")

    #  TODO: Implement back? <29-09-19, Janik von Ahnen> # 
    def next(self):
        self.randomCardMode["text"]="show solution"
        self.randomCardMode["command"]=lambda: self.showFullCard(self.currentFlashCard)
        for s in self.master.pack_slaves():
            if s.__class__.__name__ == 'Label':
                s.destroy()
        nextCard = random.choice(self.user.allFlashCards)
        self.currentFlashCard = nextCard
        self.cardLabel["text"]=nextCard.content[random.choice(list(nextCard.content.keys()))].__repr__()

    def showFullCard(self, flashCard):
        self.randomCardMode["text"]="next"
        self.randomCardMode["command"]=self.next
        self.cardLabel["text"]=flashCard.fullCardContent()
        # self.cardLabel = tk.Label(
        #     self.master, text=flashCard.fullCardContent()).pack()

    @classmethod
    def load(cls, frame, user):
        obj = randomCardMode(master=frame, userName=user)