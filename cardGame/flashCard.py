#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os


class flashCard:
    def __init__(self):
        self.content = {}

    def getContent(self, attr):
        return self.content[attr]

    def flip(self, arg):
        pass

    def showCardContent(self, show=None, dontShow=[]):
        prettyString = ""
        if show is None:
            show = list(self.content.keys())
        for k in show:
            if k in dontShow:
                continue
            try:
                prettyString += str(k)+"  :  "+str(self.content[k])+"\n--------\n"
            except KeyError:
                print("WARNING: {ky} not in this flash card".format(ky=k))
                return self.showCardContent()
        return prettyString

    @classmethod
    def readFlashCardJSON(self, jsonName):
        flashCards = []
        if not os.path.isfile(jsonName):
            print("WARNING: {jsonfile} does not exist!".format(
                jsonfile=jsonName))
            return flashCards
        with open(jsonName) as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                print("WARNING: {jsonfile} can not be loaded! Wrong format?".format(
                    jsonfile=jsonName))
                return flashCards
            for cards in data["flashCards"]:
                flashC = flashCard()
                flashCards.append(flashC)
                for side in cards:
                    flashC.content[side] = cards[side]
        return flashCards
