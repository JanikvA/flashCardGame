#!/usr/bin/env python
# -*- coding: utf-8 -*-


def clearScreen(frame):
    for widget in frame.winfo_children():
        widget.destroy()
