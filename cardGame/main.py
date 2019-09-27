#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import randomCardMode


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.randomCardMode = tk.Button(self)
        self.randomCardMode["text"]="Start random card mode!"
        self.randomCardMode["command"] = self.startRCM
        self.randomCardMode.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def startRCM(self):
        self.clearScreen()
        randomCardMode.main(self.master)

    def clearScreen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        


def main(args):
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple game for learning flash cards.")
    args = parser.parse_args()
    main(args)
