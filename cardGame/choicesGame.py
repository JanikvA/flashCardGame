#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import random
import utils
import main


class choicesGame(tk.Frame):
    def __init__(self, master=None, userName=None):
        super().__init__(master)
        self.master = master
        self.user = userName
        self.grid()
        self.create_widgets()
        self.currentFlashCard = None
        self.questionShows=["Chinese", "Pinyin"]
        self.answerShows=["English"]
        self.flashCardSubset=self.user.getFlashCardSubset(nCards=20)

        self.master.bind('j', lambda event: self.next())
    def create_widgets(self):

        self.quit = tk.Button(self, text="QUIT(q)", fg="red",
                              command=self.master.destroy).grid()

        self.loadMain = tk.Button(self)
        self.loadMain["text"]="Main menu(m)",
        self.loadMain["fg"]="blue",
        self.loadMain["command"]=lambda: main.Application.loadMainMenu(frame=self.master, usr=self.user)
        self.loadMain.grid()

        self.choicesG=tk.Button(self)
        self.choicesG["text"] = "next(j)"
        self.choicesG["command"] = self.next
        self.choicesG.grid()

        self.cardLabel = tk.Label(self)
        self.cardLabel.config(font=("Courier", 22))
        self.cardLabel.grid(row=3, column=2, pady=30)



    #  TODO: Implement back? <29-09-19, Janik von Ahnen> # 
    def next(self):
        self.choicesG["text"]="show solution (j)"
        self.choicesG["command"]=lambda: self.showFullCard(self.currentFlashCard)
        for s in self.master.grid_slaves():
            if s.__class__.__name__ == 'Label':
                s.destroy()
        nextCard = random.choice(self.flashCardSubset)
        self.currentFlashCard = nextCard
        # self.cardLabel["text"]=nextCard.content[random.choice(list(nextCard.content.keys()))].__repr__()
        self.cardLabel["text"]=nextCard.showCardContent(show=self.questionShows)
        self.master.bind('j', lambda event: self.showFullCard(self.currentFlashCard))

    def showFullCard(self, flashCard):
        self.choicesG["text"]="next (j)"
        self.choicesG["command"]=self.next
        self.cardLabel["text"]=flashCard.showCardContent()
        self.master.bind('j', lambda event: self.next())

    @classmethod
    def load(cls, frame, user):
        obj = randomCardMode(master=frame, userName=user)
