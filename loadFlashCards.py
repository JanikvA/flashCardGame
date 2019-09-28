#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import userCards
# from tkFileDialog import askopenfilename


class loadFlashCards(tk.Frame):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.loadFlashCards = tk.Button(
            text='File Open', command=callback).pack(fill="top")

    def callback(self):
        name = tk.tkFileDialog.askopenfilename()
        self.user.addFlashCards(name)

    @classmethod
    def load(cls, frame):
        obj = loadFlashCards(master=frame)
        obj.mainloop()
