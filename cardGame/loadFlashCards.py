#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter.filedialog import askopenfilename
import main


class loadFlashCards(tk.Frame):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()

        self.master.bind('o', lambda event: self.callback())

    def create_widgets(self):
        self.loadFlashCards = tk.Button(
            text='File Open(o)', command=self.callback).pack(fill="none")

        self.quit = tk.Button(self, text="QUIT(q)", fg="red",
                              command=self.master.destroy).pack(side="bottom")

        self.loadMain = tk.Button(self, text="Main menu(m)", fg="blue",
                command=lambda: main.Application.loadMainMenu(frame=self.master, usr=self.user)).pack(side="bottom")

    def callback(self):
        name = askopenfilename()
        if name:
            self.user.addFlashCards(name)

    @classmethod
    def load(cls, frame, user):
        obj = loadFlashCards(master=frame, user=user)
