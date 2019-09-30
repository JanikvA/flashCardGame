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
        #  TODO: Make allFlashCards uniq <29-09-19, Janik von Ahnen> # 
        self.allFlashCards = []

    def addFlashCards(self, jsonNameFC):
        self.allFlashCards += flashCard.flashCard.readFlashCardJSON(jsonNameFC)

    def loadUserInfo(self):
        self.allFlashCards += flashCard.flashCard.readFlashCardJSON(
            userClass.allUserJSONName)

    def resetUserInfo(self):
        #FIXME make a pop up open to ask if user is sure
        print("Data for {usr} has been reseted!".format(usr=self.name))
        self.allFlashCards=[]

    def writeUserInfo(self):
        data = {"flashCards": [fc.content
                               for fc in self.allFlashCards]}
        print(data)
        with open(userClass.allUserJSONName, 'w') as outfile:
            json.dump(data, outfile)
