#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class flashCard:
    def __init__(self):
        self.content = {}

    #  TODO: implement audio and image arguments <27-09-19, Janik von Ahnen> #
    def setContent(self, side, text=None):
        fcc = flashCardContent(text=text)
        self.content[side] = fcc

    def showContent(self, side):
        self.content[side].show()

    def flip(self, arg):
        pass

    def getDictJSON(self):
        di = {}
        for k, v in self.content.items():
            di[k] = v.getDictJSON()
        return di

    def fullCardContent(self):
        prettyString = ""
        tmpD = self.getDictJSON()
        for k in tmpD:
            prettyString += str(k)+"  :  "+str(tmpD[k])+"\n--------\n"
        return prettyString

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

    def getDictJSON(self):
        di = {}
        for attr in ["text"]:
            di[attr] = getattr(self, attr)
        return di

    def __repr__(self):
        prettyString = ""
        for k in self.__dict__:
            prettyString += str(k)+"  :  "+str(self.__dict__[k])+"\n--------\n"
        return prettyString
