#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import flashCard


class userClass():
    gameDir = os.path.join(os.path.expandvars(
        "${HOME}"), ".flashCardGame/")
    if not os.path.isdir(gameDir):
        os.mkdir(gameDir)
    allUserJSONName = os.path.join(gameDir, "userInfo.json")
    open(allUserJSONName, "a")

    def __init__(self, name="user"):
        self.name = name
        self.allFlashCards = []

    def addFlashCards(self, jsonNameFC):
        self.allFlashCards += flashCard.flashCard.readFlashCardJSON(jsonNameFC)

    def loadUserInfo(self):
        self.allFlashCards += flashCard.flashCard.readFlashCardJSON(
            userClass.allUserJSONName)

    def writeUserInfo(self):
        # data = {"flashCards": {i: fc.getDictJSON()
        #                        for i, fc in enumerate(self.allFlashCards)}}
        data = {"flashCards": [fc.getDictJSON()
                               for fc in self.allFlashCards]}
        print(data)
        with open(userClass.allUserJSONName, 'w') as outfile:
            json.dump(data, outfile)
