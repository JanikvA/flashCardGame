#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import random
import utils
import main
import copy


class choicesGame(tk.Frame):
    def __init__(self, master=None, userName=None):
        super().__init__(master)
        self.master = master
        self.user = userName
        self.grid()
        self.nButtons = 10
        self.create_widgets()
        self.currentFlashCard = None
        self.questionShows = ["Chinese", "Pinyin"]
        self.answerShows = ["English"]
        self.flashCardSubset = self.user.getFlashCardSubset(nCards=20)

        self.master.bind('j', lambda event: self.next())

    def create_widgets(self):

        self.quit = tk.Button(self, text="QUIT(q)", fg="red",
                              command=self.master.destroy).grid()

        self.loadMain = tk.Button(self)
        self.loadMain["text"] = "Main menu(m)",
        self.loadMain["fg"] = "blue",
        self.loadMain["command"] = lambda: main.Application.loadMainMenu(
            frame=self.master, usr=self.user)
        self.loadMain.grid()

        self.choicesG = tk.Button(self)
        self.choicesG["text"] = "next(j)"
        self.choicesG["command"] = self.next
        self.choicesG.grid()

        self.cardLabel = tk.Label(self)
        self.cardLabel.config(font=("helvetica", 22))
        self.cardLabel.grid(row=3, column=2, pady=30)

        # self.answerButtons={i:None for i in range(self.nButtons)}
        self.answerButtons = {}
        for buttonN in range(self.nButtons):
            newButton = tk.Button(self)
            newButton["text"] = "{n}".format(n=buttonN)
            # newButton["command"] = self.checkCorrect
            if buttonN % 2:
                newButton.grid(row=4+buttonN-1, column=1, padx=5, pady=5)
            else:
                newButton.grid(row=4+buttonN, column=3, padx=5, pady=5)
            self.answerButtons[buttonN] = newButton

    #  TODO: Implement back? <29-09-19, Janik von Ahnen> #

    def next(self):
        self.choicesG["command"] = self.answerFirst
        self.master.bind('j', lambda event: self.answerFirst())
        for s in self.master.grid_slaves():
            if s.__class__.__name__ == 'Label':
                s.destroy()
        nextCard = random.choice(self.flashCardSubset)
        self.currentFlashCard = nextCard
        self.cardLabel["text"] = nextCard.showCardContent(
            show=self.questionShows)

        randomSubset = self.user.getFlashCardSubset(nCards=10)
        rightButton = random.randint(0, self.nButtons-1)
        for k, b in self.answerButtons.items():
            b.configure(bg=self.master.cget("bg"))
            if k == rightButton:
                b["text"] = self.currentFlashCard.showCardContent(
                    show=self.answerShows)+"({n})".format(n=str(k))
                b["command"] = lambda: self.correctAnswer(rightButton)
                self.master.bind(
                    str(k), lambda event: self.correctAnswer(rightButton))
            else:
                self.master.bind(
                    str(k), lambda event: self.wrongAnswer(k, rightButton))
                b["text"] = randomSubset[k].showCardContent(
                    show=self.answerShows)+"({n})".format(n=str(k))
                b["command"] = lambda: self.wrongAnswer(int(k), rightButton)

    def correctAnswer(self, buttonPressed):
        self.answerButtons[buttonPressed].configure(bg="green")
        self.choicesG["command"] = self.next
        self.master.bind('j', lambda event: self.next())

    def wrongAnswer(self, buttonPressed, correctButton):
        # FIXME always button 9 is displayed red. i guess this is beacuse the lambda is evaluated during runtime and k is always at the end of the loop at that point?
        # self.answerButtons[buttonPressed].configure(bg="red")
        self.answerButtons[correctButton].configure(bg="green")
        self.choicesG["command"] = self.next
        self.master.bind('j', lambda event: self.next())

    def showFullCard(self, flashCard):
        self.choicesG["text"] = "next (j)"
        self.choicesG["command"] = self.next
        self.cardLabel["text"] = flashCard.showCardContent()
        self.master.bind('j', lambda event: self.next())

    def answerFirst(self):
        pass

    @classmethod
    def load(cls, frame, user):
        obj = choicesGame(master=frame, userName=user)
