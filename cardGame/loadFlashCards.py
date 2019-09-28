#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter.filedialog import askopenfilename


class loadFlashCards(tk.Frame):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.loadFlashCards = tk.Button(
            text='File Open', command=self.callback).pack(fill="none")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).pack(side="bottom")

    def callback(self):
        name = askopenfilename()
        self.user.addFlashCards(name)

    @classmethod
    def load(cls, frame, user):
        obj = loadFlashCards(master=frame, user=user)
