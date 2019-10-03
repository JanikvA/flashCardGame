#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
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

    def resetUserInfo(self):
        #FIXME make a pop up open to ask if user is sure
        print("Data for {usr} has been reseted!".format(usr=self.name))
        self.allFlashCards=[]

    def writeUserInfo(self):
        data = {"flashCards": [fc.content
                               for fc in self.allFlashCards]}
        with open(userClass.allUserJSONName, 'w') as outfile:
            json.dump(data, outfile)

    def getFlashCardSubset(self, nCards=20, sortByMemScore=False):
        subset=[]
        if sortByMemScore:
            lowestMemScore=sorted(self.allFlashCards, key=lambda fc: fc.calcMemoryScore())
            subset=lowestMemScore[:nCards]
        else:
            while len(subset)<nCards and len(subset)<len(self.allFlashCards):
                randomCard=random.choice(self.allFlashCards)
                if randomCard in subset:
                    continue
                else:
                    subset.append(randomCard)
        return subset
        
