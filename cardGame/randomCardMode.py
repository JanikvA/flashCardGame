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
        self.randomCardMode = tk.Button(
            text='next', command=self.next).pack(fill="none")
        self.showSolution = tk.Button(
            text='show solution', command=lambda: self.showFullCard(self.currentFlashCard)).pack(fill="none")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).pack(side="bottom")

    def next(self):
        for s in self.master.pack_slaves():
            if s.__class__.__name__ == 'Label':
                s.destroy()
        nextCard = random.choice(self.user.allFlashCards)
        self.currentFlashCard = nextCard
        self.cardLabel = tk.Label(
            self.master, text=nextCard.content[random.choice(list(nextCard.content.keys()))].__repr__()).pack()

    def showFullCard(self, flashCard):
        self.cardLabel = tk.Label(
            self.master, text=flashCard.fullCardContent()).pack()

    @classmethod
    def load(cls, frame, user):
        obj = randomCardMode(master=frame, userName=user)
