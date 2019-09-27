#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class flashCard:
    def __init__(self):
        self.content = {"front": None, "back": None}

    #  TODO: implement audio and image arguments <27-09-19, Janik von Ahnen> #
    def setContent(self, side, text=None):
        if side not in self.content.keys():
            raise ValueError(
                "flashCard.setContent: side argument is not 'front' or 'back'!"
            )
        fcc = flashCardContent(text=text)
        self.content[side] = fcc

    def showContent(self, side):
        self.content[side].show()

    def flip(self, arg):
        pass

    @classmethod
    def readFlashCardJSON(self, jsonName):
        flashCards = []
        with open(jsonName) as json_file:
            data = json.load(json_file)
            for cards in data["flashCards"]:
                flashC = flashCard()
                flashCards.append(flashC)
                for side in cards:
                    flashC.setContent(side, **cards[side])
        return flashCards


class flashCardContent:
    def __init__(self, text=None):
        self.text = text

    def show(self):
        print(self.text)
